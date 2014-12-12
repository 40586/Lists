shopping_list = []
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

for index, item in enumerate(shopping_list):
    print(" {0}. {1}".format(index+1,item))
