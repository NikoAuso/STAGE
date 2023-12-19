import random
import itertools

import numpy as np

############# CREO ARRAY CASUALI #########################################################
elements = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
ranks = [1, 2, 3]

array_final = []
array_casuale = []

for _ in range(20):
    array_length = random.randrange(1, 10)
    for _ in range(array_length):
        array_casuale = [random.sample(elements, array_length), random.choice(ranks)]
    array_final.append(array_casuale)
##########################################################################################

# Ordino gli array in base al ranking
array_final.sort(key=lambda x: x[1])
res = []

# Divido gli array in base al ranking
for key, group in itertools.groupby(array_final, key=lambda x: x[1]):
    merged_result = [sublist[0] for sublist in list(group)]
    # Raggruppo gli elementi degli array e restituisco l'array senza doppioni e la frequenza di ogni elemento
    merged_result = np.unique(np.concatenate(merged_result), return_counts=True)
    res.append([key, sorted(dict(zip(merged_result[0], merged_result[1])).items(), key=lambda item: item[1], reverse=True)])

for item in res:
    print(item)
