from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email or not password:
            raise ValueError("Email and password fields must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_active", False)
        kwargs.setdefault("is_superuser", False)

        if not kwargs.get("is_staff") or not kwargs.get("is_superuser"):
            raise ValueError("Fields 'is_staff' and 'is_superuser' must be set True")

        user = self.create_user(email, password, **kwargs)
        return user
