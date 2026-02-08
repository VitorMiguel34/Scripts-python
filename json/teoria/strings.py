'''
json.loads() -> transforma uma string em um dicionario
json.dumps() -> transforma um dicionario em uma string
'''

import json

obj_string = '''
{
    "estudando": "true",
    "nome": "Victor"
}
'''

json_ = json.loads(obj_string)
print(json_)
obj = json.dumps(obj_string,ensure_ascii=False)
print(obj)
