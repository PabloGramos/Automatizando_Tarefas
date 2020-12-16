#! python3
# pw.py - Um programa para repositorios de senhas que não é seguro.
PASSWORDS={'email':'F7minBDDlokznlc56DFn','blog':'VmALjnksdjkfjbKJBkj78600','luggage':'12345'}

import sys
if len(sys.argv) < 2:
    print('Usage:python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]