from src.helpers.cli_menu_decorator import cli_menu

@cli_menu('Criar Usuário')
class CreateUserCLIController:
    def __init__(self):
        print('init')
