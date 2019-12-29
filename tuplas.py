mitupla=("Juan", 13, 1, 1995)
miLista=list(mitupla) #convierte tupla en lista

miLista=["Juan", 13, 1, 1995,13]
mitupla = tuple(miLista) #convierte lista en tupla

print(mitupla.count(13)) #cuenta el número de veces que aparece el elemento

print(len(mitupla)) #el número de elementos de la tupla


mitupla=("Juan",) #tupla unitaria

mitupla = "Juan", 13, 1, 1995 #empaquetado de tupla

mitupla = ("Juan", 13, 1, 1995)
nombre, dia, mes , agno = mitupla #empaquetado de tuplas

print(nombre,dia,mes,agno)

print(len(mitupla))