import json

data = {
    "id": 3,
    "total": 300.00,
    "items": [
    {
        "name": "item 3.1",
        "quantity": 5,
        "price": 150.00
    },
    {
        "name": "item 3.2",
        "quantity": 10,
        "price": 50.00
    },
    {
        "name": "item 3.3",
        "quantity": 23,
        "price": 500.00
    }
    ]
}

with open('./Data/ex_3.json') as data_json:
    json_ = json.load(data_json)

json_["invoices"].append(data)

with open('result_7.3.json', 'w') as write:
    json.dump(json_, write, indent=4)