# Lineal Search !!!!!!!!!!
import random

def Lineal(list,target):
    match = False

    for element in list:
        if element == target:
            match = True
            break
    return match

if __name__=="__main__":
    ListSize = int(input("Enter the size of the list:"))
    n = []
    for i in range(ListSize):
        n.append(i)
    
    print (f'The list is: \n {n}\n')
    
    Objetive= int(input("Enter the number to search in the list: "))
    if Lineal(n,Objetive) == True:
        print("The number is in the list")
    else:
        print("The number is not in the list.")
    
# Now with a Random list 
    print("\n\n now an automatic list will be generated with random numbers:")
    howmany = int(input("Select how many numbers do you want in the list, max 100. "))
    #now i can control if the users enter correctly the number but i wont.
    newlist = [random.randint(0 , 100) for i in range(howmany)]
    print("Random list created succesfully")
    Objetive= int(input("Enter the number to search in the list: "))
    if Lineal(newlist,Objetive) == True:
        print("The number is in the list")
    else:
        print("The number is not in the list.")
        print(f'Here you got the random list created: ')
        print(newlist)
