import os, time

def run(x):
  for i in x + "\n":
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1/100)