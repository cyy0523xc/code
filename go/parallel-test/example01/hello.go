package main

import "github.com/cyy0523xc/code/go/parallel-test"
import "time"

func hello() {
	time.Sleep(time.Second * 60)
	parallel.Hello()
}
