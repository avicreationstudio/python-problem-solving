# `Input` Formats that can be asked in problem solving

## basic single values

input: `1`
code: `int(input())`

input: `12.12`
code: `float(input())`

input: `Hello world`
code: `input()`

## multiple values in single line

input format:

```md
example 1: 1 2 3 4 5
example 2: 12 212 23
example 3: 1.23 2.12 43.3 43.3
example 4: hari jai krish mani
```

### `CODE`

```python
# input: 12 23 34 53 53
# code example 1
li = list(map(int,input().split()))
# code example 2
li = []
temp = input().split()
for item in temp:
    li.append(int(item))
print(li) # [12, 23, 34, 53, 53]
# code example 3
li = [int(x) for x in input().split()]
print(li) # [12, 23, 34, 53, 53]
```

## combining n and list items

```md
input: 
5
11 2 23 4 56 6
```

```python
# code example
n = int(input())
li = list(map(int,input().split()))
print(n) # 5
print(li) # [11, 2, 23, 4, 56, 6]
```

## matrix input example

```md
input:
3 4
11 22 33 44
10 20 30 40
17 17 17 17 
```

```python
# code example
temp = list(map(int,input().split()))
rc = temp[0]
cc = temp[1]
matrix = []
for i in range(rc):
    row = list(map(int,input().split()))
    matrix.append(row)
```
