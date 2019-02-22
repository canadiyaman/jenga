from django.contrib.auth import login, get_user_model
from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            return

        UserModel = get_user_model()
        ip = request.META['REMOTE_ADDR']
        try:
            user = UserModel.objects.get(ip=ip)
        except UserModel.DoesNotExist:
            user = UserModel.objects.create(ip=ip)

        login(request, user)
