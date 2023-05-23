import os
#verifica se arquivos existem
print(os.path.exists('calc.py'))
print(os.path.exists('texto.py'))
print(os.path.exists('arquivos/teste.txt'))

#Verifica se diretórios existem
print(os.path.exists('arquivos'))
print(os.path.exists('arquivos/pastanova'))

#exemplo de caminhos
print(os.path.exists('arquivos/pastanova/texto.py'))

#criar pastas
os.mkdir('olamundo')
