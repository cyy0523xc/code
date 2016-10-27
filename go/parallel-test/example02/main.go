package main

import "github.com/cyy0523xc/code/go/parallel-test"
import "time"

func main() {
	parallel.Hello()
	time.Sleep(time.Second * 60)
}
