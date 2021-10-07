cover = input("What type of cover does the book have?\n")
if cover == "soft":
    perfect = input("Is the book perfect-bound?\n")
    if perfect == "yes":
        print("Soft cover, perfect bound books are very popular!\n")
    else:
        print("Soft covers with coils or stitches are great for short books\n")
else:
    print("Books with hard covers can be more expensive!\n")