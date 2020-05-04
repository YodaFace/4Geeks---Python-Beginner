import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    students_array = []
    #your loop here
    for i in range(10): 
        #students_array = random.randint(0,4)
        #students_array = students_array.append(get_color(random.randint(0,4)))
        students_array.append(get_color(random.randint(0,4)))
        # WHAT THIS MEANS IN ORDER (Read Backwards) 
        # random.randint(0,4) = Produce a random integer for "get_color"
        # get_color = call the function which has a dictionary that produces a color based on the random integers that were prodcued in the randint function
        # students_array.append = take what was produced from the previous functions and insert it after the current values present in student_array list
        # for testing
        # print(i)
        #print(i + students_array)
    return (students_array)


print(get_allStudentColors())



## BORROWING CODE FROM LESSONS ## 
# def sum(a,b):
#    return a+b

# def multiply(a,b):
#    return a*b;

# print(multiply(sum(3,5),sum(1,1)))


# # the execution goes from inside to outside 
# # first, the sum of 3+5 and 1+1 will be calculated 
# # then, their respective results will be multiplied 
# firstSum = sum(3,5)
# secondSum = sum(1,1)
# print(multiply(firstSum, secondSum))