count = 0

while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        print("Breaking out of the loop.")
        break
else:
    print("The while loop has completed without a break.")