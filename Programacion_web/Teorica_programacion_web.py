import requests

# pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')
# print(pedido) #si da una rta, el canal de comunicacion funciona
# print(pedido.json()) 
# se lo manipula como un diccionario de python. Me devuelve info del formato en el cual nos manda la info el cliente.
# aplicacion REST = Se correlacionan las urls con los verbos HTTPs. Esos verbos (en este caso get) son acciones que 
# los servidores entienden. la URL es informativa.
# devuelve: <Response [200]>
# {'id': 1, 'tipo': 'pantalon', 'talle': 35}
"""--> devuelve la prenda 1 por que puse en el URL /prendas/1"""

# pedido = requests.get('https://macowins-server.herokuapp.com/prendas')
# print(pedido) 
# print(pedido.json()) 
# si no le aclaro el numero me trae todas las prendas en una lista de diccionarios (todo lo que tiene en la base de datos)

# DESAFIO I - hace otro pedido para traer la prenda 20.
'''pedido = requests.get('https://macowins-server.herokuapp.com/prendas/20')
print(pedido.json()) '''
# devuelve: {'id': 20, 'tipo': 'saco', 'talle': 'XL'}

# Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
#pedido = requests.get('https://macowins-server.herokuapp.com/prendas/400')
#print(pedido) 
'''Devuelve <Response [404]>'''
#print(pedido.headers)
'''Devuelve {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '0', 'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"', 'Vary': 'Accept-Encoding', 'Date': 'Mon, 09 May 2022 14:43:33 GMT', 'Via': '1.1 vegur'}'''
#print(pedido.status_code)
'''Devuelve: 404'''
# pedido = requests.get('https://macowins-server.herokuapp.com/prendas') 
# print(len(pedido.json())) 
"""para saber el total de prendas"""
# imprime 20 --> hay 20 prendas en total, por eso, con 400 da error. 

# Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' 
# ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(pedido)
""""Devuelve """
print(pedido.headers)
""""Devuelve """
print(pedido.status_code)
""""Devuelve """

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo 
# https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
pedido = requests.get('https://macowins-server.herokuapp.com/prindas/1?')
print(pedido)
""""Devuelve """

# Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y 
# requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior
requests.get('https://macowins-server.herokuapp.com/ventas') 
requests.get('https://macowins-server.herokuapp.com/ventas/2')

# Desafío VI: Obtené las remeras.
requests.get('https://macowins-server.herokuapp.com/prendas/remeras')

# Desafío VII: Obtené las remeras XS
requests.get('https://macowins-server.herokuapp.com/prendas/remeras/XS')

# Desafío VIII: decí usando tus palabras qué significa la URI de este ejemplo cerebral 
""" """

# Desafío IX: ¿a través de qué IP accedés a google desde tu computadora?


# Desafío X: ¿Qué devolverá la página principal (home) de nuestro sitio? Averiguá el Content-Type de /home

# Desafío XI: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, si el contenido se 
# transfiere encriptado, y la fecha de expieración del contenido.

# Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo

# Desafío XIII: Nos quedaron prendas con ids que no nos sirven; ¡borralas!

# Desafío XIV: Creá una venta.

# Desafío XV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. 
# ¿Qué sucede?

# Desafío XVI: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
# Github, Youtube, Facebook, Infobae, Pagina12, La Nacion, UNQ, UCEMA

# Desafío XVII: si no se organizan de forma REST, ¿cómo se organizan sus rutas?

# Desafío XVIII: ¿En dónde está desplegado QMP? ¿Podés averiguarlo las cabeceras HTTP y/o la URL?