import re
phoneNumRegex = re.compile(r'(\(\d\d\))(\d\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (63)98485-7288.')
print(mo.group(1))
print(mo.group(2))
