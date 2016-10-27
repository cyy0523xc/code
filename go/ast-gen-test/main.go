package main

import (
	"flag"
	"fmt"
	"log"
)

func main() {
	log.SetFlags(0)

	// 命令参数设置
	database := flag.String("d", "", "")
	charset := flag.String("c", "utf8", "")
	username := flag.String("u", "", "")
	password := flag.String("p", "", "")
	host := flag.String("o", "127.0.0.1", "")
	port := flag.Int("r", 3306, "")
	version := flag.Bool("v", false, "")
	help := flag.Bool("h", false, "")
	flag.StringVar(database, "database", "", "")
	flag.StringVar(charset, "charset", "utf8", "")
	flag.StringVar(username, "username", "", "")
	flag.StringVar(password, "password", "", "")
	flag.StringVar(host, "host", "127.0.0.1", "")
	flag.IntVar(port, "port", 3306, "")
	flag.BoolVar(version, "version", false, "")
	flag.BoolVar(help, "help", false, "")
	flag.Usage = func() { log.Println(usageText) } // call on flag error
	flag.Parse()

	if debug {
		fmt.Println("**********************************")
		fmt.Printf("database: %s\n", *database)
		fmt.Printf("charset: %s\n", *charset)
		fmt.Printf("username: %s\n", *username)
		fmt.Printf("password: %s\n", *password)
		fmt.Printf("host: %s\n", *host)
		fmt.Printf("port: %d\n", *port)
		fmt.Println("**********************************")
	}

	if *help {
		// not an error, send to stdout
		// that way people can: scaneo -h | less
		fmt.Println(usageText)
		return
	}

	if *version {
		fmt.Println(versionText)
		return
	}

	files_arr := flag.Args()
	if len(files_arr) != 1 {
		log.Println("Error: 需要一个文件名参数")
		log.Fatal(usageText)
	}

	file := files_arr[0]
	if debug {
		fmt.Printf("input files: %+v\n", file)
	}
}
