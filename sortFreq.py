# n=input('Enter a string : ')
# v='aeiou'
# n=n.lower()
# dct = {k:0 for k in v}
# for ch in n:
#     if ch in v:
#         dct[ch]+=1
# def get(k):
#     return k[1]

# srtd = sorted(dct.items() , key=get)

# for i,f in srtd:
#     print(f'{i} ----->{f}')
k=8
for i in range(5,0,-1):
    for j in range(i):
        print(k,end=' ')
    print()
    k-=2
