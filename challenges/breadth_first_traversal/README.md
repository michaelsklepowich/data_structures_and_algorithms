# Breadth First Traversal

## Problem Domain:
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach; print every visited node’s value.

## Set up
import both the tree and node class so that the breadth_first_traversal function has valid input.

## Logic
The walk function in this traversal method takes an array of nodes and if any of the elements of that array are NOT NULL, then recursively call the walk function on the children of all elements until all nodes have been visited. The output list is then returned.