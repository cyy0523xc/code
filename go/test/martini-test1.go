package main

import (
	"github.com/go-martini/martini"
	"net/http"
)

func main() {
	m := martini.Classic()
	m.Get("/", func() string {
		return "Hello world!"
	})

	// res 和 req 是通过Martini注入的
	m.Get("/test1", func(res http.ResponseWriter, req *http.Request) {
		res.WriteHeader(200) // HTTP 200
	})

	m.Get("/hello/:name", func(params martini.Params) string {
		return "Hello " + params["name"]
	})

	m.Get("/hello2/**", func(params martini.Params) string {
		return "Hello " + params["_1"]
	})

	m.Get("/hello3/(?P<name>[a-zA-Z]+)", func(params martini.Params) string {
		return fmt.Sprintf("Hello %s", params["name"])
	})
	m.Run()
}
