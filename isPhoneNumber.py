def isPhoneNumber(text):
	if len(text) != 13:
		return False
	for i in range(0,2):
		if not text[i].isdecimal():
			return False
	if text[2] != '-':
		return False
	for i in range(3,8):
		if not text[i].isdecimal():
			return False
	if text[8]!='-':
		return False
	for i in range(9,13):
		if not text[i].isdecimal():
			return False
	return True

message = 'Call me at 63-98485-7288 tomorrow. 63-98485-3410 is my office.'
for i in range(len(message)):
	chunk = message[i:i+13]
	if isPhoneNumber(chunk):
		print('Phone number found: '+ chunk)
print("Done")