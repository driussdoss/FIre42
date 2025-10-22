get_number = int(input(">"))
# check is it a number or string
if isinstance(get_number, int):
    print("Let's make your number smaller")
    f = get_number + 10
    for get_number in f:
        get_number = get_number - 1
        print(f"Your number is {get_number}")
else:
    print("Give me a number, not string")
