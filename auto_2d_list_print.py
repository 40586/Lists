#Kieran Burnett
#13-01-2015
#Auto 2D list print
player = [
    ["k1llmAchine",51,49],
    ["bob2247",5 , 99],
    ["hAxOr12",72,30]
]

def get_length(player,col):
    col1 = 0
    for play in player:
        temp1 = len(str(play[col]))
        if temp1 > col1:
            col1 = temp1
    return col1

def get_length_all(player):
    length=[]
    for count, play in enumerate(player):
        length.append(get_length(player,count))
    print(length)
    test_(player,length)

def test_(player,length):
    for play in player:
        row = "|"
        for num,item in enumerate(play):
            insert = "{0:<{1}}".format(str(item),length[num])
            row = row + insert
            row = row + "|"
        print("-"*len(row))
        print(row)
    print("-"*len(row))


get_length_all(player)
