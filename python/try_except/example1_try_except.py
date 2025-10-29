#!/usr/bin/env python3

#number check

try:
    num = int(input("Give me num buddy: "))
    print(f"Your number: {num}")
except ValueError:
    print("You don't give me number")

