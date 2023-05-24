import os
#verificar se arquivos existem
print(os.path.exists('calc.py'))
print(os.path.exists('texto.py'))
print(os.path.exists('arquivos/teste.txt'))

#Verificar se diretórios existem
print(os.path.exists('arquivos'))
print(os.path.exists('arquivos/pastanova'))

#exemplo de caminhos
print(os.path.exists('arquivos/pastanova/texto.py'))

#criar arquivo
open('./olamundo/aa.txt', 'w')

#criar pasta
os.mkdir('olamundo/Teste')
os.mkdir('./Teste/Teste2')

#Apagar arquivos
os.remove('./arquivos/pastanova/texto.py')
#Apagar diretório
os.rmdir('./arquivos/pastanova')
#renomear arquivos
os.rename('./olamundo/aa.txt', 'puts.jar')
#abrir e ler arquivos.
arquivo = open('./#Args.py')
print(arquivo.read())
#fechar arquivos
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
#escrever coisas em arquivos['a' = append(adiciona coisas), 'w' = write(Troca o texto por: ), 'r' = read(Ler arquivos.)]
texto = """
Teste teste teste



"""
arquivo = open('./arquivos/teste.txt', 'a')
arquivo.write(texto)
