import csv
records = []
headings = []
def load_data(file_path):
    print("Loading data...")
    b = 0
    with open(file_path) as my_file:
        read = csv.reader(my_file)
        headings = next(read)
        for line in read:
            records = line
            if line != "\n":
                b += 1
        return(b)
def display_menu():
    a = int(input("Please select one of the following options:"))
    print("[1] Display the names of all passengers\n[2] Display the number of passengers that survived\n[3] Display the number of passengers per gender\n[4] Display the number of passengers per age group")
    return(a)
def display_passenger_names():
    print("The names of the passengers are...")
    for a in records:
        print(f"{a[3]}")

def run():
   records = load_data("titanic.csv")
   selected_option = display_menu()
   print(f"You have selection option: {selected_option}")
   print(f"Successfully loaded {records} records.")
   display_passenger_names()

run()