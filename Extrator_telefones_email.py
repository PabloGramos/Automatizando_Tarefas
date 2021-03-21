import re, pyperclip

phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              #código de área
    (\s|-|\.)?                      #separador
    (\d{3})                         #primeiros 3 dígitos
    (\s|-|\.)                       #separador
    (\d{4})                         #últimos 4 dígitos 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extensão
)""",re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+    #nome do usuário
@                    #símbolo @
[a-zA-Z0-9.-]+       #nome do domínio
(\.[a-zA-Z]{2,4})    #ponto seguido de outros caracteres
)''',re.VERBOSE)

#Encontra as conrrespondências no texto do clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups