acl = input("Ingrese el número de ACL IPv4: ")

if acl.isdigit():
    acl = int(acl)
    if acl >= 1 and acl <= 99:
        print("Es una ACL Estándar")
    elif acl >= 100 and acl <= 199:
        print("Es una ACL Extendida")
    else:
        print("El número que insertó no corresponde al rango de ACL permitidas.")
else:
    print("Por favor, ingrese un número válido.")
