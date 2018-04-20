#We will first create a  list for job weight and time
jobst = [2,4,5,3,5]
jobsw = [32,23,44,65,23]

def quicksort(array,array0):
 upperlist = []
 lowerlist = []
 pivotlist = []

 upper0 = []
 lower0 = []
 pivot0 = []

 #If the length of the array is 1 it doesnt need sorting of any kind
 if len(array)<=1:
  return array,list(array0)
 
 #Else, we will separate the list into the upper elements and lower
 else:
  pivot = array[0]

  for i in range(0,len(array)):
   element = array[i]
   element0 = array0[i]

   if element<pivot:
    lowerlist.append(element)
    lower0.append(element0)
   elif element>pivot:
    upperlist.append(element)
    upper0.append(element0)
   else:
    pivotlist.append(element)
    pivot0.append(element0)

  upperlist,upper0 = quicksort(upperlist,upper0)
  lowerlist,lower0 = quicksort(lowerlist,lower0)

 return lowerlist + pivotlist + upperlist, list(lower0 + pivot0 + upper0)

#We will return an array with the indexes in the order that they need to be accessed
sortw,jobst = quicksort(jobsw, jobst)

#We initialize the variables
s_job = 0 
sumw = 0

#Now we will start scheduling the events
for i in range(len(jobsw)-1,-1,-1):
 t = jobst[i]
 w = jobsw[i]

 #Finish time of the job
 c = s_job+t

 #Update the sum
 sumw = sumw + c*w

print('Total weighted sum: %i' %sumw)

