import urllib
import urllib.request

try:
    sit = 'http://www.pudim.com.br'
    site = urllib.request.urlopen(sit)
except:
    print('Não consegui acessar')
else:
    print('Consegui acessar o site')
    