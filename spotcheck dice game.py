import random


def inti_freq(temp,freq):
    for count1 in range(1,20):
        for count in range(1,6):
            if temp[count == count:
                freq[count] = freq[count] + 1
    
def dice_throw(temp):
    for count in range(1,20):
        temp_ = random.randint(1,6)
        temp.append(temp_)

def display(score,freq):
    print("score    frequency")
    for count in range(1,6):
        print(score[count],"    ",freq[count])
        
def freq_die_scores():
    freq = [0,0,0,0,0,0]
    score = [1,2,3,4,5,6]
    temp = []
    dice_throw(temp)
    inti_freq(temp,freq)
    display(score,freq)


freq_die_scores()
