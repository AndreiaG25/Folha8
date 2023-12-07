
def artigos(texto):
    artigos_count = 0

    with open(texto, 'r', encoding='utf-8') as file:
        content = file.read()
        artigos = content.split("<pub>")

        if artigos[0] == '':
            artigos_count = len(artigos) - 1
        else:
            artigos_count = len(artigos)

    return artigos_count

texto = "folha8.OUT.txt"

num_artigos = artigos(texto)

print(f"Existem {num_artigos} no texto.")
