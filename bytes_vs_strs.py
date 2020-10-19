
country = "Wakanda"

print(type(country))
print(country[0], len(country), country.upper())

bc = country.encode()   # encode non-ASCII chars with utf-8

print(bc, type(bc), len(bc))
print(bc[0])

cs = "20\u00B0 Celsius"
print(cs, type(cs), len(cs))

bcs = cs.encode(encoding="ascii", errors='ignore')  # 'ignore' 'strict' 'replace'
print(bcs, type(bcs), len(bcs))

ocs = bcs.decode()
print(ocs, type(ocs), len(ocs))

x = "abc"
print(isinstance(cs, str), isinstance(cs, bytes))
print(isinstance(bcs, str), isinstance(bcs, bytes))





