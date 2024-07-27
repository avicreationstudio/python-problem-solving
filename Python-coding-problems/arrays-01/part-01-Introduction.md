# Time and Space Complexity

## TIME complexity

Time complexity refers to the amount of time an algorithm takes to complete as a function of the size of the input.
Its not about time taken, but is about growth rate of algorithm.

It is typically expressed using Big O notation,
which describes the upper bound of the algorithm's running time.

In simple term we can say, time complexity is not about amount of time taken, But it is about growth rate.

### Big O Notation Examples

|notation  |type  |desc  |example  |
|---------|---------|---------|---------|
|O(1)  |     Constant time    |     the running time does not depend on the size of the input.     |   a formula, sum on n numbers      |
|O(n)     |     Linear time    |       the running time grows linearly with the input size.   |    find a element in an array     |
|O(n^2)     |    Quadratic time     |      the running time grows quadratically with the input size.    |      bubble sorting   |
|O(log n)     |    Logarithmic time     |      the running time grows logarithmically with the input size.    |     binary search    |
|O(n log n)     |      Linearithmic time   |     the running time grows in proportion to n log n.     |   merge sort      |

## SPACE complexity

Space complexity refers to the amount of memory an algorithm uses in relation to the size of the input.
Extra amount of space required to run a program.

### Array

- The space complexity of an array is O(n) because we need space to store n elements.

### Linked List

- The space complexity of a linked list is also O(n) for storing n elements, but additional space is required for pointers.
- For a singly linked list, each node contains data and a pointer to the next node.

## over all example

### Bubble Sort

Time Complexity
---

In the worst case, bubble sort has a time complexity of O(n^2) because it involves nested loops that compare and swap adjacent elements.
cpp

Space Complexity
---

Bubble sort has a space complexity of O(1) because it only uses a constant amount of extra space for the temporary variable during swaps.

```c++
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

```

![](https://he-s3.s3.amazonaws.com/media/uploads/ece920b.png)

<!-- ## most cases we will be using vector over array -->

<!-- ### Arrays

- `Fixed Size:`Arrays have a fixed size that is determined at https://he-s3.s3.amazonaws.com/media/uploads/ece920b.pngcompile time and cannot be changed during runtime.
- `Static Allocation:` Memory for arrays is allocated statically (on the stack or globally) or dynamically (on the heap using new).
- `Direct Access:` Elements in an array are accessed using index notation ([]). Array indices start from 0.
- `No Built-in Size Tracking:` Arrays do not store information about their size internally, so the programmer must keep track of the size separately.
- `No Dynamic Resizing:`Once defined, the size of an array cannot be changed. To resize an array, a new array must be allocated and elements copied over.
- `Simple Syntax:`Arrays are simpler in syntax and initialization compared to vectors.

### Vectors

- `Dynamic Size:` Vectors can dynamically resize themselves during runtime to accommodate varying numbers of elements.
- `Dynamic Allocation:`Memory for vectors is allocated dynamically on the heap. Vectors manage their own memory allocation and deallocation.
- `Direct Access:`Like arrays, elements in vectors are accessed using index notation ([]). Vector indices also start from 0.
- `Size Tracking:`Vectors store their current size internally, so you can retrieve the size of a vector using the size() member function.
- `Dynamic Resizing:`Vectors support dynamic resizing using operations like push_back(), pop_back(), resize(), etc., which allows them to grow or shrink as needed.
- `Versatility:`Vectors are more versatile than arrays in terms of functionality and can be passed to functions more easily (as they carry their size with them). -->

### PRE-REQUISITE

- Array
- stack
- queue
- HashTable

python concepts

- function scope
- class basics
