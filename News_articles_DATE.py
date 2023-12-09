
def artigos(file_path):
    artigos_count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        artigos = content.split("#DATE")

        if artigos[0] == '':
            artigos_count = len(artigos) - 1
        else:
            artigos_count = len(artigos)

    return artigos_count

texto = "folha8.OUT.txt"
num_artigos = artigos(texto)

print(f"Existem {num_artigos} no texto.")