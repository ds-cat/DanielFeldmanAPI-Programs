from http.client import responses
import requests
import json

#open file 
input_file = open("reviews.txt",encoding='utf-8', errors='ignore')
output_file = open("api_three_results.txt", "a")

#read file line by line
input_lines = input_file.readlines()

#api set up
url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"
count = 1
retry = True
retry_count = 0
output = ""




#send each line to api
for line in input_lines:
	retry = True
	while retry:

		payload = [
			{
				"id": count,
				"language": "en",
				"text": line
			}
		]
		headers = {
			"content-type": "application/json",
			"Accept": "application/json",
			"X-RapidAPI-Key": "4a4af92182mshf92efd60ccdae50p1c8d0cjsnd62da1d35446",
			"X-RapidAPI-Host": "sentiment-analysis9.p.rapidapi.com"
		}


		response = requests.request("POST", url, json=payload, headers=headers)
		print(response)
		if (response.status_code == 200):#if error retry
			retry = False
			response = response.json()
			print(response[0]["predictions"][0]["prediction"])
			output=(response[0]["predictions"][0]["prediction"] + "\n")
			retry_count = 0
		else:
			if(retry_count < 3):
				retry = True
				retry_count= retry_count+1
			else:
				output = ("error\n")
				retry_count = 0
				retry = False
			
		

		#print(response['type'])
	

	#save response to new file and line
	print (output)
	output_file.write(output)
output_file.close()
	



