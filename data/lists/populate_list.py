def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left" , "Turn Right"]
    return (directions)
def menu():
    a = 0
    tr = directions()
    vm = []
    print("Please select a direction:")
    while (a <= 3) :
        b = 0
        while (b <= 3):
            print(f"{tr[b]}")
            b = b + 1
        c = input()
        vm[a] = tr[c]
        a = a + 1
    print(f"{vm}")
def run():
    print("Working out escape route...")
    menu()

run ()