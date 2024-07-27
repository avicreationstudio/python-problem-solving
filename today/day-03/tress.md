# Tree data structure

is a specialized data structure to store data in hierarchical manner.

## Parent Node

The node which is a predecessor of a node is called the parent node of that node.

## Child Node

The node which is the immediate successor of a node is called the child node of that node.

## Root Node

The topmost node of a tree or the node which does not have any parent node is called the root node.  

## Leaf Node or External Node

The nodes which do not have any child nodes are called leaf nodes.

## Ancestor of a Node

Any predecessor nodes on the path of the root to that node are called Ancestors of that node.

## Descendant

A node x is a descendant of another node y if and only if y is an ancestor of x.

## Sibling

Children of the same parent node are called siblings.

## Level of a node

The count of edges on the path from the root node to that node. The root node has level 0.

## Subtree

Any node of the tree along with its descendant.
Eg. left sub tree / right sub tree.

Types of trees
---------------

[] based on no of children

1. binary tree  : left and right child
2. ternary tree : left, mid, right child
3. n-ary tree   : many children at every node

[] Special types of trees

1. Binary search tree
2. AVL tree
...

[] Binary tree types based on count

1. Full binary tree    : node has 0 or 2 node
2. Degenerate Binary tree : node has one child (ll)
3. Skewed Binary tree     :
   - left-skewed binary tree
   - right-skewed binary tree

[] Binary Tree Types basis of levels

1. complete binary tree

    - A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible.
    - A complete binary tree is just like a full binary tree, but with two major differences:
      - Every level except the last level must be completely filled.
      - All the leaf elements must lean towards the left.
      - The last leaf element might not have a right sibling i.e. a complete binary tree doesn’t have to be a full binary tree.

2. perfect binary tree
    A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level. 
3. balanced binary tree
    eg: AVL tree
    depth = height(left) - height(right) 

-------------------------------------------------

binary tree traversal

- pre order
- in order
- post order
- no of nodes
- level order
- level order level
- zig zag
- left and right view

