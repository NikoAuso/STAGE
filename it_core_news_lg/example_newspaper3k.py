from newspaper import Article

url = "https://it.wikipedia.org"
url_vogue = ("https://www.corriere.it/esteri/23_novembre_07/netanyahu-israele-sicurezza-gaza-29e1453a-7d53-11ee-8bbd-2076da079d53.shtml")

# Crea un oggetto Article e scarica il contenuto della pagina
article = Article(url_vogue)
article.download()

# Esegui l'analisi per estrarre il testo e altre informazioni
article.parse()

# Estrai il titolo dell'articolo
titolo = article.title
print("Titolo:", titolo)

# Estrai il testo principale dell'articolo
testo = article.text
print("Testo principale:")
print(testo)