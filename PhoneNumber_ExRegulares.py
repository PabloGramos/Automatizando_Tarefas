import re
phoneNumRegex = re.compile(r'(\(\d\d\))?(\d\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (63)98485-7288.')
haGerex = re.compile(r'(Ha){3,5}')
mo1 = haGerex.search('HaHaHaHa')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
print(mo1.group())