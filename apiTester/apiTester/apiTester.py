#take number of samples from user
sample_size = input("Enter sample size:" )
#3	35	67	99	131	163	195	227	259	291	323	355

largest = 0
cluster_sizes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cluster_propotion = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp = 0
i = 0
n = 0
templist = []
list_of_ids = []
#take input csv
from ast import Str
import csv
from pickle import APPEND
import random as rand
import math
from sqlite3 import apilevel
z = 0
y= 0
averageOver = 0
averageOver2 = 0
averageOver3 = 0
averageOverSRS = 0
averageOverSRS2 = 0
averageOverSRS3 = 0

run_size = 500
k = '-6'
inputfilename = 'clustered_sentances' + k +'.csv'
#
while z< run_size:
    
    with open(inputfilename,encoding='utf-8') as csvfile:
        clustered = csv.reader(csvfile)
    #from csv:
        for row in clustered:
        
        #get number of clusters
            if(row != []):
                templist.append(row[1])
                if(int(row[1]) > largest):
                    largest = int(row[1])
        #get size of cluster
                cluster_sizes[int(row[1])] = cluster_sizes[int(row[1])] + 1
        #number of samples/number of clusters
        for x in cluster_sizes:
            temp =  x + temp
        for x in cluster_sizes:
            cluster_propotion[i] = math.ceil(x/temp*int(sample_size))
            i = i + 1
        temp = 0
        for x in cluster_propotion:
            temp =  x + temp
        while (temp>int(sample_size)):
            y = rand.randint(0, 24)
            if (cluster_propotion[y] != 0):
                cluster_propotion[y] = cluster_propotion[y]-1
                temp = temp - 1
        csvfile.close()
        
        #randomly select inputs from clusters
        i = 0
        n = 0
        for x in cluster_propotion:
            while i < x:
                temp = rand.randint(0, len(templist)-1)

                if(int(templist[temp]) == n):
                    if(list_of_ids.count(temp) < 1):
                        list_of_ids.append(temp)
                        i = i+1
            i = 0
            n = n + 1
 
 
    API_1_Accuracy_GT = 0
    API_2_Accuracy_GT = 0
    API_3_Accuracy_GT = 0
    API_1_Called = 0
    API_2_Called = 0
    API_3_Called = 0

    API_1_Accuracy_SRS = 0
    API_2_Accuracy_SRS = 0
    API_3_Accuracy_SRS = 0

    API_1_Accuracy_CLUST = 0
    API_2_Accuracy_CLUST = 0
    API_3_Accuracy_CLUST = 0
    missed = 0
    #from second csv:
    with open('dataset_results.csv',encoding='utf-8') as csvfile:
        dataset = csv.reader(csvfile)
        #get total accuracy of the the whole thing for each api
        i = 0
        for row in dataset:
            if(row != []):
                i = i + 1
                if row[2] == row[1]:
                    API_1_Called = API_1_Called + 1
                if row[3] == row[1]:
                    API_2_Called = API_2_Called + 1
                if row[4] == row[1]:
                    API_3_Called = API_3_Called + 1

        API_1_Accuracy_GT = API_1_Called/i
        API_2_Accuracy_GT = API_2_Called/i
        API_3_Accuracy_GT = API_3_Called/i
    csvfile.close()
    with open('dataset_results.csv',encoding='utf-8') as csvfile:
        dataset1 = csv.reader(csvfile)
        #get accuracy of SRS
        API_1_Called = 0
        API_2_Called = 0
        API_3_Called = 0
        SRS_list = []
       
        while (len(SRS_list) <  (1+int(sample_size))):
            temp = rand.randint(0, len(SRS_list))
            if(SRS_list.count(temp) < 1):
                SRS_list.append(temp)
        i = 0
        n = 0
        missed = 0
        for row in dataset1:
            if(row != []):
                i = i + 1
                if i in SRS_list:
                    n = n + 1
                    if row[2] == row[1]:
                        API_1_Called = API_1_Called + 1
                    if row[3] == row[1]:
                        API_2_Called = API_2_Called + 1
                    if row[4] == row[1]:
                        API_3_Called = API_3_Called + 1


                        
        API_1_Accuracy_SRS = API_1_Called/n
        #print(API_1_Called)
        API_2_Accuracy_SRS = API_2_Called/n
        #print(API_2_Called)
        API_3_Accuracy_SRS = API_3_Called/n
        #print(API_3_Called)
        #print("ding")
    csvfile.close()
    with open('dataset_results.csv',encoding='utf-8') as csvfile:
        dataset2 = csv.reader(csvfile)
        #get accuracy of clustered inputs
        API_1_Called = 0
        API_2_Called = 0
        API_3_Called = 0
        i = 0
        n = 0
        for row in dataset2:
            if(row != []):
                i = i + 1
                if i in list_of_ids:
                    n = n + 1
                    if row[2] == row[1]:
                        API_1_Called = API_1_Called + 1
                    if row[3] == row[1]:
                        API_2_Called = API_2_Called + 1
                    if row[4] == row[1]:
                        API_3_Called = API_3_Called + 1
        API_1_Accuracy_CLUST = API_1_Called/n
        API_2_Accuracy_CLUST = API_2_Called/n
        API_3_Accuracy_CLUST = API_3_Called/n
        #print(API_1_Called)
        #print(API_2_Accuracy_GT)
        #print(API_3_Called)
        #print(abs(API_2_Accuracy_CLUST-API_2_Accuracy_GT)-abs(API_2_Accuracy_CLUST-API_2_Accuracy_SRS))
                
    
    csvfile.close()
    #save results to txt
    #print("GROUND TRUTH ACCURACY API 1: ",API_1_Accuracy_GT)
    #print("GROUND TRUTH ACCURACY API 2: ",API_2_Accuracy_GT)
    #print("GROUND TRUTH ACCURACY API 3: ",API_3_Accuracy_GT)
    #print("SRS ACCURACY API 1: ",API_1_Accuracy_SRS, " WITH SAMPLE SIZE: ", sample_size)
    #print("SRS ACCURACY API 2: ",API_2_Accuracy_SRS, " WITH SAMPLE SIZE: ", sample_size)
    #print(API_3_Accuracy_SRS)
    #print("SRS ACCURACY API 3: ",API_3_Accuracy_SRS, " WITH SAMPLE SIZE: ", sample_size)
    #print("CLUSTERING ACCURACY API 1: ",API_1_Accuracy_CLUST, " WITH SAMPLE SIZE: ", sample_size)
    #print(API_3_Accuracy_CLUST)
    #print("CLUSTERING ACCURACY API 2: ",API_2_Accuracy_CLUST, " WITH SAMPLE SIZE: ", sample_size)
    #print("CLUSTERING ACCURACY API 3: ",API_3_Accuracy_CLUST, " WITH SAMPLE SIZE: ", sample_size)
    z= z+1
    cluster_propotion = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    largest = 0
    cluster_sizes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cluster_propotion = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    temp = 0
    i = 0
    n = 0
    templist = []
    list_of_ids = []
    y = y + 1
    if(z%10 == 0):
        print(int(z/10))
    averageOver =averageOver+ API_1_Accuracy_CLUST
    averageOver2 = averageOver2 + API_2_Accuracy_CLUST
    averageOver3 = averageOver3 + API_3_Accuracy_CLUST
    averageOverSRS = averageOverSRS + API_1_Accuracy_SRS
    averageOverSRS2 = averageOverSRS2 + API_2_Accuracy_SRS
    averageOverSRS3 = averageOverSRS3 + API_3_Accuracy_SRS
print(abs(averageOver/z-API_1_Accuracy_GT))
print(abs(averageOver2/z-API_2_Accuracy_GT))
print(abs(averageOver3/z-API_3_Accuracy_GT))
print(abs(averageOverSRS/z-API_1_Accuracy_GT))
print(abs(averageOverSRS2/z-API_2_Accuracy_GT))
print(abs(averageOverSRS3/z-API_3_Accuracy_GT))
filenametemp = 'run-'+str(z) + 'cluster-'+ str(k)+'sample-'+str(sample_size)+ '.txt'
with open(filenametemp, 'w') as writeout:
    writeout.write(str(abs(averageOver/z-API_1_Accuracy_GT))+ "\n")
    writeout.write(str(abs(averageOver2/z-API_2_Accuracy_GT))+ "\n")
    writeout.write(str(abs(averageOver3/z-API_3_Accuracy_GT))+ "\n")
    writeout.write(str(abs(averageOverSRS/z-API_1_Accuracy_GT))+ "\n")
    writeout.write(str(abs(averageOverSRS2/z-API_2_Accuracy_GT))+ "\n")
    writeout.write(str(abs(averageOverSRS3/z-API_3_Accuracy_GT))+ "\n")
writeout.close()

