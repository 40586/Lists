scores =[18,23,36,21,58,40,45,59]

max_ = 8
for count in range(max_-1):
    for count2 in range(max_ -1):
        if scores[count2] > scores[count2 + 1]:
            temp = scores[count2]
            scores[count2] = scores[count2+1]
            scores[count2 + 1] = temp
count4 = 0
for count3 in scores:
    print(count4+1,": ",scores[count4])
    count4 = count4+1
