from jsonschema import validate
import json

JSONfile = input()

with open(JSONfile) as JSON_file, open("./Result_7.1/pattern.json") as pattern:
    JSON_f = json.load(JSON_file)
    schema = json.load(pattern)

try:
    validate(JSON_f, schema)
    print("Валидация прошла успешно")
except Exception as e:
    print(f"Ошибка валидации: {e}")