#Takes input CSV
import csv
inputValues = []
with open('input.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        row = row.strip()
        inputValues.append(row)

#Takes a set of IDs as CSV (int 1 through 2000)
keys = []
with open('key.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        row = row.strip()
        keys.append(keys)
    #Ids should be in the form of a CSV for example
	    #Input : 5,12,55…ect.
    #The number of IDs should be the number of results compared

#Check for duplicates and remove them,
processedKeys = [*set(keys)]

#Use IDs took look at corresponding line (i.e ID 10 should look at the 11th line, ID 0 should look at the header)
#Use the dataset positive/negative data to determine if each API got that text entry correct and store the number of correct along with the number looked at for each API
#Use majority voting to determine if each API got that text entry while ignoring dataset for the voting
#Make a tie breaker
#Can be anything: coin flip, result priority, api priority ect.
#If an API has an input of error it is automatically incorrect
#Save to a file the number each API got correct along with than number of entries looked at

