import requests

# pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')
# print(pedido) #si da una rta, el canal de comunicacion funciona
# print(pedido.json()) 
# se lo manipula como un diccionario de python. Me devuelve info del dormato en el cual nos manda la info el cliente.
# aplicacion REST = Se correlacionan las urls con los verbos HTTPs. Esos verbos (en este caso get) son acciones que los servidores entienden. la URL es informativa.
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
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(pedido) 
'''Devuelve <Response [404]>'''
print(pedido.headers)
'''Devuelve {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '0', 'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"', 'Vary': 'Accept-Encoding', 'Date': 'Mon, 09 May 2022 14:43:33 GMT', 'Via': '1.1 vegur'}'''
print(pedido.status_code)
'''Devuelve: 404'''
# pedido = requests.get('https://macowins-server.herokuapp.com/prendas') 
# print(len(pedido.json())) 
"""para saber el total de prendas"""
# imprime 20 --> hay 20 prendas en total, por eso, con 400 da error. 