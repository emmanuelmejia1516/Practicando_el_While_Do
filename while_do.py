print("Mejia Suarez Emmanuel Alexander:programa para practicar while_do")
# Mostrar números del 1 al 5
i = 1
print("Números del 1 al 5:")
while i < 6:
    print(i)
    i += 1

# Salir cuando i es igual a 3
print("\nSalir cuando i es igual a 3:")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continuar una vez que i es igual a 3
print("\nContinuar cuando i es igual a 3:")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Mensaje desplegado cuando sea falso
print("\nMensaje cuando i ya no es menor que 6:")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i ya no es menor que 6")
