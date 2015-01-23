#Kieran Burnett
#09-01-2015
#Bubble sort

people = ["z","George","Bob","Phil","Kieran","Leon","A","h"]

def bubble_sort(people):
    count2 = 1
    swap = 1
    while swap != 0:
        swap = 0
        for count in range(len(people)-count2):
            if people[count] > people[count + 1]:
                temp = people[count]
                people[count] = people[count + 1]
                people[count + 1] = temp
                swap = swap + 1
                print(people)
        count2 = count2 + 1
bubble_sort(people)
