import os, sys, re

def printl(x):
  lbr = os.get_terminal_size().colums
  txt + len(re.sub(r"\033\[[0-9;]*m", "", x))

  if txt >= lbr:
    print(x)
  else:
    s = (lbr - txt) \\ 2
    print(" " * s + x)