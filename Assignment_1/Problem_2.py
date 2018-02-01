men = ['V','W','X','Y','Z']
women = ['A','B','C','D','E']

#Men's preferences
vpref = ['B','A','D','E','C']
wpref = ['D','B','A','C','E']
xpref = ['B','E','C','D','A']
ypref = ['A','D','C','B','E']
zpref = ['B','D','A','E','C']

#Create a dictionary to store men's preferences
menpref = {'V':vpref,'W':wpref,'X':xpref,'Y':ypref,'Z':zpref}

#Woman's preferences
apref = ['Z','V','W','Y','X']
bpref = ['X','W','Y','V','Z']
cpref = ['W','X','Y','Z','V']
dpref = ['V','Z','Y','X','W']
epref = ['Y','W','Z','X','V']

#Create a dictionary to store women's preferences
womenpref = {'A':apref, 'B':bpref, 'C':cpref, 'D':dpref, 'E':epref}

#We will use two dictionaries to check man and woman availability
manav = dict(zip(men,[1]*len(men)))
womanav = dict(zip(women,[1]*len(women)))

#Engage dictionary, we will use woman as a key to help check the womans preference
eng = {'A':None,'B':None,'C':None,'D':None,'E':None}

###Do not forget to implement the efficient algo###

#Implementation of the propose and reject algorithm

#We still need to go back to a man if he gets free, and check woman's preference list

menav = len(men)

while menav>0:
 for man in men:
  print('Engaging man: %s' %man)
  while manav.get(man) == 1:
   #We propose to one woman
   for i in range(0,len(menpref.get(man))):
    #Now we start proposing to every woman on the list
    pref = menpref.get(man)
    #The current woman we are proposing to
    woman = pref[i]
    #If the woman is not engaged, they get automatically engaged
    if womanav.get(woman)==1:
     print('Engaged\n')
     #Engage that man and woman
     eng[woman] = man
     #Set that man's and woman's availability to 0
     manav[man] = 0
     womanav[woman] = 0
     
     menav = menav - 1
     
     #Break the for loop and go to the next man
     break
    #If the woman is already engaged we will have to check the womans preference list
    else:
     currentengman = eng.get(woman)
     print('%s already engaged to: %s' %(woman,currentengman))
     #His position in the list (we need to implement this outside the loop)
     poseng = womenpref.get(woman).index(currentengman)
     posnew = womenpref.get(woman).index(man)
     print(posnew,poseng)
     #If this man is higher in the list of pref. than the other man we dump the current one and 
     #engage her with this one
     if posnew<poseng:
      print('Updating Engagement\n')

      #Engage that man and woman
      eng[woman] = man

      #We set this mans availability to 0 and the old engaged man to 1
      manav[man] = 0
      manav[currentengman] = 1

      #Append the man to the end of the list so we have to iterate over him again
      men.append(currentengman)
      print(men)
    
      break
 
      #Engage them
      eng[woman] = man

     #If this man is lower in the list that the man the woman is already engaged with,
     #this man will try to engage to the next woman on the list
     else:
      continue
    
#We print the final results
print(eng)

###Changing the man order of proposal###

#In this case the order of man proposing goes from Z to V instead

###Another different implementation###

#What if women were proposing to men instead?

