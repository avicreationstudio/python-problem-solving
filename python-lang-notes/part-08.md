# scope of variables in python

```python
# scope in python
# variable scope
# local 
# global


print("start of code")
val = input("input 1:")

def fn():
    # print last element
    li = [ x for x in range(10_00_00_000) ]
    print("the last value",li[-1])
    # The above code will take around 800 MB space.
    # as it is declared inside function.
    # it act as a local variable. So it will consume RAM only on its execution
fn()
# Once function logic is executed. 
# The memory used to run the logic inside function will
# get removed from memory.

val = input("input 2:")
print("end of code")
```

```python
# scope

x = 100

def fn():
 global x
 x = 200
 print('inside fn ',x)

fn()
print("outside fn ",x) # 200
```
