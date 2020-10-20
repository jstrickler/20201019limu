
# OOP approach
from knightfile import KnightFile

kf = KnightFile('DATA/knights.txt')

for knight in kf:
    print(knight.title, knight.name)  # properties
    print(knight.get_title(), knight.get_name())  # getters (accessors)

oldest = KnightFile.get_oldest_knight()

# non-OOP approach
from knightfile import read_knight_file, get_oldest_knight

file_info = read_knight_file('DATA/knights.txt')
for knight_info in file_info:
    print(knight_info['title'], knight_info['name'])

oldest = get_oldest_knight(knight_info)

