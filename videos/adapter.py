from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

class CustomAccountAdapter(DefaultAccountAdapter):
    def authenticate(self, request, **credentials):
        User = get_user_model()
        username = credentials.get(User.USERNAME_FIELD)
        if username is None:
            # If username is None, try to get it from email field
            username = credentials.get('email')
        if username is None:
            return None
        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            # Run the default authenticate method
            return super().authenticate(request, **credentials)
        else:
            # Check if the user has the correct password
            if user.check_password(credentials['password']):
                return user
        return None
