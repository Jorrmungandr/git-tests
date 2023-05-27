from src.interface.cli.controllers.auth.login_cli_controller import LoginCLIController
# from src.interface.cli.controllers.user.create_user_cli_controller import CreateUserCLIController
# from src.helpers.cli_menu_decorator import paths

# Login Cycle
login_controller = LoginCLIController()

auth_user = None

while not auth_user:
    auth_user = login_controller.execute()

# # Instanciate Controllers
# CreateUserCLIController()

# # Menu Cycle
# print(paths)
