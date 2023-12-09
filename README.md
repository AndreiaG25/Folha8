# Folha8
News_articles.py: Conta o número de publicações, tendo como referência a tag <pub>.

News_articles_DATE.py: Conta o número de publicações, tendo como referência a tag <DATE>. O resultado deste código dá um número inferior de publicações ao anterior, o que me levou à conclusão que, possivelmente, nem todas as publicações têm datas.

News_Tags.py: Extrai e ordena por ordem decrescente de ocorrências todas as tags apresentadas, usando expressões regulares que correspondam ao formato "tag:{algum_texto_aqui}"fazendo a extração de todas as "tag:{}" que aparecem no documento.

Tags.txt: Resultado do código dado por "News_Tags.py".

Datas.py: Cria uma lista das datas de todas as publicações, fazendo também uso de expressões regulares, começando com #DATE, seguido por uma sequência de caracteres até encontrar uma data no formato "dia de mês de ano". O código está escrito de forma a extrair apenas a 1ª data que aparece após #DATE, de modo a evitar contar todas as datas que puderão aparecer no documento.

Datas.txt: Resultado do código dado por "Datas.py".

Datas_sorted.py: Junta e ordena as ocorrências das datas anteriores.

Datas_sorted.txt: Resultado do código dado por "Datas_sorted.py".

Comp_medio_frases.py: Este é o exercício livre, onde é calculado o comprimento médio das frases. 
