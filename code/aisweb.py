import sys
from requests_html import HTMLSession
import requests


if len(sys.argv) < 2:
    print('É necessário fornece o código ICAO')
    exit()

codigo_icao = sys.argv[1]
if len(codigo_icao) < 4:
    print('O código deve ter ao menos 4 caracteres')
    exit()

session = HTMLSession()
url = 'https://aisweb.decea.mil.br/?i=aerodromos&codigo='


r = session.get(url+codigo_icao)

print('')
sunrise = r.html.find('sunrise', first=True)
if sunrise == None:
    print('Não foram encontradas informações para este código')
    exit()

print('Nascer do sol: ',sunrise.text)

sunset = r.html.find('sunset', first=True)
print('Por do sol: ', sunset.text)
print('')

div_redemet = r.html.find('div.order-sm-12', first=True)
p_redemet = div_redemet.find('p')

print('METAR')
print(p_redemet[2].text.rstrip('='))
print('')

print('TAF')
print(p_redemet[3].text.rstrip('='))
print('')

cartas = div_redemet.find('a')
links_cartas = div_redemet.absolute_links

print('Fazendo download das cartas')
numero_cartas = 0
for carta in cartas:
    carta_url = carta.xpath('a/@href')[0]
    if 'aisweb.decea.gov.br/download' in carta_url:
        print(carta.text)
        name_file = carta.text.replace(' ', '-').replace('/', '-') + ".pdf"
        file = requests.get(carta_url, allow_redirects=True)
        pdf = open(name_file, "wb")
        pdf.write(file.content)
        pdf.close()
        numero_cartas += 1
print(f'O dowload de {numero_cartas} cartas foi concluido')
print('')


# import requests as req

# URL = "https://www.facebook.com/favicon.ico"
# file = req.get(url, allow_redirects=True)

# open("facebook.ico", "wb").write(file.content)



# <hr id="met" class="mt-0">
# <p class="text-center mt-0"><img class="img-fluid" src="https://aisweb.decea.mil.br/assets/templates/portal/img/logos/bt_redemet.png" alt=""></p>
# <h5 class="mb-0 heading-primary">METAR</h5>
# <p>111400Z 02005KT CAVOK 28/18 Q1016=</p>
