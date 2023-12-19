import webbrowser
import spacy
from spacy import displacy

nlp = spacy.load("it_ItLit800")


def display_result_displacy(doc):
    """colors = {"TEL": "FF00FF", "CEL": "#FFFF00"}
    options = {"ents": ["TEL", "CEL", "PER", "ORG", "MISC", "LOC"], "colors": colors}"""
    html = displacy.render(doc, style="ent", page=True)
    with open("../output.html", "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open("../output.html")


text = ("""Nel cuore della vivace città di Milano, troverete una vasta gamma di attività e servizi. Se hai bisogno di 
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
contatta l'ufficio turistico al +39 02 999-0000.""")

text = ("""Nel cuore della vivace città di Verona, Giulia passeggiava lungo le antiche strade lastricate di pietra. I 
suoi occhi scuri riflettevano la storia millenaria della città, mentre il vento leggero scompigliava i suoi lunghi 
capelli castani. Giulia era una giovane scrittrice appassionata, sempre in cerca di ispirazione tra le mura ricche di 
cultura e di storie da raccontare. Incontrò Marco, un musicista di strada con una chitarra consumata che emanava 
melodie avvolgenti. I loro destini si intrecciarono quando Marco decise di accompagnarla nel suo viaggio attraverso 
le strade della creatività. Insieme, crearono un connubio unico di parole e note che catturarono l'essenza della 
città e dei suoi abitanti. Attraversando Piazza delle Erbe, s'imbatterono in una pittoresca bancarella gestita da un 
anziano signore di nome Enzo. Enzo, un appassionato collezionista di libri antichi, aveva una vasta conoscenza della 
storia locale. Condivideva racconti affascinanti di personaggi leggendari che avevano segnato il passato di Verona. 
Il trio, condividendo le proprie esperienze e passioni, divenne una strana ma affiatata famiglia. Le serate 
trascorrevano in conversazioni profonde e improvvisazioni musicali sotto le stelle. Giulia, Marco e Enzo si trovavano 
immersi in un mondo creativo che sembrava fluttuare al di sopra delle restrizioni del tempo. La loro avventura non 
solo li arricchì culturalmente ma li fece anche crescere come individui. Attraverso le pagine dei libri, 
le corde della chitarra e le strade di Verona, impararono che l'arte e la creatività potevano unire le persone in 
modi sorprendenti. E così, continuando il loro cammino insieme, lasciarono un'impronta indelebile nella trama della 
città e nei cuori di coloro che avevano il privilegio di incrociare il loro percorso.""")

doc = nlp(text)

for ent in doc.ents:
    print("Entity:", ent.text, "Label:", ent.label_)

display_result_displacy(doc)
