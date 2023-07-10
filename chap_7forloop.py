fruits = ['apple','bananna','peer','graphes']
for item in fruits:
   print(item)
 
#for loop
for i in range (1,8):
     print(i)

#optional else in for loop.
for i in range (8):
     print(i)
else:
     print("this inside the loop")

#break statement
for i in range (10):
     
     if(i %2!= 0):
      continue
     print(i)
  
#pass statement
i = 4 
if i>4:
     pass
print(i)
