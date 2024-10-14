import os

# Função para criar arquivos e pastas
def criar_arquivos_e_pastas(palavras):
    # Cria a pasta 'entry' se não existir
    os.makedirs('entry', exist_ok=True)
    
    for palavra in palavras:
        palavra = palavra.strip()
        if palavra:  # Verifica se não está vazio
            # Verifica se a palavra contém um ponto
            if '.' in palavra:
                # Se contiver um ponto, cria um arquivo dentro da pasta 'entry'
                file_path = os.path.join('entry', palavra)
                with open(file_path, 'w') as f:
                    f.write(f"# Arquivo criado: {palavra}\n")
                print(f"Arquivo criado: {file_path}")
            else:
                # Se não contiver um ponto, cria uma pasta dentro da pasta 'entry'
                dir_path = os.path.join('entry', palavra)
                os.makedirs(dir_path, exist_ok=True)
                print(f"Pasta criada: {dir_path}")

# Ler palavras de um arquivo .txt
def ler_palavras(arquivo_txt):
    palavras = []
    with open(arquivo_txt, 'r') as f:
        for linha in f:
            palavras.extend(linha.split())
    return palavras

# Nome do arquivo de entrada
arquivo_txt = 'entry.txt'  # Altere para o nome do seu arquivo .txt

# Chamar funções
palavras_lidas = ler_palavras(arquivo_txt)
criar_arquivos_e_pastas(palavras_lidas)
