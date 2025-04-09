# ejemplo de una función
def saludar(nombre):
    print(f'Hola {nombre}')
    
saludar("Ricardo")
saludar("Pedro")
saludar("Maria")
saludar("Teresa")
    
# Documentar funciones con el docstring
def restar(a, b):
    '''Resta dos números y devuelve el resultado'''
    return a -b

print(restar.__doc__) # Así también se accede al docsctring desde la consola. 
# help(restar)

# Argumentos por clave
def describir_personas(nombre, edad, sexo):
    print(f'Soy {nombre}, tengo {edad} años y mi sexo es: {sexo}')
describir_personas("Alberto", 47, "masculino")

