#Number of rungs
n = 2**32

print('Number of rungs: %i\n' %n)

jar = 'OK' #Set the status of the initial jar to OK
bd = 30000 #Breaking distance
r0 = 0 #Starting rung
kmax = 12 # Maximum number of jars for the test

def test(start,end,k,jar):
 print('Starting rung: %i Ending rung: %i Length: %i' %(start,end,end-start))
 jar = 'OK' #We set the status of the current jar to OK
 r = start #Starting rung
 #We calculate the step size and the number of divisions
 exp = (1./(k+1))
 div = (end-start)**(exp)
 step = (end-start)/div

 #Convert the number of divisions and steps to integers
 div = int(div)
 step = int(step)

 #If the number of divisions is only one, we will fix the step
 #size to 1
 if step>(end-start) or div == 1:
  step = 1

 print('Divisions: %i Step size: %i' %(div,step))
 
 #While the jar is not broken, we increase the drop by the step size
 while (jar=='OK'):
  r0 = r #Save the current safest rung
  r = r + step #Current rung
  if (r>bd):
   jar = 'RIP'
   print('Current Highest safe rung: %i\n'  %r0)
   k = k +1
   #While we still have jars available, and the number of divisions is greater
   #than one, we continue to search
   if (k<= kmax and div>1):
    test(r0,r,k,jar)
   
test(0,n,1,jar)










