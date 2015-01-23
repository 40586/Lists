#Kierna Burnett
#09-01-2015
#Search
user_list = ["Bob","George","Phill"]


name = input("Please enter the name you are looking for")
    

def search(user_input,user_list):
    count = 0
    found = False
    while not found and count < len(user_list):
        if user_list[count] == user_input:
            found = True
            
        count = count + 1
    if found = False:
        count = 0
    else:
        count = count - 1
    return count, found

user_input = input("Please enter the name you are looking for")
count,found = search(user_input,user_list)
print(count,found)
