print("\n=== Monthly Budget Tracker ===\n")

categories = {
    "Food": 0,
    "Rent": 0,
    "Transport": 0,
    "Entertainment": 0,
    "Clothes": 0
}

while True:
    try:
        budget = int(input("Enter your monthly budget: $"))
        if budget < 0:
            print("Budget can't be negative!")
            continue

        for category in categories:
            categories[category] = int(input(f"How much did you spend on {category.lower()}? $"))
            if categories[category] < 0:
                print("Expenses can't be negative!")
                break
        else:
            break
    except ValueError:
        print("Please enter a valid number!\n")

print("\n=== Your Expenses ===")
print(f"Budget: ${budget}\n")

total = sum(categories.values())

for category, amount in categories.items():
    if budget != 0:
        percentage = (amount / budget) * 100
    else:
        percentage = 0
    print(f"{category}: ${amount} ({percentage:.1f}%)")

print("\n=== Summary ===")
print(f"Total spent: ${total}")
print(f"Remaining: ${budget - total}")

if budget > 0:
    print(f"Budget usage: {total / budget * 100:.1f}%")