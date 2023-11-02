package main

import "C"
import "fmt"

func add_10(a int64) int64 {
	val := a + 10
	fmt.Println("Adding 10 to the first argument for fun yields")
	fmt.Println(val)
	return val
}

//export Add
func Add(a, b int64) int64 {
	go add_10(a)
	return a + b
}

func main() {}
