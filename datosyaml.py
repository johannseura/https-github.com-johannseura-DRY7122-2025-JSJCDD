import yaml

with open("eva1.yaml", "r") as archivo:
    archivo_yaml = archivo.read()
    parseoyaml = yaml.safe_load(archivo_yaml)

print("ID Usuario:", parseoyaml["id_usuario"])
print("Token de seguridad:", parseoyaml["token_seguridad"])
print("Fecha de creación:", parseoyaml["fecha_creacion"])
print("Estado:", parseoyaml["estado"])
