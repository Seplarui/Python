miLista = ["María", "Pepe", "Marta", "Antonio"]
print(miLista) #Toda la lista
print(miLista[2]) #Posición 2

print(miLista[-1]) #Empieza a contar por el final

print(miLista[:3]) #Los tres primeros
print(miLista[2:]) #Los dos últimos

miLista.append("Sandra") #Añade un elemento al final

miLista.insert(2,"Sandra2") #Añade elemento en una posición concreta

miLista.extend(["Ana","Lucía"]) #Añade varios elementos a la lista

print("Pepe" in miLista) #Devuelve si existe el elemento

miLista.remove("María") #Elimina el elemento

miLista.pop() #Elimina el último elemento

miLista=["María", 5, True, 78.35]

miLista2 = ["Sandra", "Lucía"]

miLista3 = miLista + miLista2 #Sumar listas

miLista=["María", 5, True, 78.35] * 30 # Repite la lista 3 veces

#print(miLista.index("Antonio")) #Devuelve la posición, si se repite el elemento nos mostrará la posición del primer elemento

print(miLista)
