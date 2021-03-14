import re
phoneNumRegex = re.compile(r'(\(\d\d\))?(\d\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (63)98485-7288. Work: (64)99255-0000')
haGerex = re.compile(r'(Ha){3,5}?')
mo1 = haGerex.search('HaHaHaHaHaHa')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
print(mo1.group())

mo = phoneNumRegex.findall('My number is (63)98485-7288. Work: (64)99255-0000')
print(mo) #Retorna uma lista com tuplas para cada grupo entre parenteses

xmasRegex = re.compile(r'\d+\s\w+')
ma = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swanas')
print(ma)

vowelRegex = re.compile(r'[aeiouAEIOU]')#Encontrar todas essas vogais no texto
mi = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mi)

caractereRegex = re.compile(r'[a-zA-Z0-9]')#Referir todos os valores de "a" a "z" por exemplo
mu = caractereRegex.findall('Observe a postura desde a 1 letra até a ULTIMA.')
print(mu)

consoantRegex = re.compile(r'[^aeiouAEIOU]')
me = consoantRegex.findall('RoboCop east baby food. BABY FOOD.')
print(me)

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World!') , beginsWithHello.search('He said hello.')==None)

endsWithNumber = re.compile(r'\d+$')#COM O '+' QUER DIZER UM OU MAIS NUMEROS NO FINAL DA STRING, SEM O '+' APENAS O ULTIMO NUMERO
print(endsWithNumber.search('You number is 42') , endsWithNumber.search('You number is forty two.')==None)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on tyhe flat mat.'))

nameRegex = re.compile(r'First Name:(.*)Last Name:(.*)')
mo = nameRegex.search('First Name: Al stop, lefth Last Name: Sweigart')
print(mo.group(1),mo.group(2))

robocop = re.compile(r'robocop',re.I)
print(robocop.search('RoboCop is part man.').group())

nomesRegex = re.compile(r'Agent \w+') # Vai substituir a palavra selecionanda e a proxima por CENSORED
print(nomesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.'))

