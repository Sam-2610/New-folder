import random

while True:
    print("\n1 > Rock\n2 > Paper\n3 > Scissors\n4 > Exit")
    user_input = input("Enter your choice: ")

    if user_input == "4":
        print("Exiting game. Goodbye!")
        break

    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    if user_input not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    user_choice = choices[user_input]
    computer_choice = random.choice(list(choices.values()))

    print(f"\n🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("✅ You Won!")
    else:
        print("💻 Computer Won!")
