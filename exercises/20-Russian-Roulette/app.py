import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE 
    #Round_Chambered = []
    for i in range(1):
        #students_array.append(get_color(random.randint(0,4)))
        if spin_chamber == bullet_position:
            print("You are dead!")
        else:
            print("Keep playing!")
            StopIteration
    return

print(fire_gun())