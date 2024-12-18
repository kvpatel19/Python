def bubblesort(list):
    for i in (0,len(list)):
        for j in range(0,len(list)-i):
            if list[j]>list[j+1]:
               temp=list[j]
               list[j]=list[j+1]
               list[j+1]=temp
list=[19,27,2,3,5,99]
bubblesort(list)
print(list)
