try:
    number = int(input("Write your number: "))
    print(f"Your number is - {number}")
except ValueError:
    print("Please write number")
