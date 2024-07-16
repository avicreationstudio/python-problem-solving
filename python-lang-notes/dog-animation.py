
import time 
eyes = "0-"
dog = r"""
  |\_|\
_/ {0} {0} |   
| ^    | ____ /
\_____./    |/
  | __ ___  |
  |/ |/  ||/
"""
for i in range(100):
    time.sleep(0.5)
    print(dog.format(eyes[i%2]))
