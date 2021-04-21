package main

import (
	"C"
	"fmt"
	"runtime"
	"sync"
	"time"
)

func Fib(n int) int {
	switch n {
	case 0:
		return 0
	case 1:
		return 1
	case 2:
		return 2
	default:
		return Fib(n-1) + Fib(n-2)
	}
}

func DoTask(wg *sync.WaitGroup) {
	Fib(40)
	// var n = Fib(40)
	// print("n: ", n)
	(*wg).Done()
}

func DoTasks(x, n int) {
	runtime.GOMAXPROCS(x)
	var wg sync.WaitGroup
	start := time.Now()
	for i := 0; i < n; i++ {
		wg.Add(1)
		go DoTask(&wg)
	}

	wg.Wait()
	fmt.Println("DoTasks Time:", time.Since(start))
}

//export DoTasksAPI
func DoTasksAPI(x, n C.int) {
	var start = time.Now()
	DoTasks(int(x), int(n))
	fmt.Println("Time:", time.Since(start))
}

func main() {
	var n int = 40
	var start = time.Now()
	Fib(n)
	fmt.Println("Times 1:", time.Since(start))

	start = time.Now()
	for i := 0; i < 5; i++ {
		Fib(n)
	}
	fmt.Println("Times 5:", time.Since(start))

	DoTasks(4, 12)
}
