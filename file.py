def list_inventario(dict):
    
    """
    Retorna o dicionário completo.
    :param dict: dict.
    :return dict listando o inventário.
    """
    try:
        for item in dict:
            print(f'O item {item} possui {dict[item]} unidades')
    except:
        print('Parâmetro em tipo primitivo diferente')

def add_item(dict, item, quantidade):
    """
    Adiciona item ao dicionário do inventário
    :param dict: dict.
    :param item: str.
    :param quantidade: int.
    :return dict adiciona x ao inventário
    """
    try:
        if item in dict.keys():
            print(f'Este item já está no inventário e possui {dict[item]} unidade(s)')
        else:
            dict[item] = quantidade
    except:
        print('Parâmetro em tipo primitivo diferente')

def rem_item(dict, item):
    """
    Remove item do dicionário do inventário
    :param dict: dict.
    :param item: str.
    :return dict remove item do dict
    """
    try:
        if item in dict.keys():
            dict.pop(item)
        else:
            print('Este item não estava no inventário')
    except:
        print('Parâmetro em tipo primitivo diferente')

def find_item(dict, item):
    """
    Busca item no dicionário do inventário
    :param dict: dict.
    :param item: str
    :return Bool caso item no dict retorna True
    """
    try:
        if item in dict.keys():
            return True
        else:
            return False
    except:
        print('Parâmetro em tipo primitivo diferente')