#We will first create a  list that contains the participants in the competition
#and their swimming time, biking time, and running time
contestants = [
(1,2,3), #Contestant #1
(2,3,10), #...
(4,5,3)  #Contestant #N
]

#Deadlines list
deadline = [0]*len(contestants)

#We calculate the total deadline for each one of the contestants
for i in range(0,len(contestants)):
 contestant = contestants[i]
 deadline[i] = sum(contestant)

#We print our results
print(deadline)

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
  pivot0 = list(array0[0])

  for i in range(0,len(array)):
   element = array[i]
   element0 = list(array0[i])

   if element<pivot:
    lowerlist.append(element)
    lower0.append(element0)
   elif element>pivot:
    upperlist.append(element)
    upper0.append(element0)
   else:
    print(pivot0)
    pivotlist.append(element)
    pivot0.append(element0)

  upperlist,upper0 = quicksort(upperlist,upper0)
  lowerlist,lower0 = quicksort(lowerlist,lower0)

 return lowerlist + pivotlist + upperlist, list(lower0 + pivot0 + upper0)

#We will return an array with the indexes in the order that they need to be accessed
schedule,sortcont = quicksort(deadline, contestants)

print(sortcont)