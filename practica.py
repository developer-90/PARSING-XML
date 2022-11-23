# muestra la descripcion de todos los productos por consola. Noa de uno sólo
# archivo xml de referencia en el siguiente enlace
# https://gist.github.com/Fhernd/6f2aa7527a682f76c165b91fe0e989ee

from bs4 import BeautifulSoup

# Al cafe negro le añadimos el precio 9.95

with open('catalogoProductos.xml','r') as f:
    data=f.read()
#print(data)

Bs_data=BeautifulSoup(data, 'xml')
#print(Bs_data)

descripcion=Bs_data.find_all('Descripcion')
print(descripcion)

for tag in Bs_data.find_all('Producto', {'ID':'100001'}):
    tag['precio'] = '9.95'

print(Bs_data.prettify())