# 'r+'	Read + Write	Reads and writes without truncating. File must exist. Starts at beginning.
# 'w+'	Write + Read	Overwrites file, creates if not there. Truncates everything. Starts at beginning.
# 'a+'	Append + Read	Appends to the file, creates if not there. Can read, but writing always goes to the end.
# 'x+'	Create + Read/Write	Creates new file, errors if file exists.

# w ---> overwrites the entire file
f = open('pre.txt', 'r')
value = f.read()
f.close()
# a ---> appends at the end
f=open('kaka.txt','w+')
f.write('hii animesh \n\t\n\t'+value)
data = f.read()
print(data)
f.close()
