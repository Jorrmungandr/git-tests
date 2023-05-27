from src.application.exceptions.user.invalid_params_exception import InvalidParamsException
from src.application.exceptions.user.invalid_confirm_password_exception import InvalidConfirmPasswordException

from src.infrastructure.in_file_storage.repositories.user_repository import UserRepository

class CreateUserUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, name, email, password, confirm_password):
        if ',' in name:
            raise InvalidParamsException('Nome inválido')
        if ',' in email:
            raise InvalidParamsException('Email inválido')
        if ',' in password:
            raise InvalidParamsException('Senha inválida')

        if password != confirm_password:
            raise InvalidConfirmPasswordException('As senhas estão diferentes')

        created_user = self.repository.create_user(name, email, password)

        return created_user
