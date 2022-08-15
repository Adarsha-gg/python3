import requests
import random
num = random.randint(1,10)
paramerters = {
    "amount":10,
    "type":"boolean"}
ques = requests.get("https://opentdb.com/api.php",params=paramerters)
ques.raise_for_status()
data =ques.json()
question_data = data["results"]
