package main

import (
	"testing"
)

func BenchmarkTest1(b *testing.B) {
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			//test1()
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
	})
}

func BenchmarkTest2(b *testing.B) {
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			//test2()
			var c int
			c = step11(c)
			c = step12(c)
			c = step13(c)
			c = step14(c)
			//fmt.Println(c)
			_ = c
		}
	})
}
