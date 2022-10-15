from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from optparse import OptionParser
import json
from scipy import spatial
import numpy as np
import gensim
from gensim.models import Word2Vec
import time
import matplotlib.pyplot as plt
import csv
import nltk
from nltk.cluster import KMeansClusterer
from nltk.cluster import euclidean_distance
from nltk import cluster
from numpy import array
sentence_vectors_unprocessed = []

#loop opens csv and converts it into list of sentacne vectors in format[[list of some numbers that represent the sentances],[],...,[]]
with open('vectors_save.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        temp2 = []
        temp = str(row)
        temp = temp.replace("['", '')
        temp = temp.replace("']", '')
        
        #print(temp)
        temp = (temp.split(','))

        for x in temp:
            #print(x)
            try:
                temp2.append(float(x))
            except:
                #print("empty value occured")
                #do anything
                waster = 1
        #print(temp2[1])


        sentence_vectors_unprocessed.append(temp2)

sentence_vectors_processed = []
#for each entry in list of sentances sort the vectors
for unsorted in sentence_vectors_unprocessed:
    if unsorted:#check if there is an element in the list portion
        #sort each sentance vectors
        #print(unsorted[0])
        sortedsentance = unsorted
        sortedsentance.sort()
        #print(sortedsentance[0])
        #now that the list is sorted split the list in half
        #bottom 50%
        bot50 = sortedsentance[:len(sortedsentance)//2]
        #top 50%
        top50 = sortedsentance[len(sortedsentance)//2:]
        #get avg bottom 50
        bot50avg = sum(bot50) / len(bot50)
        #get avg top 50
        top50avg = sum(top50) / len(top50)
        #turn into 2d vector
        temp3 = [bot50avg,top50avg]
        #append to processed list
        sentence_vectors_processed.append(temp3)




print("processed: ")
print(len(sentence_vectors_processed))#use this to make sure there are the right number of sentaces (there should be 2001 and for the current project)
#for sentence in sentences:
 #   X.append(sent_vectorizer(sentence, vectors))   
 
#print ("========================")
#print (X)
 
 
  
 
# note with some version you would need use this (without wv) 
#  model[model.vocab] 
#print (model[model.wv.key_to_index ])
 
 
  
 
#print (model.wv.similarity('post', 'book'))
#print (model.wv.most_similar(positive=['machine'], negative=[], topn=2))
  
  
batch_size = 45
test = sentence_vectors_processed
centers =  [array(f) for f in sentence_vectors_processed]
NUM_CLUSTERS=2
print(nltk.cluster.util.cosine_distance)
assigned_clusters = cluster.KMeansClusterer(2, euclidean_distance)
assigned_clusters.cluster(centers, True)
print (assigned_clusters)

  
reviews = open("reviews.txt", "r", encoding="utf-8")
sentences = reviews.readlines()

#for index, sentence in enumerate(sentences):    
  #  print (str(assigned_clusters[index]) + ":" + str(sentence))
 
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7)

import time
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0

from sklearn.cluster import MiniBatchKMeans
n_clusters = len(centers)
mbk = MiniBatchKMeans(
    init="k-means++",
    n_clusters=3,
    batch_size=batch_size,
    n_init=10,
    max_no_improvement=10,
    verbose=0,
)
t0 = time.time()
mbk.fit(X)
t_mini_batch = time.time() - t0

from sklearn.metrics.pairwise import pairwise_distances_argmin

k_means_cluster_centers = k_means.cluster_centers_
order = pairwise_distances_argmin(k_means.cluster_centers_, mbk.cluster_centers_)
mbk_means_cluster_centers = mbk.cluster_centers_[order]

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
     
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 3))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
colors = ["#4EACC5", "#FF9C34", "#4E9A06"]

# KMeans
ax = fig.add_subplot(1, 3, 1)
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    ax.plot(X[my_members, 0], X[my_members, 1], "w", markerfacecolor=col, marker=".")
    ax.plot(
        cluster_center[0],
        cluster_center[1],
        "o",
        markerfacecolor=col,
        markeredgecolor="k",
        markersize=6,
    )
ax.set_title("KMeans")
ax.set_xticks(())
ax.set_yticks(())
plt.text(-3.5, 1.8, "train time: %.2fs\ninertia: %f" % (t_batch, k_means.inertia_))

# MiniBatchKMeans
ax = fig.add_subplot(1, 3, 2)
for k, col in zip(range(n_clusters), colors):
    my_members = mbk_means_labels == k
    cluster_center = mbk_means_cluster_centers[k]
    ax.plot(X[my_members, 0], X[my_members, 1], "w", markerfacecolor=col, marker=".")
    ax.plot(
        cluster_center[0],
        cluster_center[1],
        "o",
        markerfacecolor=col,
        markeredgecolor="k",
        markersize=6,
    )
ax.set_title("MiniBatchKMeans")
ax.set_xticks(())
ax.set_yticks(())
plt.text(-3.5, 1.8, "train time: %.2fs\ninertia: %f" % (t_mini_batch, mbk.inertia_))

# Initialize the different array to all False
different = mbk_means_labels == 4
ax = fig.add_subplot(1, 3, 3)

for k in range(n_clusters):
    different += (k_means_labels == k) != (mbk_means_labels == k)

identic = np.logical_not(different)
ax.plot(X[identic, 0], X[identic, 1], "w", markerfacecolor="#bbbbbb", marker=".")
ax.plot(X[different, 0], X[different, 1], "w", markerfacecolor="m", marker=".")
ax.set_title("Difference")
ax.set_xticks(())
ax.set_yticks(())

plt.show()