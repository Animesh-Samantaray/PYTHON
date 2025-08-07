s="aabb0123456789"
print(s.endswith('9'))
print(s.capitalize()) #capitalize 1st char
s=s.capitalize()
print(s)
s=s.replace('01',' Animesh ')
print(s)

#find
print(s.find('7'))#return 1st index of value -1 if not present
#count
#return how many times vlue present in string
print(s.count('p'))