""""""
"""commentez simplement ce programme. utilisez internet pour tous les mots clefs nouveaux qui apparaissent"""

file_name = 'moliere.txt'

with open(file_name,'r') as f:
    raw_data = f.read()
    #print("Data length:", len(raw_data))

# On crée l'ensemble contenant le vocabulaire
vocab = set()
# On décide, pour simplifier le preprocessing, qu'un espace sépare deux mots
words = str.split(raw_data, sep=' ')
for s in words:
    vocab.add(s)
print('Nombre de mots dans les données :', len(words))
vocab_size = len(vocab)
print('Taille du vocabulaire :', vocab_size)

#On place le vocabulaire dans un dictionnaire
idx_to_vocab = dict(enumerate(vocab))
vocab_to_idx = dict(zip(idx_to_vocab.values(), idx_to_vocab.keys()))

#On transforme ce dictionnaire pour que chaque mot du vocabulaire pointe sur un index
data = [vocab_to_idx[c] for c in words]
del raw_data

liste=[]
for i in idx_to_vocab:
    print(i,idx_to_vocab[i])
    liste.append(idx_to_vocab[i])
    if i>10: break

for word in liste:
    print(word,vocab_to_idx[word])


