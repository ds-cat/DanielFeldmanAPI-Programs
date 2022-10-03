from http.client import responses
from sqlite3 import DataError
import requests
import json
import time

#open file 
input_file = open("reviews.txt",encoding='utf-8', errors='ignore')
output_file = open("api_two_results.txt", 'w')

#read file line by line
input_lines = input_file.readlines()

#api set up

url ="https://text-sentiment.p.rapidapi.com/analyze"

retry = True

DataError = False


#send each line to api
for line in input_lines:
	retry = True
	while retry == True:
		pos = False
		neg = False
		neu = False
		payload = "text=" + line
		headers = {
			"content-type": "application/x-www-form-urlencoded",
			"X-RapidAPI-Key": ,
			"X-RapidAPI-Host": "text-sentiment.p.rapidapi.com"
		}

		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.status_code)
		if response.status_code == 200:
			retry = False
			response = response.json()
	print(response)
	if response != 1000:
		in_dict =  "pos" in response
		print(in_dict)
	
		if in_dict:
			a = response['pos']
			b = response['neg']
			output_text = "error"
			if a > b:
				pos = True
				output_text = "positive\n"
			else:
				if b > a:
					neg = True
					output_text = "negative\n"
				else:
					neu = True
					output_text = "neutral\n"
		else:
			output_text= "error\n"
	else:
		output_text= "error\n"
	print(output_text)

	#save response to new file and line
	output_file.write(output_text)
output_file.close()



