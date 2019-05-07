#from oferta import Oferta
#oferta = Oferta()
#oferta.scrapping('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',1)
#oferta.scrapping('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',2)
#oferta.scrapping('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INRO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',3)
#oferta.scrapping('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',4)
#oferta.scrapping('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INBI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',5)
#oferta.scrapping('http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=IGFO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',6)

import requests
from bs4 import BeautifulSoup
import json
url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
#url='http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
#url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INRO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
#url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000 '
#url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INBI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
#url='http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=IGFO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
r = requests.get(url)
r.encoding = 'utf-8'
#print(r.text)
#html_doc = r.text
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
items = soup.find('table')
#print(items)
contenido = items.find_all('tr')
cont = contenido[2]
#print(cont)
datos = cont.find_all(class_='tddatos')

lista = [ ]
for c in contenido:
    "nrc" : datos[0].text,
    "clave" :datos[1].a.text,
    "materia" :datos[2].text,
    "seccion" :datos[3].text,
    "creditos" :datos[4].text,
    "cupos" : datos[5].text,
    "disponible" :datos[6].text,
    "hora": cont.find(align='center').find('table').find('tr').find_all('td')[1].text,
    "dias": cont.find(align='center').find('table').find('tr').find_all('td')[2].text,
    "edificio": cont.find(align='center').find('table').find('tr').find_all('td')[3].text,
    "aula" :cont.find(align='center').find('table').find('tr').find_all('td')[4].text,
    "periodo": cont.find(align='center').find('table').find('tr').find_all('td')[5].text,
    "profe": datos[7].find_all(class_='tdprofesor')[1].text



nrc=datos[0].text
clave=datos[1].a.text
materia=datos[2].text
seccion=datos[3].text
creditos=datos[4].text
cupos=datos[5].text
disponible=datos[6].text
hora=cont.find(align='center').find('table').find('tr').find_all('td')[1].text
dias=cont.find(align='center').find('table').find('tr').find_all('td')[2].text
edificio=cont.find(align='center').find('table').find('tr').find_all('td')[3].text
aula=cont.find(align='center').find('table').find('tr').find_all('td')[4].text
periodo=cont.find(align='center').find('table').find('tr').find_all('td')[5].text
profe=datos[7].find_all(class_='tdprofesor')[1].text
