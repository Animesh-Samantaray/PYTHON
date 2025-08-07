with open('num.txt','r+') as f:
    f.write('0099aaaa')
    f.seek(0)
    print(f.read())
