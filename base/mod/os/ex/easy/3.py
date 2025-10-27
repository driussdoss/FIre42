#!/usr/bin/env python3
import os

#make dir log

os.makedirs("./logs", exist_ok=True)
os.chdir("./logs")
print(os.getcwd())
