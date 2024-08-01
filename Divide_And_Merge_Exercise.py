

Numbers = [10,20,30,40,50,60,70,80,90,100]
print(Numbers)

def divideList(list1):
    divide = len(list1) // 2
    return list1[:divide], list1[divide:]

count = 0
list_num = 0
check_list = True
new_list = 0
newNew = 0
while count < 8:
    if(list_num == 0):
        listA, listB = divideList(Numbers)
    while new_list < list_num:
        if check_list:
            if newNew == 0:
                Numbers = listA # This will be 10,20  and 30,40,50 first time
          #  print("This is the list A: ", listA)
            check_list = False

            listC, listD = divideList(Numbers)
            print(listC,listD, end=' ')
        else:
            if newNew == 0: 
               Numbers = listB # This will be 60,70 and 80,90,100 first time
         #   print("This is the list B: ", listB)
            check_list = True
            listE, listF = divideList(Numbers)
            print(listE,listF)
        new_list += 1
        newnew += 1
    if (list_num == 0):
        print(listA,listB)
      # print("10,20,30,40,50,60,70,80,90,100")
    list_num += 2
    count += 1




    