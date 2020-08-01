#!/usr/bin/evn python3

import subprocess

interface = input("what's your os  linux give sudo , termux give enter ==>")

os = input("what's your os  linux give -framework , termux give enter ==>")

subprocess.call(interface +  " apt install unstable-repo", shell=True)

subprocess.call(interface +  " apt install metasploit" + os , shell=True)

subprocess.call("msfconsole", shell=True)