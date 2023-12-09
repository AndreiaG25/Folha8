import re

def comprimentoMedio(txt):
    palavras = re.findall(r'\w+', txt)
    pontuacao = re.findall(r'\.\.\.|[!?]+|[.]', txt)
    total = len(pontuacao)
    
    if total > 0:
        compMedio = len(palavras) / total
    else:
        compMedio = 0
    
    return compMedio

Nome = "folha8.OUT.txt"
txt = open(Nome, encoding="utf-8").read()

compMedio = comprimentoMedio(txt)
print(f"O comprimento médio das frases em palavras é: {compMedio}")
