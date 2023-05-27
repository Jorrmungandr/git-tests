from src.application.exceptions.user_not_found_exception import UserNotFoundException
from src.application.exceptions.invalid_credentials_exception import InvalidCredentialsException

from src.infrastructure.in_file_storage.user_repository import UserRepository

class LoginUsecase:
    def __init__(self):
        self.repository = UserRepository()

    def execute(self, email, password):
        user = self.repository.get_user_by_email(email)

        if not user:
            raise UserNotFoundException('Usuário não encontrado')

        if user.password != password:
            raise InvalidCredentialsException('Senha incorreta')

        return user
