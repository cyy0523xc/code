package parallel

import "fmt"
import "time"

func init() {
	timer := time.NewTicker(time.Second * 5)
	for {
		select {
		case <-timer.C:
			fmt.Println(time.Now().Format("2006-01-02 03:04:05"))
			time.Sleep(time.Second)
		}
	}
}

func Hello() {
	fmt.Println("======>")
}
