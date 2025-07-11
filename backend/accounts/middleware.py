from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from jwt.exceptions import ExpiredSignatureError
import jwt

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get('access_token')
        if token:
            try:
                """
                    Si hay token, intenta validarlo usando UntypedToken().
                    Verifica la firma.
                    Verifica si está expirado.
                    Verifica si es válido en general.
                """
                UntypedToken(token)
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
                
            except (InvalidToken,TokenError,ExpiredSignatureError):
                #bandera que me marca que el token debe ser eliminado, dado que esta vencido
                #atributo arbitrario variable
                request._delete_token_unusable = True
        #llamo a la vista o al siguiente middleware
        response = self.get_response(request)
        #elimino la cookie que fue marcada en este caso delete_token_unusable
        if getattr(request,'_delete_token_unusable',False):# es falso para evitar errores de que no exista
            response.delete_cookie('access_token')
        return response
                
            