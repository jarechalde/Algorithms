#We will first create a  list that contains the participants in the competition
#and their swimming time, biking time, and running time
contestants = [
(1,1,2,3), #Contestant #1
(2,4,6,6), #Contestant #2  
(3,2,3,5),#...
(4,4,5,3)  #Contestant #N
]

#Deadlines list
deadline = [0]*len(contestants)

#We calculate the total deadline for swimming for each one of the contestants
for i in range(0,len(contestants)):
 contestant = contestants[i]
 deadline[i] = sum(contestant[1:4])

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
   element0 = list(array0[i])

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
schedule,sortcont = quicksort(deadline, contestants)

#We initialize the variables
s_swim = 0 

#Now we will start scheduling the events
for contestant in sortcont:

 print("\n")
 print("Contestant ID: %i" %contestant[0])

 #The time that will take the contestant to finish each one of the sections
 t_swim = contestant[0] 
 t_bike = contestant[1]
 t_run = contestant[2]

 #Swimming time
 f_swim = s_swim + t_swim
  
 #Biking time
 s_bike = f_swim
 f_bike = s_bike + t_bike

 #Running time
 s_run = f_bike
 f_run = s_run + t_run

 print("Start Swimming: %i End Swimming: %i" %(s_swim,f_swim))
 print("Start Biking: %i End Biking: %i" %(s_bike,f_bike))
 print("Start Running: %i End Running: %i" %(s_run,f_run))

#The next contestant will start swimming when the previous one is done
 s_swim = f_swim
