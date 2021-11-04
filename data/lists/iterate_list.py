def movements():
    directions = [ "Move Forward", "Move Backward", "Turn Left" ,"Turn Right"]
    return (directions)
def menu():
    a = int(input("Please select a direction:"))
    str = movements()
    a = 0;
    while(a <= 4)
        print(f"{a}: {str[a]}")
        a = a + 1
def run():
    menu()

if __name__ == "__main__":
    run()