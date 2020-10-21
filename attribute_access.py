import re
from president import President

p = President(26)
print(type(p))

fields_wanted = ['first_name', 'last_name', 'favorite_beatle']

print(p.first_name)

for field in fields_wanted:
    if hasattr(p, field):
        print(field, getattr(p, field))
    else:
        print(field, "is not an attribute")

print(dir(p))

name_fields = [attr for attr in dir(p) if re.search('name', attr, re.I)]
print(name_fields)

def gfn(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "get_first_name", gfn)

print(p.get_first_name())
print()

for attr in dir(p):
    if not attr.startswith('_'):
        attr_value = getattr(p, attr)
        if not callable(attr_value):
            print(attr, attr_value)

