my_list=[]
#my_tuple=(10,20,30,40)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(2,15) 
list_2=[50,60,70] #create another list

my_list.extend(list_2) #add the 2 lists
my_list.pop() #deletes the last object inthe list
my_list.sort()
my_list.index(30)
#printing the output
print(my_list)
print(my_list.index(30))