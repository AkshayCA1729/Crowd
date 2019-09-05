input_list = []                 #creating empty list
N = int(input(""))              #taking input and parsing into integer 

if 0<=N<10:                     #checking condition for N,if condition is true execute the following,else will part be executed
    for i in range(0, N):       #loop for taking inputs from range 0 to N
        ele = int(input())       
        input_list.append(ele)  #creating original list
        without_duplicateList = [] #creating empty duplicate list
        for i in input_list: 
            if i not in without_duplicateList: 
                without_duplicateList.append(i)               
    print("Without duplicates:", without_duplicateList)  #list without duplicates 
    print("Maximum :", max(without_duplicateList), "\nMinimum :", min(without_duplicateList)) #max and min number
    descending_order_list = input_list
    descending_order_list.sort(reverse = True) #descending the sorting list 
    print("Sorted in descending order:",descending_order_list)
    total = sum(input_list) #sum of list
    print("Sum: ", total)        
else:
    print("please enter valid input!")   #invalid inputs



    