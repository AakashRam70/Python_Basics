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