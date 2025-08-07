import time
k = time.time()
 
for i in range(1000):
    print(i)
print(k)
print(time.time())
print(time.time()-k)

time.sleep(10)
print('I am running after 10 secs')