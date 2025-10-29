#!/usr/bin/env python3


import subprocess

#get return code

answer = subprocess.run(["pwd"])

print(answer.returncode)
