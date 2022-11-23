from bs4 import BeautifulSoup

print('hola mundo')

with open('Clientes.xml','r') as f:
    data=f.read()
#print(data)

Bs_data=BeautifulSoup(data, 'xml')
#print(Bs_data)

telefonos=Bs_data.find_all('telefono')
print(telefonos)

b_name=Bs_data.find('cliente', {'ID':'C001'})
print(b_name)

for tag in Bs_data.find_all('child', {'name':'Frank'}):
    tag['ciudad'] = 'Madrid'

print(Bs_data.prettify())

