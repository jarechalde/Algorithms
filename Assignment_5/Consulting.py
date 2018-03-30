#Low stress jobs
l = [10,1,10,10]

#High Stress jobs
h = [5,50,5,1]

length = len(l)

#Initializing the revenue to 0
rev = [0]*(length+1)

#Initializing some values
rev[0] = 0
rev[1] = max(l[0],h[0])

for i in range(1,length):
 p = i+1
 if h[i]>l[i]+l[i-1]:
  rev[p] = h[i]+rev[p-2]
 else:
  rev[p] = l[i]+rev[p-1]
print(rev)
