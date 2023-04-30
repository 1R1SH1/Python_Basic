import json
from typing import List, Dict

new_data = open('json_new.json', "r")
old_data = open('json_old.json', "r")

new = json.loads(new_data.read())
old = json.loads(old_data.read())

def compare(dict_1: Dict, dict_2: Dict, diff: List) -> Dict:
    """Функция, перебирающая ключи в двух JSON-файлах на предмет не соответствия значений"""
    for key in dict_1.keys():
        if isinstance(dict_1[key], dict):
            compare(dict_1[key], dict_2[key], diff)
        elif dict_1[key] != dict_2[key] and key in diff:
            dict_of_values[key] = dict_1[key]
    return dict_of_values


dict_of_values: Dict = {}
diff_list: List[str] = ["services", "staff", "datetime"]
result: Dict = compare(new, old, diff_list)
print(result)

with open('result.json', 'w') as final:
    json.dump(result, final, indent=4)