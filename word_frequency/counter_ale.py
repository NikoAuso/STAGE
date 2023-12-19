import requests
import spacy
from datasets import load_dataset
from collections import Counter
from cleaner import extract_meaningfull_text
import urls_data
import time

start_time = time.time()

nlp = spacy.load("it_core_news_lg")

validation_dataset = load_dataset("itacasehold/itacasehold", split='validation')
legal_docs = validation_dataset["doc"]

non_legal_docs = []
for doc in legal_docs:
    doc = extract_meaningfull_text(doc)

for url in urls_data.legal_urls:
    s = requests.get(url)
    legal_docs.append(extract_meaningfull_text(s.text))

for url in urls_data.non_legal_urls:
    s = requests.get(url)
    non_legal_docs.append(extract_meaningfull_text(s.text))

c, c1 = Counter(), Counter()
n_words_in_doc, n_words_in_doc1 = 0, 0

for doc in legal_docs:
    for token in nlp(doc):
        if token.pos_ not in ['SPACE', 'X', 'SYM', 'INTJ']:
            c += Counter([token.pos_])
            n_words_in_doc += 1

for doc1 in non_legal_docs:
    for token in nlp(doc1):
        if token.pos_ not in ['SPACE', 'X', 'SYM', 'INTJ']:
            c1 += Counter([token.pos_])
            n_words_in_doc1 += 1

print(f"Sono stati analizzati {len(legal_docs)} documenti legali e {len(non_legal_docs)} documenti non legali. \n")
print("Rapporto tra i documenti legali e non legali per ogni token in base al POS :")
for pos, count in sorted(c.items()):
    print(f" {pos} : {(count / n_words_in_doc) / ((c1[pos]) / n_words_in_doc1)}")

end_time = time.time()
print(end_time - start_time)