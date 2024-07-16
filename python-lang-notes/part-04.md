# control flow statments

```python
# a combination of while with else.
# else will execute only if loop ends.
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        print("Breaking out of the loop.")
        break
else:
    print("The while loop has completed without a break.")
```

```python
for i in range(20):
    print(i,end=" ")
    if i == 10:
        break
else:
    # this will execute only if for loop condition fails
    print("end of for loop")
    # now in output you won't see this line.
    # because as break statement will be executed first.
```
