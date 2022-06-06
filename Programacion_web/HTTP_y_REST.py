import requests, json

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
# pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')
# print(pedido)
""""Devuelve <Response [200]>"""
# print(pedido.headers)
""""Devuelve {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 'Date': 'Fri, 27 May 2022 17:52:24 GMT', 'Via': '1.1 vegur'}"""
# print(pedido.status_code)
""""Devuelve 200"""

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo 
# https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
# pedido = requests.get('https://macowins-server.herokuapp.com/prindas/1?')
# print(pedido)
""""Devuelve <Response [404]>"""

# Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y 
# requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior
# print((requests.get('https://macowins-server.herokuapp.com/prendas')).json())
# print((requests.get('https://macowins-server.herokuapp.com/prendas/1')).json())
# print((requests.get('https://macowins-server.herokuapp.com/ventas')).json())
# print((requests.get('https://macowins-server.herokuapp.com/ventas/2')).json())
"""En los casos donde no se aclara el numero devuelve todos los pedidos o todas las ventas (según se le pida), mientras
que si se aclara el numero de pedido o venta, devuelve unicamente los datos correspondientes a dicho pedido o venta"""

# Desafío VI: Obtené las remeras.
# pedido = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera').json()
# print(pedido)

# Desafío VII: Obtené las remeras XS
# pedido = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS').json()
# print(pedido)

# Desafío VIII: decí usando tus palabras qué significa la URI de este ejemplo cerebral: cerebro://recuerdos:3403/recientes#hoy?tema=http
""" En este caso se está pidiendo al cerebro que busque un recuerdo de hoy sobre http"""

# Desafío IX: ¿a través de qué IP accedés a google desde tu computadora?
""" Google Public DNS IPv4: 8.8.8.8. 8.8.4.4. """

# Desafío X: ¿Qué devolverá la página principal (home) de nuestro sitio? Averiguá el Content-Type de /home
# home = requests.get('https://macowins-server.herokuapp.com/home')
# print(home.headers)
""" 'Content-Type': 'text/html; charset=utf-8' """

# Desafío XI: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, si el contenido se 
# transfiere encriptado, y la fecha de expieración del contenido.
# meli = requests.get('https://www.mercadolibre.com.ar/')
# print(meli.headers)
""" 'Server': 'Tengine' | 'content-encoding': 'gzip' | Expires=Sat, 27 May 2023 23:57:23 GMT, _csrf=t71GpsZRZBcugGf6zqwElzyA"""

# bcra = requests.get('http://www.bcra.gov.ar/')
# print(bcra.headers)
""" 'Expires': 'Fri, 27 May 2022 23:59:54 GMT' , no aclara nada sobre el contenido y el servidor"""

# youtube = requests.get('https://www.youtube.com/')
# print(youtube.headers)
""" 'Expires': 'Mon, 01 Jan 1990 00:00:00 GMT' | 'Content-Encoding': 'gzip' | 'Server': 'ESF' """

# github = requests.get('https://github.com/')
# print(github.headers)
""" 'Server': 'GitHub.com' | 'Content-Encoding': 'gzip' | Expires=Sun, 28 May 2023 00:05:46 GMT """

# Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo
# data = {'id': 21}
# r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
# print(r.status_code)
""" Devuelve 201 """

# Desafío XIII: Nos quedaron prendas con ids que no nos sirven; ¡borralas!
# requests.delete('https://macowins-server.herokuapp.com/?id=21')
# print(requests.get('https://macowins-server.herokuapp.com/prendas').json())
"""chequear"""

# Desafío XIV: Creá una venta.
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# data =  { "tipo": "pantalon", "talle": "42" }
# r = requests.post('https://macowins-server.herokuapp.com/ventas', data=json.dumps(data), headers=headers)
# print(r.status_code)

# Desafío XV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. 
# ¿Qué sucede?
# r = requests.post('https://macowins-server.herokuapp.com/prendas/1')
# print(r.status_code)
""" Devuelve 404, es decir, error """

# Desafío XVI: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
# Github: si
# Youtube: si
# Facebook: si
# Infobae: si
# Pagina12: si
# La Nacion: si
# UNQ: si
# UCEMA: si

# Desafío XVII: si no se organizan de forma REST, ¿cómo se organizan sus rutas?
""" preguntar """

# Desafío XVIII: ¿En dónde está desplegado QMP? ¿Podés averiguarlo las cabeceras HTTP y/o la URL?
