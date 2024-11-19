from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Tambahkan klaim kustom di sini
        token['name'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_superuser'] = user.is_superuser
        token['groups'] = list(user.groups.values_list('name', flat=True))
        
        # Klaim lainnya (opsional)
        # Contoh:
        # token['email'] = user.email
        # token['department'] = user.department  (jika ada field 'department' di model User)
        return token
