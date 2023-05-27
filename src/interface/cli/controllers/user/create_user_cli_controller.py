from getpass import getpass

from src.application.exceptions.user.invalid_params_exception import InvalidParamsException
from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException

from src.application.usecases.user.create_user_usecase import CreateUserUsecase

class CreateUserCLIController:
    def __init__(self):
        self.usecase = CreateUserUsecase()

    def execute(self):
        try:
            name = input('Digite o seu nome: ')
            email = input('Digite o seu email: ')
            password = getpass('Digite a sua senha: ')
            confirm_password = getpass('Confirme a sua senha: ')

            result = self.usecase.execute(name, email, password, confirm_password)

            print(result)

            return result
        except InvalidParamsException as error:
            print(f'Erro de validação de parâmetro: {error.message}')
        except InvalidConfirmPasswordException:
            print('A confirmação de senha está diferente da senha')
