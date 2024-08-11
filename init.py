# Conjunto inicial de nombres
nombres = {
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
}

# Conjunto Nombres de magos y científicos
magos = {"Harry Houdini", "David Blaine", "Teller"}
cientificos = {"Newton", "Hawking", "Einstein"}

# Conjunto de nombres que no son magos ni científicos
otros = nombres - cientificos - magos


# Función para hacer a los magos grandiosos
def hacer_grandioso(lista_magos):
    return [f"El gran {mago}" for mago in lista_magos]

# Función para imprimir nombres de una lista o conjunto en  este caso
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Hacer a los magos grandiosos, modifica el conjunto de magos por grandiosos magos
magos = hacer_grandioso(magos)

# Imprimir los resultados
print("Lista original de nombres:")
imprimir_nombres(nombres)

print("\nMagos grandiosos:")
imprimir_nombres(magos)

print("\nCientíficos:")
imprimir_nombres(cientificos)

print("\nOtros:")
imprimir_nombres(otros)