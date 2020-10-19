

name = 'Chris Hemsworth'

values = [5, 10, 15, 20]

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

for obj in name, values, person:
    print(obj, len(obj), obj[0], obj[-1], obj[0:2])

print(name[:4], name[6:9], name[-9:])

# S[start:stop]   S[start:stop:step]

print(name[6:99])

print(name[-20:3])

