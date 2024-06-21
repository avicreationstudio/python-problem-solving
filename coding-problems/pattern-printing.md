# 🏷️ PATTERN PRINTING 🏷️

## BASICS


```python
# base code
n =  5
for i in range(n):
    for j in range(n):
        print("{}{}".format(i,j),end=" ")
    print()
```

    00 01 02 03 04 
    10 11 12 13 14 
    20 21 22 23 24 
    30 31 32 33 34 
    40 41 42 43 44 
    


```python
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j==0:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * * 
    *         
    *         
    *         
    *         
    


```python
# other version of code. alternate version of using `or`
n = 5
for i in range(n):
    for j in range(n):
        if i in [0,n//2,n-1] or j in [0,n//2,n-1]:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * * 
    *   *   * 
    * * * * * 
    *   *   * 
    * * * * * 
    


```python
# other version of code. alternate version of using `or`
n = 5
for i in range(n-1):
    for j in range(n):
        if i+j >= n-1 and j==n-1-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i >= j and j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("* "*n + "* "*(n-1))
```

            *         
          *   *       
        *       *     
      *           *   
    * * * * * * * * * 
    


```python
n = 5
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    *         
      *       
        *     
          *   
            * 
    


```python
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    *         
    * *       
    * * *     
    * * * *   
    * * * * * 
    


```python
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * * 
      * * * * 
        * * * 
          * * 
            * 
    


```python
n = 5
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

            * 
          *   
        *     
      *       
    *         
    


```python
n = 5
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
    


```python
n = 5
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * * 
    * * * *   
    * * *     
    * *       
    *         
    


```python

```


```python

```

## all basic triangle pattern


```python
# *           |   1           |   A
# * *         |   1 2         |   A B
# * * *       |   1 2 3       |   A B C
# * * * *     |   1 2 3 4     |   A B C D
# * * * * *   |   1 2 3 4 5   |   A B C D E
```

```python
#         *    |            1    |            A
#       * *    |          1 2    |          A B
#     * * *    |        1 2 3    |        A B C
#   * * * *    |      1 2 3 4    |      A B C D
# * * * * *    |    1 2 3 4 5    |    A B C D E
```

```python
#          *           |           1           |           A
#        * * *         |         1 2 3         |         A B C
#      * * * * *       |       1 2 3 4 5       |       A B C D E
#    * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
#  * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
```

```python
# * * * * *   |   1 2 3 4 5   |   A B C D E 
# * * * *     |   1 2 3 4     |   A B C D
# * * *       |   1 2 3       |   A B C
# * *         |   1 2         |   A B
# *           |   1           |   A
```

```python
# * * * * *    |    1 2 3 4 5    |    A B C D E
#   * * * *    |      1 2 3 4    |      A B C D
#     * * *    |        1 2 3    |        A B C
#       * *    |          1 2    |          A B
#         *    |            1    |            A
```

```python
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
#   * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
#     * * * * *       |       1 2 3 4 5       |       A B C D E
#       * * *         |         1 2 3         |         A B C
#         *           |           1           |           A
```

```python
#         *           |           1           |           A
#       * * *         |         1 2 3         |         A B C
#     * * * * *       |       1 2 3 4 5       |       A B C D E
#   * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
#   * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
#     * * * * *       |       1 2 3 4 5       |       A B C D E
#       * * *         |         1 2 3         |         A B C
#         *           |           1           |           A
```

```python
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
#   * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
#     * * * * *       |       1 2 3 4 5       |       A B C D E
#       * * *         |         1 2 3         |         A B C 
#         *           |           1           |           A
#       * * *         |         1 2 3         |         A B C
#     * * * * *       |       1 2 3 4 5       |       A B C D E
#   * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
```

```python
# * * * * *   |   1 2 3 4 5   |   A B C D E
# *       *   |   1       5   |   A       E
# *       *   |   1       5   |   A       E
# *       *   |   1       5   |   A       E
# * * * * *   |   1 2 3 4 5   |   A B C D E
```

`pending`

```python
#         *           |           1           |           A
#       *   *         |         1   3         |         A   C
#     *       *       |       1       5       |       A       E
#   *           *     |     1           7     |     A           G
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
```

```python
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
#   *           *     |     1           7     |     A           G
#     *       *       |       1       5       |       A       E
#       *   *         |         1   3         |         A   C
#         *           |           1           |           A
```

```python
#         *           |           *           |           A
#       *   *         |         *   *         |         A   C
#     *       *       |       *       *       |       A       E
#   *           *     |     *           *     |     A           G
# *               *   |   *               *   |   A               I
#   *           *     |     *           *     |     A           G
#     *       *       |       *       *       |       A       E
#       *   *         |         *   *         |         A   C
#         *           |           *           |           A
```

```python
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9    |   A B C D E F G H I
#   *           *     |     1           7      |     A           G
#     *       *       |       1       5        |       A       E
#       *   *         |         1   3          |         A   C
#         *           |           1            |           A
#       *   *         |         1   3          |         A   C
#     *       *       |       1       5        |       A       E
#   *           *     |     1           7      |     A           G
# * * * * * * * * *   |   1 2 3 4 5 6 7 8 9    |   A B C D E F G H I
```

```python
# 1          |   A
# 2 3        |   B C
# 4 5 6      |   D E F
# 7 8 9 10   |   G H I J
```

`pending`

```python
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 
```

`pending`

```python
#     * * * * *   |       1 2 3 4 5   |       A B C D E
#    * * * * *    |      1 2 3 4 5    |      A B C D E
#   * * * * *     |     1 2 3 4 5     |     A B C D E
#  * * * * *      |    1 2 3 4 5      |    A B C D E
# * * * * *       |   1 2 3 4 5       |   A B C D E
```


---

## Pattern problem 01

    *           |   1           |   A
    * *         |   1 2         |   A B
    * * *       |   1 2 3       |   A B C
    * * * *     |   1 2 3 4     |   A B C D
    * * * * *   |   1 2 3 4 5   |   A B C D E


```python
# basic pattern printing
```


```python
# easy version
n = 5
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# other options
# -----------------------------
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
# -----------------------------
for i in range(n):
    print("* "*(i+1))
# ------------------------------
```

    *         
    * *       
    * * *     
    * * * *   
    * * * * * 
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    


```python
# numbers combination
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
# ----------------------------
print() # just to give new line nothing special

for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
# ----------------------------
print() # just to give new line nothing special

count = 1
for i in range(n):
    for j in range(i+1):
        print("{:>2}".format(count),end=" ")
        count += 1
    print()
# ----------------------------
print() # just to give new line nothing special

# char A
ascii_A = ord("A")
count = 0
for i in range(n):
    for j in range(i+1):
        print(chr(ascii_A + count),end=" ")
        count += 1
    print()
# ----------------------------
print() # just to give new line nothing special

# char A
ascii_A = ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(ascii_A+j),end=" ")
    print()
```

    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
    
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5 
    
     1 
     2  3 
     4  5  6 
     7  8  9 10 
    11 12 13 14 15 
    
    A 
    B C 
    D E F 
    G H I J 
    K L M N O 
    
    A 
    A B 
    A B C 
    A B C D 
    A B C D E 
    


```python

```

---

## Pattern problem 02

            *    |            1    |            A
          * *    |          1 2    |          A B
        * * *    |        1 2 3    |        A B C
      * * * *    |      1 2 3 4    |      A B C D
    * * * * *    |    1 2 3 4 5    |    A B C D E

---

## Pattern problem 03

    #          *           |           1           |           A
    #        * * *         |         1 2 3         |         A B C
    #      * * * * *       |       1 2 3 4 5       |       A B C D E
    #    * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
    #  * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I


```python
# easy version
n = 5
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# -----------------------------
for i in range(n):
    print("  "*(n-i-1) + "* "*(i+1) + "* "*(i+1-1))
# ------------------------------
```

            *         
          * * *       
        * * * * *     
      * * * * * * *   
    * * * * * * * * * 
            * 
          * * * 
        * * * * * 
      * * * * * * * 
    * * * * * * * * * 
    


```python
# easy version
n = 5
for i in range(n):
    count = 1
    for j in range(n):
        if i+j>=n-1:
            print(count,end=" ")
            count += 1
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i>=j:
            print(count,end=" ")
            count += 1
        else:
            print(" ",end=" ")
    print()
```

            1         
          1 2 3       
        1 2 3 4 5     
      1 2 3 4 5 6 7   
    1 2 3 4 5 6 7 8 9 
    


```python
# easy version
n = 5
ascii_A = ord("A")
for i in range(n):
    count = 0
    for j in range(n):
        if i+j>=n-1:
            print(chr(ascii_A + count),end=" ")
            count += 1
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i>=j:
            print(chr(ascii_A + count),end=" ")
            count += 1
        else:
            print(" ",end=" ")
    print()
```

            A         
          A B C       
        A B C D E     
      A B C D E F G   
    A B C D E F G H I 
    


```python

```

---

## Pattern problem 04

    # * * * * * * * * *   |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
    #   * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
    #     * * * * *       |       1 2 3 4 5       |       A B C D E
    #       * * *         |         1 2 3         |         A B C
    #         *           |           1           |           A


```python
# easy version
n = 5
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i+j<=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# other options
# -----------------------------
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(1,n-i):
        print("*",end=" ")
    print()
# -----------------------------
for i in range(n):
    print("  "*(i) + "* "*(n-i) + "* "*(n-i-1))
# ------------------------------
```

    * * * * * * * * * 
      * * * * * * *   
        * * * * *     
          * * *       
            *         
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            * 
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            * 
    


```python
# easy version
n = 5
for i in range(n):
    count = 1
    for j in range(n):
        if i<=j:
            print(count,end=" ")
            count+=1
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i+j<=n-1:
            print(count,end=" ")
            count+=1
        else:
            print(" ",end=" ")

    print()
# alphabet printing
n = 5
ascii_A = ord("A")
n = 5
for i in range(n):
    count = 0
    for j in range(n):
        if i<=j:
            print(chr(ascii_A +count),end=" ")
            count+=1
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i+j<=n-1:
            print(chr(ascii_A +count),end=" ")
            count+=1
        else:
            print(" ",end=" ")
    print()
```

    1 2 3 4 5 6 7 8 9 
      1 2 3 4 5 6 7   
        1 2 3 4 5     
          1 2 3       
            1         
    A B C D E F G H I 
      A B C D E F G   
        A B C D E     
          A B C       
            A         
    


```python

```
