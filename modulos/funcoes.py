from time import sleep
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

dic = dict()

def interface():
    while True:
        sleep(0.2)
        print('-='*60)
        sleep(0.2)
        print("""
    [ 1 ] Listar inventário
    [ 2 ] Adicionar item ao inventário
    [ 3 ] Remover item do inventário
    [ 4 ] Buscar item no inventário
    [ 5 ] Sair
            """)
        sleep(0.2)
        print('-='*60)
        sleep(0.2)
        escolha = input('\nEscolha sua opção: ').strip() 

        #Caso o usuário escolha opção 1, seguimos com a listagem do inventário
        if escolha == '1':
            list_inventario()

        elif escolha == '2':
            item = str(input('Digite o item que deseja buscar')).lower()
            quantidade = int('Quanto possui desse item?')
            add_item(dic, item, quantidade)
            
        elif escolha == '3':
            item = str(input('Digite o item que deseja excluir')).lower()
            rem_item(dic, item)

        elif escolha == '4':
            item = str(input('Digite o item que deseja buscar')).lower()
            print(find_item(dic, item))

        elif escolha == '5':
            break
        
        #Tratamento caso o usuário não escolha nenhuma das opções disoníveis
        else:
            sleep(0.2)
            print("\n\033[31mPor favor, escolha uma opção válida!\033[m")