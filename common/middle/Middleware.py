from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info == '/user/login/' or request.path_info == '/user/register/':
            return
        user = request.session.get("userinfo")
        if user:
            return
        return redirect("/user/login/")

    def process_response(self, request, response):
        return response
