def  observed():
    a = 0
    my_list = []
    while (a < 5):
        b = input("Please enter an observation:")
        my_list.append(b)
        a += 1
    return(my_list)
def remove_observations():
    while(decision != "no"):
        decision = input("Do you wish to remove an observation (yes/no)?")

def run():
