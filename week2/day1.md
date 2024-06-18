# topics

## `int`

different types of number representation available in python
they are

1. (2)  binary     :  eg, 0b1010 or 0B1010
1. (8)  octal      :  eg, 0o8 or 0O8
1. (10) decimal    :  eg, 24
1. (16) hexadecimal:  eg, 0xA or 0XB

note:

```python
>>> a = 000012
#  ? ---> will show error
#  because as in int datatype 0 is used to represent number system.
#  we can't use leading zeros in int type.
```

store numbers using underscore `_`=

eg:

```python
>>> fees = 2_00_000
>>> val = 0b1100_1100
>>> a = 0_00000_1
# error
>>> a = 0_0
# 0
```

## float

- number system only works with int
- not with float type

`>>> a = 123`

```python
>>> a = 12.23
>>> a = 000000000122.0
>>> a = 000000_00_0122.0
>>> .0
>>> 0.
>>> 12e2.1 # default to float and cant use power as float
```

# bool

- bool type is actually inherited from int type

```python
>>> True + True * True / (False+1)
# 2.0
```

# complex

```python
 # complex numbers
val = 12 + 12.90j
# as a real number, we can use int, float, bool
# as a imaginary number, we can only use float
print(val)
print(val.real)
print(val.imag)
# output
# (12+12.9j)
# 12.0
# 12.9
>>> a = (2+2j)*(2+2j)
>>> a.imag
>>> a = 100
>>> a = True

```
