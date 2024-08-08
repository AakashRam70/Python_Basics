# JSON is JavaScript Object Notation 
# It is mainly used for storing and transfering data between browser and server
# JSON is text, written with JavaScript object notation
# Python too supports JSON with a built-in pakage cales json.

import json
d = {
    'course_name':'Python',
    'fees':15000
}

f = json.dumps(d)
print(type(f))

print(f)

# Converting JSON to Python Objects 
# If you have a JSON string, you can parse it by using the json.loads() method. 

# import json 
dictionary = '{"cname":"Python", "fees":12000, "duration":"2 Months"}'

x = json.loads(dictionary)
print(type(x))
print(x)

