import csv
output = open('result_appened_dataset.csv','w', encoding="utf-8")
reviews = open("reviews.txt", "r", encoding="utf-8")
review_lines = reviews.readlines()

dataset = open("dataset_results.txt", "r")
dataset_lines = dataset.readlines()

api_one = open("api_one_results.txt", "r")
api_one_lines = api_one.readlines()

api_two = open("api_two_results.txt", "r")
api_two_lines = api_two.readlines()

api_three = open("api_three_results.txt", "r")
api_three_lines = api_three.readlines()

# create the csv writer
writer = csv.writer(output)


header = ['text', 'dataset', 'fyhao api', 'twinword api', 'symanto api']

review_data= []
for line in review_lines:
    review_data.append(line)


dataset_data= []
for line in dataset_lines:
    print(line)
    dataset_data.append(line)

one_data= []
for line in api_one_lines:
    one_data.append(line)

two_data= []
for line in api_two_lines:
    two_data.append(line)

three_data= []
for line in api_three_lines:
    three_data.append(line)



# write a row to the csv file
writer.writerow(header)

count = 0
while count < 2000:
    entry = [review_data[count], dataset_data[count], one_data[count], two_data[count], three_data[count]]
    writer.writerow(entry)
    count= count +1

# close the file
output.close()