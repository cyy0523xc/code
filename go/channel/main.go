package main

import (
	//"fmt"
	"runtime"
	"time"
)

func init() {
	runtime.GOMAXPROCS(runtime.NumCPU())
}

func test1() {
	var c chan int
	c = make(chan int, 1)
	defer close(c)

	var num int
	go step01(c)
	num = <-c
	go step02(c)
	num = <-c
	go step03(c)
	num = <-c
	go step04(c)
	num = <-c
	//fmt.Println(num)
	_ = num
}

func step01(c chan int) {
	//println("step01")
	time.Sleep(time.Millisecond)
	c <- 1
}

func step02(c chan int) {
	//println("step02")
	time.Sleep(time.Millisecond)
	c <- 2
}

func step03(c chan int) {
	//println("step03")
	time.Sleep(time.Millisecond)
	c <- 3
}

func step04(c chan int) {
	//println("step04")
	time.Sleep(time.Millisecond)
	c <- 4
}

func test2() {
	var c int
	c = step11(c)
	c = step12(c)
	c = step13(c)
	c = step14(c)
	//fmt.Println(c)
	_ = c
}

func step11(num int) int {
	//println("step01")
	time.Sleep(time.Millisecond)
	return num + 1
}

func step12(num int) int {
	//println("step02")
	time.Sleep(time.Millisecond)
	return num + 1
}

func step13(num int) int {
	//println("step03")
	time.Sleep(time.Millisecond)
	return num + 1
}

func step14(num int) int {
	//println("step04")
	time.Sleep(time.Millisecond)
	return num + 1
}
