import os

def listar_pasta(caminho, nivel=0, arquivo=None):
    # Lista de pastas a serem ignoradas
    pastas_ignoradas = {'.venv', '.idea'}

    # Itera sobre todos os itens na pasta
    for item in os.listdir(caminho):
        # Cria o caminho completo do item
        caminho_completo = os.path.join(caminho, item)

        # Ignora pastas especificadas
        if os.path.isdir(caminho_completo) and item in pastas_ignoradas:
            continue

        # Adiciona o item ao arquivo com indentação baseada no nível
        if arquivo:
            arquivo.write("  " * nivel + "|-- " + item + "\n")

        # Se o item for um arquivo de código, inclui o conteúdo no arquivo
        if os.path.isfile(caminho_completo):
            # Verifica a extensão do arquivo para determinar se é um arquivo de código
            if caminho_completo.endswith(('.py', '.js', '.java', '.c', '.cpp', '.h')):
                arquivo.write("  " * (nivel + 1) + "Conteúdo:\n")
                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                    for linha in f:
                        arquivo.write("  " * (nivel + 2) + linha)
        # Se o item for uma pasta, chama a função recursivamente
        elif os.path.isdir(caminho_completo):
            listar_pasta(caminho_completo, nivel + 1, arquivo)

# Caminho da pasta que você quer listar
caminho_da_pasta = './'

# Caminho do arquivo .txt onde a listagem será salva
caminho_arquivo = 'listagem_pasta.txt'

# Abre o arquivo para escrita
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    listar_pasta(caminho_da_pasta, arquivo=arquivo)

print(f"A listagem foi salva em {caminho_arquivo}")
