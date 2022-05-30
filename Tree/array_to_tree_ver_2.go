package main

import (
	"fmt"
)

type tree struct {
	value       int
	left, right *tree
}

func main() {
	
	input := []int{3, 4, 2, 6, 1, 5, 7,8,1,2,3,4,67,56,34,23,12,3}

	fmt.Printf("input array: %d\n", input)

	var root *tree

	for _, val := range input {
		root = addToArray(root, val)
	}

	printTree(root)
	
}

func addToArray(root *tree, val int) *tree {

	node := root;
	for node != nil {
		if val < node.value {
			node = node.left
		}else{
			node = node.right
		}	
		node = &tree{value: val}
	}
	
	return root

}

func printTree(root *tree) {

	if root == nil {
		return
	}
	printTree(root.left)
	fmt.Println(root.value)
	printTree(root.right)
}

