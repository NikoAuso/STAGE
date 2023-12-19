import itertools
import webbrowser

import numpy as np
import spacy
import time

from spacy import displacy

from CleantextExtractor.CleanTextExtractor import CleanTextExtractor
from urls_data import non_legal_urls, legal_urls

non_legal_pos = []
legal_pos = []

nlp = spacy.load('it_core_news_lg')
extractor = CleanTextExtractor(chrome=True)


def display_result_displacy(doc):
    html = displacy.render(doc, style="ent", page=True)
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open("output.html")


# total_time = 0
# # Non legal document
# for url in non_legal_urls:
#     start_time = time.time()
#     text = extractor.getPageChrome(url)
#     end_time = time.time()
#     total_time += end_time - start_time
#     doc = nlp(text)

#     for token in doc:
#         if token.pos_ not in ['SPACE', 'X', 'SYM', 'INTJ', 'PUNCT']:
#             non_legal_pos.append([token.orth_, token.pos_])
# non_legal_pos.sort(key=lambda x: x[1])

# # Divido gli array in base al POS TAG
# merged_result = []
# res = []
# for key, group in itertools.groupby(non_legal_pos, key=lambda x: x[1]):
#     merged_result.append([key, [sublist[0] for sublist in list(group)]])
#     # Raggruppo gli elementi degli array e restituisco l'array senza doppioni e la frequenza di ogni elemento
#     merged_result = np.unique(merged_result, return_counts=True)
#     res.append([key, sorted(dict(zip(merged_result[0], merged_result[1])).items(), key=lambda item: item[1], reverse=True)])
# print(res)

# # Legal document
# for url in legal_urls:
#     start_time = time.time()
#     text = extractor.getPageChrome(url)
#     end_time = time.time()
#     total_time += end_time - start_time
#     doc = nlp(text)
#     for token in doc:
#         if token.pos_ not in ['SPACE', 'X', 'SYM', 'INTJ', 'PUNCT']:
#             legal_pos.append([token.orth_, token.pos_])
# legal_pos.sort(key=lambda x: x[1])

#
# # Divido gli array in base al POS TAG
# res_legal = []
# for key, group in itertools.groupby(legal_pos, key=lambda x: x[1]):
#     res_legal.append([key, [sublist[0] for sublist in list(group)]])
#     # Raggruppo gli elementi degli array e restituisco l'array senza doppioni e la frequenza di ogni elemento
#     # merged_result = np.unique(merged_result, return_counts=True)
#     # res.append([key, sorted(dict(zip(merged_result[0], merged_result[1])).items(), key=lambda item: item[1], reverse=True)])
#
# for key, item in res_non_legal:
#     print(key, len(item))
#
# for key, item in res_legal:
#     print(key, len(item))
