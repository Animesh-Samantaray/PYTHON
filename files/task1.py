with open('task1.txt','w') as f:
    f.write('1hii java\n')
    f.write(' java byy\n')
    f.write('xxx is a java learning')

with open('task1.txt','r+') as f :
    data = f.read()
    data=data.replace('java','python')
    f.seek(0)
    f.write(data)
    if 'learning' in data:
        print('learning is present')
    else:
        print('learning is not present')