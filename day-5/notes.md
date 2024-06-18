# theory

## ternary operator

conditional operator

- `max_val = a if a>b else b`
- if condition is true then max_val = a else max_val = b

nesting if else

```python
a,b,c = 12,2,12
max_val = a if a>b and a>c else b if b>a and b>c else c 

a,b,c,d = 12,2,12,2
res = a if a>b and a>c and a>d else b if b>a and b>c and b>d else c if c>a and c>b and c>d else d
```

`NOTE: the above code will follow R->L associativity`

## flow control

1. while
1. for
1. break, continue
1. match case

### `while`

| Feature                   | `for` Loop                                  | `while` Loop                                 |
|---------------------------|---------------------------------------------|----------------------------------------------|
| **Purpose**               | Iterates over a sequence (e.g., list, tuple, string) | Repeats as long as a condition is true       |
| **Syntax**                | `for item in sequence:`                     | `while condition:`                           |
| **Use Case**              | When the number of iterations is known or finite | When the number of iterations is not known or is dependent on a condition |
| **Initialization**        | Automatically takes the first item from the sequence | Must initialize variables before the loop    |
| **Condition**             | Implicitly checks for the end of the sequence | Explicit condition is checked each iteration |
| **Iteration**             | Automatically moves to the next item in the sequence | Must manually update variables within the loop |
| **Example**               | `for i in range(5):`<br>`print(i)`      | `i = 0`<br>`while i < 5:`<br>`print(i)`<br>`i += 1` |
| **Break and Continue**    | Supports `break` and `continue` statements  | Supports `break` and `continue` statements   |
| **Readability**           | Often more readable for simple iterations   | May be less readable if the condition or updates are complex |

```python
# the basic concept of while
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("The while loop has completed without a break.")

# --------------------------------------------------------------

count = 0

while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        print("Breaking out of the loop.")
        break
else:
    print("The while loop has completed without a break.")

# --------------------------------------------------------------

s1 = "BYTS"
n = len(s1)
i = 0
while i<n:
    print(s[i])
    i = i + 1

```

### `for`

```python

li = [1,2,3,4,5]
for x in li:
    print(x)

# ------------------------------------------------------

li = [1,2,3,4,5]

for i in range(len(li)):
    print(li[i])

# ------------------------------------------------------
my_list = ['apple', 'banana', 'cherry', 'date']

# Using enumerate to get index and item
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")
# ------------------------------------------------------

```

### `match case`

```python
# program to find exam grading system

grade = input() # A B C D E 

def fn(grade):
    match grade:
        case "A":
            print("very good")    
        case "B":
            print("good")
        case "C":
            print("average")
        case "D":
            print("below average")
        case "E":
            print("poor")
        case _:
            print("invalid grade")
 
```

## function

### `built in function`

- print, input, range
- usage of range function
  - syntax -> `range(x,y,z)`
  - `list(range(x,y,z))`
  - `sum()` `min()` `max()`

### `user defined function`

we can create our own function

```python
def fn(x,y,z):  # func definition  ( arguments )
    pass
fn(10,20,30)       # func call        ( parameters)
```

---

calling function within function

```python
def fn1():
    print("inside fn1 start")
    print("inside fn1 end")

def fn2():
    print("inside fn2 start")
    fn1()
    print("inside fn2 end")

fn1()
fn2()
```

why to use functions

```python
a,b = 10,20
c = a+b

a,b = 12,26
c = a+b

a,b = 2,20
c = a+b

# make a code reusable
def add(a,b):
    return a+b

res = add(10,20)
print(res)
```

### return

```python

def fn1():
    return 10

val = fn1()
print(val)

def fn2():
    return 10,20

a,b = fn2()
print(a,b)

```

## lambda

to use short representation of funtion

```python
def add(a,b):
    return a+b

res = add(10,20)
print(res)

# convert to lambda


```

## bitwise operator

1. AND (&)
The bitwise AND operation compares each bit of two numbers and returns 1 if both bits are 1, otherwise it returns 0.

```python
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

result = a & b  # (binary: 0001)
print(result)   # Output: 1
```

2. OR (|)
The bitwise OR operation compares each bit of two numbers and returns 1 if at least one of the bits is 1, otherwise it returns 0.

```python
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

result = a | b  # (binary: 0111)
print(result)   # Output: 7
```

3. XOR (^)
The bitwise XOR operation compares each bit of two numbers and returns 1 if only one of the bits is 1, otherwise it returns 0.

```python
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

result = a ^ b  # (binary: 0110)
print(result)   # Output: 6
```

4. NOT (~)
The bitwise NOT operation flips all the bits of a number, turning 1s into 0s and 0s into 1s. This is also known as the bitwise complement.

```python
a = 5  # (binary: 0101)

result = ~a  # (binary: 1010, which is -6 in decimal due to two's complement representation)
print(result)  # Output: -6

```

5. Left Shift (<<)
The left shift operation shifts all the bits of a number to the left by a specified number of positions. This is equivalent to multiplying the number by 2 raised to the power of the number of positions shifted.

```python
a = 5  # (binary: 0101)

result = a << 1  # (binary: 1010)
print(result)    # Output: 10

```

6. Right Shift (>>)
The right shift operation shifts all the bits of a number to the right by a specified number of positions. This is equivalent to dividing the number by 2 raised to the power of the number of positions shifted, discarding any remainder.

```python
a = 5  # (binary: 0101)

result = a >> 1  # (binary: 0010)
print(result)    # Output: 2
```

| Operation    | Symbol | Description                                      | Example                      | Result       |
|--------------|--------|--------------------------------------------------|------------------------------|--------------|
| AND          | `&`    | Bits that are 1 in both operands                 | `5 & 3`  (0101 & 0011)       | `1` (0001)   |
| OR           | `|`    | Bits that are 1 in at least one operand          | `5 | 3`  (0101 | 0011)       | `7` (0111)   |
| XOR          | `^`    | Bits that are 1 in one operand but not both      | `5 ^ 3`  (0101 ^ 0011)       | `6` (0110)   |
| NOT          | `~`    | Bits that are flipped                            | `~5`  (~0101)                | `-6` (1010)  |
| Left Shift   | `<<`   | Shifts bits to the left, filling with 0s         | `5 << 1` (0101 << 1)         | `10` (1010)  |
| Right Shift  | `>>`   | Shifts bits to the right, discarding shifted bits| `5 >> 1` (0101 >> 1)         | `2` (0010)   |
