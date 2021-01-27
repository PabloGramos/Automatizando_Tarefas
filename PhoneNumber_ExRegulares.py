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



