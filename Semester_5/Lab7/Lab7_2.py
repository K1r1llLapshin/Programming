import json

with open('new_ex_2_Lab7_2.json') as data:
    json_ = json.load(data)
    
name_phone = {}
for user in json_['users']:
    name_phone[user['name']] = user['phoneNumber']

print(name_phone)