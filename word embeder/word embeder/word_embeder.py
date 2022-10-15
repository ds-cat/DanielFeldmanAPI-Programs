from gensim.models import Word2Vec

import nltk
from nltk.cluster import KMeansClusterer

import numpy as np 
import csv

from sent2vec.vectorizer import Vectorizer
  
from sklearn import cluster
from sklearn import metrics
  
# Sentences for which you want to create embeddings,
# passed as an array in embed()
inputFile = open("reviews.txt", mode="r", encoding="utf-8")
sentences = []
for line in inputFile:
    
    sentences.append(line[:512])#sentance 2 vec can only handle sentance of 512 characters or less


inputFile.close()
saved = True

#WARNING THIS WILL TAKE A LONG TIME 
vecMod = (sentences)
vectorizer = Vectorizer()
vectorizer.run(sentences)
vectors = vectorizer.vectors
#print(vectors)

#save voctorized sentacnes as cvs
with open('vectors_save', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(vectors)

    #TODO: turn vectored sentaces into X,Y vectors

    
