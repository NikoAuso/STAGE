import re
import it_core_news_lg
from spacy.tokenizer import Tokenizer

# Esempio di utilizzo text = ("Nel cuore di Roma, troverai il nostro accogliente ristorante al numero 06 1234567.
# Prenota ora al nostro cellulare aziendale al +39 333 4567890 per assaporare le prelibatezze della cucina italiana.
# Per eventi speciali, chiamaci al fisso di Milano: 02.987.6543. Se preferisci WhatsApp, contattaci al +39
# 345.678.9012. La nostra sede principale è a Firenze, raggiungibile al telefono fisso 055 8765432. Organizziamo
# anche catering, chiama il nostro mobile: 347-1122334. Il nostro staff è sempre pronto ad assisterti,
# anche su Skype: username \"italianodelizie\". Per informazioni aggiuntive, visita il nostro sito web
# www.ristoranteitaliano.it o chiamaci al numero verde gratuito 800 123 456.") text = ("Nel cuore della vivace città
# di Milano, troverete una vasta gamma di attività e servizi. Se hai bisogno di prenotare una tavolo in un ristorante
# esclusivo, chiama il +39 02 1234567 e assicurati di provare il loro famoso piatto di pasta. Per uno shopping di
# lusso, contatta il negozio di moda al +39 02 987-6543 e scopri le ultime tendenze. Se sei interessato ad attività
# culturali, la Galleria d'Arte Moderna ha una fantastica mostra in corso. Per informazioni sui biglietti,
# chiama il numero verde gratuito 800-112233. Se sei un appassionato di arte contemporanea, non perdere l'occasione
# di visitare la galleria al +39 (02) 345.6789. Per gli amanti dello sport, la palestra del quartiere è il posto
# giusto per allenarsi. Contatta il +39 02 111-2222 per informazioni su corsi e abbonamenti. Se invece preferisci una
# partita di tennis, prenota un campo chiamando il +39 02 3334444. Per quanto riguarda la vita notturna,
# numerosi locali offrono intrattenimento di prima classe. Il Club Blu è rinomato per le sue feste esclusive. Prenota
# il tuo posto chiamando il +39 02 5555-6666. Se preferisci qualcosa di più tranquillo, il Jazz Lounge è perfetto.
# Chiama il +39 02 7777.8888 per prenotare un tavolo e goderti una serata di jazz dal vivo. Speriamo che tu possa
# vivere appieno la tua esperienza milanese! Se hai bisogno di ulteriori informazioni su eventi o servizi,
# contatta l'ufficio turistico al +39 02 999-0000.")

"""Nel cuore della vivace città di Milano, troverete una vasta gamma di attività e servizi. Se hai bisogno di 
prenotare una tavolo in un ristorante esclusivo, chiama il +39 02 1234567 e assicurati di provare il loro famoso 
piatto di pasta. Per uno shopping di lusso, contatta il negozio di moda al +39 02 987-6543 e scopri le ultime 
tendenze. Se sei interessato ad attività culturali, la Galleria d'Arte Moderna ha una fantastica mostra in corso. Per 
informazioni sui biglietti, chiama il numero verde gratuito 800-112233. Se sei un appassionato di arte contemporanea, 
non perdere l'occasione di visitare la galleria al +39 (02) 345.6789. Per gli amanti dello sport, la palestra del 
quartiere è il posto giusto per allenarsi. Contatta il +39 02 111-2222 per informazioni su corsi e abbonamenti. Se 
invece preferisci una partita di tennis, prenota un campo chiamando il +39 02 3334444. Per quanto riguarda la vita 
notturna, numerosi locali offrono intrattenimento di prima classe. Il Club Blu è rinomato per le sue feste esclusive. 
Prenota il tuo posto chiamando il +39 02 5555-6666. Se preferisci qualcosa di più tranquillo, il Jazz Lounge è 
perfetto. Chiama il +39 02 7777.8888 per prenotare un tavolo e goderti una serata di jazz dal vivo. Speriamo che tu 
possa vivere appieno la tua esperienza milanese! Se hai bisogno di ulteriori informazioni su eventi o servizi, 
contatta l'ufficio turistico al +39 02 999-0000."""

text = ("etfrgr00h19e388g hgfhgjg")

suffix_re = re.compile(r'\d+g$')


def custom_tokenizer(nlp):
    return Tokenizer(nlp.vocab, suffix_search=suffix_re.search)


nlp = it_core_news_lg.load()
nlp.tokenizer = custom_tokenizer(nlp)

print(nlp.tokenizer.explain(text))
