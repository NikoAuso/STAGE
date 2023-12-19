import numpy as np
import random

###########################
# GENERO STRINGHE CASUALI #
###########################
# LENGTH = 4
# NO_CODES = 100000
# alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
# np_codes = np.random.choice(alphabet, size=[NO_CODES, LENGTH])
# codes = [''.join(code) for code in np_codes]
###########################


################################
# GENERO ARRAY DI NOMI CASUALI #
################################
with open('nomi_italiani.txt') as file:
    nomi = [line.rstrip() for line in file]

lunghezza_array = 20
numero_array = 50

risultato = []

for _ in range(numero_array):
    array_casuale = random.sample(nomi, lunghezza_array)
    risultato.append(array_casuale)
################################


############################################################################
# CREO IL DIZIONATIO CON GLI ELEMENTI UNICI DELL'ARRAY E LA LORO FREQUENZA #
############################################################################
res = np.unique(risultato, return_counts=True)
print(sorted(dict(zip(res[0], res[1])).items(), key=lambda item: item[1], reverse=True))
