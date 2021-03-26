import os
print(os.path.join('usr','bin','spam'))

myFiles = ['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart',filename))
print("\n")

print(os.getcwd())
os.chdir('C:\\Users\\soumi\\OneDrive\\Documentos')
print(os.getcwd()) #ALTERAR CAMINHO DO DIRETÓRIO

os.makedirs('C:\\Users\\soumi\\OneDrive\\Documentos\\Criada_Python\\walnut\\waffles')
