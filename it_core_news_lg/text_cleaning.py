from bs4 import BeautifulSoup


def replace_newline_with_dot(text):
    soup = BeautifulSoup(text, 'html.parser')

    # Trova tutti i tag <p> nel documento
    p_tags = soup.find_all('p')

    # Itera su tutti i tag <p> e sostituisci il carattere di nuova linea con un punto
    for p_tag in p_tags:
        p_tag.replace_with(p_tag.text.replace('\n', ' '))

    # Restituisci il testo modificato
    return str(soup)


html_content = """
<p>Con <a href="https://it.wikipedia.org/wiki/Elaborazione_del_linguaggio_naturale"><strong>Natural Language Processing</strong></a> 
si fa riferimento a quel campo di ricerca interdisciplinare che abbraccia informatica, intelligenza artificiale e linguistica,
il cui scopo è quello di sviluppare algoritmi in grado di analizzare, rappresentare e quindi “comprendere”
il linguaggio naturale, scritto o parlato, in maniera similare o addirittura più performante rispetto agli esseri umani.</p>

<p>Questo è un altro paragrafo con "a capo". Una seconda frase.</p>
"""

modified_text = replace_newline_with_dot(html_content)

# Stampare il risultato
print(modified_text)
