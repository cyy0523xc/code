package main

import (
	"fmt"
)

func main() {
	var myArray [10]int = [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	var mySlice []int = myArray[:5]
	for i, v := range mySlice {
		fmt.Println("element [", i, "] =", v)
	}

	type PersonInfo [3]string
	var myMap map[string]PersonInfo = make(map[string]PersonInfo, 100)
	myMap = map[string]PersonInfo{
		"1234": PersonInfo{"1", "Jack", "Room 101, …"},
	}

	val, ok := myMap["1234"]
	if ok {
		fmt.Println(val)
	}

	val, ok = myMap["a"]
	if ok {
		fmt.Println(val)
	} else {
		fmt.Println("not found")
	}
}
