#replace
list6 = [10,20,30]
list6[1:3] = ["love","hate"]
print(list6)

#insert items
list7 = [20,50,70]
list7.insert(30,40)
print(list7)

#append(adding items at end of list)
list8 = [80,90,10,40]
list8.append(50)
print(list8)

#Remove list
#remove a specified item
list3 = ["guava","grapes","pineapple"]
list3.remove("grapes")
print(list3)
print(list3[1])

list9 = ["john","peter","robin"]

list9.pop(1)  #pop
list9.pop() #(if we cant indicate any index on pop then it will remove last item )
print(list9)
