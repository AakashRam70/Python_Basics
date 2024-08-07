# get()
# keys()
# values()
# items()

# d = {
#     "name":'python',
#     "fees": '4000',
#     "duration":'2 Months'
# }

# n = d.get("duration");
# print(n)

# for a in d.keys():
#     print(a)

# for a in d.values():
#     print(a)

# for a in d.items():
#     print(a)

# for a,b in d.items():
#     print(a,b)

d = {
    "name":'JavaScript',
    "fees": '2000',
    "duration":'4 Months'
}

a = d.pop( "fees")
print(d)
print(a)