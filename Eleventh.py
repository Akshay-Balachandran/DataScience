try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error reading file 1.txt:", e)
try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error reading file 2.txt:", e)
try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error reading file 3.txt:", e)


print("Thanks for using the file reader!")  # Confirmation message
