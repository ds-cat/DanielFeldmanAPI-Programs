from gensim.test.utils import common_texts
from gensim.models import Word2Vec
# Sentences for which you want to create embeddings,
# passed as an array in embed()
inputFile = open("reviews.txt", mode="r", encoding="utf-8")
Sentences = []
for line in inputFile:
    lineStrip = line.strip()
    line_list = lineStrip.split()
    Sentences.append(line_list)
inputFile.close()
#print(Sentences)
embeddings = Word2Vec(Sentences)
  
# Printing embeddings of each sentence
print(embeddings)
  
# To print each embeddings along with its corresponding 
# sentence below code can be used.
#for i in range(len(Sentences)):
  #  print(Sentences[i])
  #  print(embeddings[i]