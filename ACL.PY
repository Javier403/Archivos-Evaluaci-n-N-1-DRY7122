acl_numero = int(input("Ingrese el numero de ACL IPV4: "))

if 1 <=acl_numero <= 99 or 1300 <= acl_numero <= 1999:
    print("ACL Estandar")
elif 100 <= acl_numero <= 199 or 2000 <= acl_numero <= 2699:
    print("ACL Extendida")
else:
    print("No corresponde a una ACL")