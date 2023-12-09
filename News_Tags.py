import re

def tagsOco(texto):
    with open(texto, 'r', encoding='utf-8') as file:
        noticias = file.read()
    tagOco = re.findall(r'tag:{([^}]+)}', noticias)
    contador = {}
    for tag in tagOco:
        if tag in contador:
            contador[tag] += 1
        else:
            contador[tag] = 1

    sorted_ocurrences = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    output_file_path = "Tags.txt"
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for tag, count in sorted_ocurrences:
            output_file.write(f"{tag}: {count} ocorrências\n")
    return output_file_path

texto = "folha8.OUT.txt"
output_file = tagsOco(texto)
print(f"Tags extraídas e salvas em {output_file}")