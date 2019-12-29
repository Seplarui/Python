midiccionario={"Alemania":"Berlín","Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

midiccionario["Italia"]="Lisboa" #añadir clave -valor

midiccionario["Italia"]="Roma" #corregir valor

del midiccionario["Reino Unido"] #eliminar clave-valor

print(midiccionario)


mitupla=["España","Francia","Reino Unido","Alemania"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(midiccionario)

midiccionario={23:"Jordan","Nombre":"Michael", "Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1994,1995,1996,1997,1998]}}
print(midiccionario.keys()) #muestra todas las claves del diccionarios
print(midiccionario.values()) #muestra los valores del diccionario
print(len(midiccionario)) #tamaño del diccionario
print(midiccionario["anillos"])