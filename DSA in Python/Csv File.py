import csv
import os

def write():
    mode = 'a' if os.path.exists('myfile.csv') else 'w'
    with open("myfile.csv", mode, newline='') as f:
        fobj = csv.writer(f)
        if mode == 'w':
            fobj.writerow(["Roll", "Name", "Marks"])

        while True:
            try:
                Roll = int(input("Enter Your Roll: "))
                Name = input("Enter Your Name: ").strip()
                Marks = int(input("Enter Your Marks: "))
                data = [Roll, Name.upper(), Marks]
                fobj.writerow(data)
            except ValueError:
                print("❌ Please enter valid numbers for Roll and Marks.")
                continue

            choice = input("1 -> Enter More\n2 -> Exit\nEnter choice: ")
            if choice == '2':
                break

def read():
    print("\n📋 Saved Records:")
    try:
        with open("myfile.csv", "r") as d:
            dobj = csv.reader(d)
            for i, row in enumerate(dobj):
                if i == 0:
                    print(f"{' | '.join(row)}")
                    print("-" * 30)
                else:
                    print(f"{' | '.join(row)}")
    except FileNotFoundError:
        print("❌ No records found. File does not exist.")

def search():
    try:
        with open("myfile.csv", "r") as q:
            qobj = csv.reader(q)
            roll = int(input("Enter the Roll Number to Search: "))
            next(qobj)  # Skip header
            found = False
            for row in qobj:
                if int(row[0]) == roll:
                    print("✅ Record Found:", row)
                    found = True
                    break
            if not found:
                print("❌ Record Not Found.")
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print("⚠️ Error:", e)

# === Menu Loop ===
while True:
    print("\n=== 🎓 Student Record Management ===")
    print("1. Add New Record")
    print("2. View All Records")
    print("3. Search Record by Roll")
    print("4. Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == '1':
        write()
    elif user_choice == '2':
        read()
    elif user_choice == '3':
        search()
    elif user_choice == '4':
        print("👋 Exiting program... Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
