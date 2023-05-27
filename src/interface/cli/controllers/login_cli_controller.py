from getpass import getpass

from src.application.exceptions.user_not_found_exception import UserNotFoundException
from src.application.exceptions.invalid_credentials_exception import InvalidCredentialsException

from src.application.usecases.login_usecase import LoginUsecase

class LoginCLIController:
    usecase = LoginUsecase

    def __init__(self):
        self.usecase = LoginUsecase()

    def execute(self):
        try:
            email = input('Digite o seu email: ')
            password = getpass('Digite a sua senha: ')

            result = self.usecase.execute(email, password)

            print(result)
        except UserNotFoundException:
            print('Credenciais Inválidas')
        except InvalidCredentialsException:
            print('Credenciais Inválidas')
