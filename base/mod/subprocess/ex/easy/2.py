#!/usr/bin/env python3

import subprocess

#get stdout - Hello

stdout = subprocess.run(["echo", "Hello"], capture_output=True, text=True)

print(stdout)

