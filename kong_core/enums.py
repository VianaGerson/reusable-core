from .utils import ChoiceEnum

class TipoUsuario(ChoiceEnum):
    CLIENTE = 'CLIENTE'
    GESTOR = 'GESTOR'

    DEFAULT = 'DEFAULT'