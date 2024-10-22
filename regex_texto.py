import re

# Carregar o conteúdo do arquivo
with open('Caminho do arquivo', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'padrão do regex a ser usado'

# exemplo de uso: Função para adicionar o pipe ao final do valor achado
def add_pipe(match):
    return match.group(0) + ' |'

# Substituição do valor origianl pelo novo valor
updated_content = re.sub(pattern, add_pipe, content, flags=re.MULTILINE)

# Salvar o conteúdo atualizado em um novo arquivo
with open('caminho do novo arquivo', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("Texto atualizado e salvo com sucesso!")