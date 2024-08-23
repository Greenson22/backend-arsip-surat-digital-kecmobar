from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer

class UserPasswordViewSet(viewsets.GenericViewSet, 
                         mixins.UpdateModelMixin):
     queryset = User.objects.all()
     serializer_class = UserSerializer

     def update(self, request, *args, **kwargs):
          partial = kwargs.pop('partial', False)
          user = self.get_object()
          
          # Check if 'old_password' is provided and matches the current password
          if 'password' in request.data:
               if not user.check_password(request.data['password']):
                    return Response({'error': 'Password lama yang dimasukan tidak cocok'}, status=status.HTTP_400_BAD_REQUEST)
          
          user.set_password(request.data['new_password'])
          request.data.pop('new_password', None) #menghapus key new_password
          serializer = self.get_serializer(user, data=request.data, partial=partial)
          serializer.is_valid(raise_exception=True)
          self.perform_update(serializer)

          if getattr(user, '_prefetched_objects_cache', None):
               # If 'prefetch_related' has been applied to a queryset, we need to
               # forcibly invalidate the prefetch cache on the user.
               user._prefetched_objects_cache = {}

          return Response(serializer.data)