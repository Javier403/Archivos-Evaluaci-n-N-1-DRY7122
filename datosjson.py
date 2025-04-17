import json
from datetime import datetime

# Abrir archivo
with open("myfile.json", "r") as json_file:
    ourjson = json.load(json_file)

# Obtener la lista de tokens
tokens = ourjson.get("tokens")

# Tomar el primer token de la lista (puedes cambiar el índice)
primer_token = tokens[0]

# Obtener el valor del token y su tiempo de expiración
token = primer_token.get("token")
tiempo_expira = primer_token.get("expiry_time")

# Convertir string a datetime
expirar = datetime.fromisoformat(tiempo_expira)

# Obtener hora actual
ahora = datetime.now()

# Calcular tiempo restante
tiempo_restante = expirar - ahora

# Imprimir resultados
print("Token:", token)
print("Expira en:", tiempo_restante)

