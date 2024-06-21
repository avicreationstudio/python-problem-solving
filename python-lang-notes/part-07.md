# HARD example

## comprehension

Whenever we are constructing a list comprehension
there must be only one value before the for

## list flattening -> convert to single list

```python
li = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]
res = []
for row in li:
    for x in row:
        res.append(x)

# list comprehension
res = [ x for row in li for x in row ]
# always start from outer loop
```

```python
# given a list 
# generate a new list with common elements
l1 = [3,7,5,8]
l2 = [7,8,9,10]
res = []
for item in l1:
    if item in l2:
        res.append(item)
# list comprehension
res = [ item for item in l1 if item in l2 ]
```

```python
# create combo of 2 list
l1 = [10,20]
l2 = [0,1]
# condition : pair should not have same combos
res = []
for x in l1:
    for y in l2:
        if x!=y:
            res.append((x,y))
# list comprehension
res = [ (i,j) for x in l1 for y in l2 if x!=j ]
```

```python
# transpose of matrix
matrix = [
    [3,5,10],
    [8,9,13],
    [6,11,14]
]
res = []
for i in range(3):
    temp = []
    for row in matrix:
        temp.append(row[i])
    res.append(temp)
# list comprehension
res = []
for i in range(3):
    temp = [ row[i] for row in matrix ]
    res.append(temp)
# further reduction
res = [[ row[i] for row in matrix ] for i in range(3) ]
# above is example of nested comprehension
```

## dictionary comprehension

```python
li = [1,2,3]
dictionary = { x:x**2 for x in li }
```

## set comprehension

```python
# given a list 
li = [2,3,4,2,4,2,6,3,2]
# generate a new list with square and without duplicates
res = { x**2 for x in li}
# the above one is set comprehension example
```

# tuple comprehension ( return generator object)

```python
li = [3,4,5]
res = ( x**2 for x in li )
print(type(t)) # generator object
print(tuple(res))
```
