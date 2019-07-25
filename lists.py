lst1=['a','b','c']
lst2=['d','e','f']
lst3=['g','h','i']
var1={'a','b','c'}
var2={'d','e','g'}
tuple1=('a','b','c')
# set1=('a','b','c','a')
# print(type(lst1))
# print(type(var1))
# print(type(tuple1))
# print(set1)
# print(dir(lst1))
# print(lst1.append('d'))
# lst2.extend(lst1)
# print(lst2)

# lst1.remove('a')
# print(lst1)

lst3=lst1.copy()
print(lst3)

lst1.reverse()
print(lst1)

print(lst1.count('a'))
print(lst2.count('g'))

# print(dir(var2))
# print(var2.count('d'))

set1={'a','b','c'}
set2={'d','e','f'}
print(dir(set1))
print(set1.union(set2))