myList=['bharath',10,20,40,'moulipavan']
myList[1:3]=[200,300]
print(myList)
print(myList[2])
print(type(myList))
print(len(myList))
print(myList[2:5]) # (search starting from index 0 and then 0,1,2,.... so on but it cant exclude the last index what we given)


#extend(add files from another list to current list )
list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]
list1.extend(list2) 
print(list1)
print(list2[-3])
print(list1[2])




list5 = ['hello',"github","123","love"]
list5.clear() #clear 
print()
