import os

def listar_arquivos_pasta_primeiro_nivel(diretorio):
    # Lista todos os arquivos e pastas dentro do diretório (apenas no primeiro nível)
    lista_itens = []
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isdir(caminho_completo) or item.endswith('.exe') or item.endswith('.rar') or item.endswith('.zip'):
            lista_itens.append(item)
    return lista_itens

def salvar_em_txt(lista, nome_arquivo):
    # Salva a lista de itens em um arquivo de texto
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_txt:
        for item in lista:
            arquivo_txt.write(item + '\n')

# Diretório que você quer listar os arquivos e pastas
diretorio = 'D:/DLL/npc'

# Obtém a lista de arquivos, pastas, .exe e .rar do primeiro nível
itens_primeiro_nivel = listar_arquivos_pasta_primeiro_nivel(diretorio)

# Nome do arquivo de texto onde a lista será salva
nome_arquivo_txt = 'lista_de_itens.txt'

# Salva a lista de arquivos, pastas, .exe e .rar em um arquivo de texto
salvar_em_txt(itens_primeiro_nivel, nome_arquivo_txt)

print(f"Lista de arquivos, pastas, .exe e .rar do primeiro nível salva em {nome_arquivo_txt}")
