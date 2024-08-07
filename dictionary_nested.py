# Nested Dictionary: Nesting Dictionary means putting a Dictionary inside another Dictionary.
# Its a collection of dictionaries into one dictionary

course = {
    'php': {'duration':'2 Months','fees': '15000'},
    'python': {'duration':'4 Months','fees': '20000'},
    'java': {'duration':'6 Months','fees': '25000'}
}
# print(course['python']['fees'])

course['java']['fees']=5000

for k,v in course.items():
    print(k,v['duration'],v["fees"])
