import json

with open('CalorieDailyRate.json', 'r') as file:
    data = json.load(file)

print(data['activity'])