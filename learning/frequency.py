l = [1,3,2,4,5,1,2,1,5,2,1,9]
check = [] 
for i in range(len(l)):
    if l[i] not in check:                 
      count=0        
      for j in range(len(l)):
           if l[i]==l[j]:
            count+=1
      print(f"the frequency of {l[i]} is {count}")  
      check.append(l[i])
