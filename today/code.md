```python

t1 = "ace"
t2 = "abcde"
```


```python
import prettytable as pt 

def display(matrix):
    p = pt.PrettyTable()
    for row in matrix:
        p.add_row(row)
    print(p)
```


```python
dp = []
for i in range(len(t1) + 1):
    temp = []
    for j in range(len(t2) + 1):
        temp.append(0)
    dp.append(temp)
```


```python
display(dp)
```

    +---------+---------+---------+---------+---------+---------+
    | Field 1 | Field 2 | Field 3 | Field 4 | Field 5 | Field 6 |
    +---------+---------+---------+---------+---------+---------+
    |    0    |    0    |    0    |    0    |    0    |    0    |
    |    0    |    0    |    0    |    0    |    0    |    0    |
    |    0    |    0    |    0    |    0    |    0    |    0    |
    |    0    |    0    |    0    |    0    |    0    |    0    |
    +---------+---------+---------+---------+---------+---------+
    


```python
for i in range(1, len(t1) + 1):
    for j in range(1, len(t2) + 1):
        if t1[i-1] == t2[j-1]:
            dp[i][j] =  dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
output = dp[len(t1)][len(t2)]
output
```




    3




```python
display(dp)
```

    +---------+---------+---------+---------+---------+---------+
    | Field 1 | Field 2 | Field 3 | Field 4 | Field 5 | Field 6 |
    +---------+---------+---------+---------+---------+---------+
    |    0    |    0    |    0    |    0    |    0    |    0    |
    |    0    |    1    |    1    |    1    |    1    |    1    |
    |    0    |    1    |    1    |    2    |    2    |    2    |
    |    0    |    1    |    1    |    2    |    2    |    3    |
    +---------+---------+---------+---------+---------+---------+
    


```python

```


```python

```
