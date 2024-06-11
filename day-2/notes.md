# operators and data types

## operators precedence and associativity

|precedence  |    operator  |associativity  |
|-------|---------|---------|
|1      |     ()    |      L-R   |
|2      |    x[index], x[index:index]     | L-R        |
|3      |   **      | R-L         |
|4      |     +x, -x, ~x     ( bitwise )    | R-L         |
|5      |   *, /, //, %      |      L-R    |
|6      |   +,-      |          L-R|
|7      |    <<,>>     |         L-R |
|8      |      (bitwise and)   |     L-R     |
|9      |      (bitwise xor)   | L-R         |
|10     |      (bitwise or)   |     L-R     |
|11     |    in, not in, is, is not, <, <=, >, >=, !=, ==     |  L-R       |
|12     |  not       |     R-L     |
|13     |     and    |      L-R    |
|14     |       or  |      L-R    |
|15     |   if else ( conditional expression )      |    R-L     |
|16     |   :=      |R-L         |  

## list of operators

- =
  - a,b = 1,2
- arithmetic operator
- +,- ( addition and subtraction )
- *, / ( divition ), // ( floor division ), % ( modulus )
  - `2+3+5`
  - `2+3*5`
- **

### `most use cases of modulus`

- get remaining values
  - in 100 seconds , we can say 1 minutes and remaining  40 seconds there.
  - how to get this 40 remaining seconds.
  - `100//60` -> 1
  - `100%60`  -> 40
- get last digit

```python
>>> 1234 % 10  # 4
>>> 1234 // 10 # 123
>>> 123 % 10   # 3
>>> 123 // 10  # 12
>>> 12 % 10    # 2
```

- repeat an index value within its limit

```python
>>> li = [ 10, 20, 30 ]
>>> n = len(li) # 3
>>> i = 0
>>> li[ i%n ] # 0%3
>>> i = i + 1
>>> li[ i%n ] # 1%3
>>> i = i + 1
>>> li[ i%n ] # 2%3
>>> i = i + 1
>>> li[ i%n ] # 3%3
>>> i = i + 1
>>> li[ i%n ] # 4%3
>>> i = i + 1
```

---
🙀 EXTRA : 🙀

```python
>>> a = 5%2 # 
>>> a = -5%2 # 
>>> a = 5%-2 # 
>>> a = -5%-2 # 
```

`🏷️ will be covered at end of class`

---

### `Exponent operator ( ** )`

- usage is purely on maths.
- find square root and cube root

```python
>>> 2**3   #
>>> 2**1   #
>>> 2**-1  #
>>> 2**0.5 # 
```

`usage`

- square root
- cube root
  - math.ceil
  - math.floor

---
🙀 EXTRA : 🙀

```python
>>>  -3**2
```

- why in python we use # for comments
- why not `//` for comments

`🏷️ will be covered at end of class`

---

### `Data types`

```md
     Data types
       /      \
  Numberic    string datatype
  /                \
int               str
float
bool
complex     
```

- Numeric type basics is enough for problem solving
- In case of strings
  - usage of single, double and triple quotes
  - freq used method is : `.format()`
  - and `.split()` which is used while getting input values.
  - `"hello"*3` for multiplying strings.

```python
>>> print("Hello my name is {}.".format('doremon'))
```

---

### `comparison/relational operators`

- `==` Equal To
- `! =` Not Equal To
- `>` Greater Than
- `<` Less Than
- `>=` Greater Than or Equal To
- `<=`  Lesser Than or Equal To

`NOTE: make sure you understand your relation`

### `logical operators`

- `and`
- `or`
- `not`

---
