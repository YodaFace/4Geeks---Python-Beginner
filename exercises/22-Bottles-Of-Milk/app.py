

def number_of_bottles(): 
    # number_of_bottle = []
    for i in reversed(range(100)): 
        if i > 1:
            print(str(i)+" bottles of milk on the wall, "+str(i)+" bottles of milk.")
            i -= 1
            print("Take one down and pass it around, "+str(i)+" bottles of milk on the wall.\n")
        elif i == 1:
            print(str(i)+" bottles of milk on the wall, "+str(i)+" bottles of milk.")
            i -= 1
            print("Take one down and pass it around, no more bottles of milk on the wall.\n")
        else:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()





## ORIGINAL CODE THAT I CAME UP WITH ## 
    # for i in reversed(range(100)): 
    #     if i > 1:
    #         print(str(i)+" bottles of milk on the wall, "+str(i)+" bottles of milk.")
    #         i -= 1
    #         print("Take one down and pass it around, "+str(i)+" bottles of milk on the wall.\n")
    #     elif i == 1:
    #         print(str(i)+" bottles of milk on the wall, "+str(i)+" bottles of milk.")
    #         i -= 1
    #         print("Take one down and pass it around, no more bottles of milk on the wall.\n")
    #     else:
    #         print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
