def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return (path)
def run():
    a = 0
    lsit = movements()
    print("Moving...")
    while (a <= 4) :
        print(f"Move {list[a]} for {list[a + 1]} steps")
        a = a + 2

if __name__ == "__main__":
    run()