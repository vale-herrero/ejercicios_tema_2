
from pickle import TRUE


def modificar(lista):

    print("lista sin duplicados:")
    lista_sin_duplicados= list(dict.fromkeys(lista))
    print(lista_sin_duplicados)

    print("lista ordenada:")
    lista_ordenada = sorted(lista_sin_duplicados, reverse= True)
    print(lista_ordenada)

    print("lista sin impares:")
    lista_sin_impares=[]
    for numero in lista_ordenada:
        if numero%2==0:
            lista_sin_impares.append(numero)
    print(lista_sin_impares)

    print("suma lista:")
    suma_lista=sum(lista_sin_impares)
    print(suma_lista)

    print("agrego suma a lista:")
    lista_sin_impares.insert(0,suma_lista)
    print(lista_sin_impares)
    return lista_sin_impares



lista_original=[2, 3, 4, 5, 3, 1, 2]
nueva_lista = modificar(lista_original)
print(nueva_lista[0] == sum(nueva_lista[1:]))
print(lista_original)
