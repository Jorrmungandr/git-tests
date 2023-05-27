from src.domain.entities.user_entity import UserEntity

class UserRepository:
    def get_user_by_email(self, user_email):
        with open('./db/users.csv', 'r', encoding='utf8') as csv_file:
            for user_line in csv_file.readlines()[1:]:
                _id, name, email, password = user_line.split(',')

                if email != user_email:
                    continue

                user_entity = UserEntity(_id, name, email, password)

                return user_entity

            return None

    def create_user(self, name, email, password):
        with open('./db/users.csv', 'r+', encoding='utf8') as csv_file:
            _id = len(csv_file.readlines())

            csv_file.write(f'\n{_id},{name},{email},{password}')

            return UserEntity(_id, name, email, password)
