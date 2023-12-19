from goose3 import Goose

url = ("https://www.corriere.it/esteri/23_novembre_07/netanyahu-israele-sicurezza-gaza-29e1453a-7d53-11ee-8bbd-2076da079d53.shtml")
url_wikipedia = "https://it.wikipedia.org"
url_vogue = ("https://www.corriere.it/esteri/23_novembre_07/netanyahu-israele-sicurezza-gaza-29e1453a-7d53-11ee-8bbd"
             "-2076da079d53.shtml")

config = {
    'strict': False,
    'browser_user_agent': 'Mozilla 5.0',
    'parser_class': 'soup'
}

with Goose(config) as g:
    article = g.extract(url=url_wikipedia)
    print(article.cleaned_text)
    g.close()
