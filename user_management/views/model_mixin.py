from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from ..models import User

class ListCustom(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_staff and user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(User.objects.filter(pk=request.user.id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RetrieveCustom(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        if request.user.is_staff and request.user.is_superuser:
            serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

class UpdateCustom(mixins.UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = request.user
        print(request.data)
        data = request.data.copy()

        if request.user.is_staff and request.user.is_superuser:
            instance = self.get_object()
        if not request.user.is_authenticated:
            return Response({'error':'AnonymousUser'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Periksa keberadaan new_password di request.data
        if 'new_password' in data:
            # jika password benar atau dia seorang admin
            if ('password' in data and instance.check_password(data['password'])) or (request.user.is_staff and request.user.is_superuser):
                data['password'] = data['new_password']
            else:
                return Response({'error':'password anda salah'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data.pop('password', None) # membuang password
        
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
class CreateCustom(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        if not (request.user.is_staff and request.user.is_superuser):
            return Response({'error':'Hanya admin yang bisa membuat user'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

class DestroyCustom(mixins.DestroyModelMixin):
     def destroy(self, request, *args, **kwargs):
        if not (request.user.is_staff and request.user.is_superuser):
            return Response({'error':'Hanya administrator yang bisa menghapus pengguna'}, status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
     
     def perform_destroy(self, instance):
        instance.delete()