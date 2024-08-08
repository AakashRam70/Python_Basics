import datetime

# x = datetime.datetime.now()
#
# print(x)

now = datetime.datetime.now()

year = now.strftime('%Y')

pmam = now.strftime('%p')

print("year:", year)

print("PM/AM", pmam)


