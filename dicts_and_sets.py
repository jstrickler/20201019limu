airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports.get('EWR'))
print(airports.get('IND'))
print(airports.get('IND', 'NOT FOUND'))
print(airports['YOW'])

print(airports.setdefault('IND', 'Indianapolis'))
print(airports)

my_stuff = [('IAD', 'Dulles'), ('YCC', 'Calgary'), ('ELM', 'Elmyra'), ('SEA', 'Seattle')]

for abbr, name in my_stuff:
    print(airports.setdefault(abbr, name))

c1 = ['Bulgaria', 'Israel', 'Canada', 'UK', 'UK', 'UK', 'UK', 'UK'] 
c2 = ['Israel', 'Mexico', 'Panama', 'Bulgaria', 'UK', 'Burkina Faso', 'Mali', 'East Timor']

s1 = set(c1)
s2 = set(c2)

print("Both (intersection):", s1 & s2)
print("Only one (Xor):", s1 ^ s2)
print("All (union):", s1 | s2)
print("Just s1:", s1 - s2)
print("Just s2:", s2 - s1)
print("Union WITH DUPES:", list(s1) + list(s2))