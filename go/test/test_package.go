package testPackage

func Hello(str string) {
	println("in Hello")
	return "hello" + str
}

func test(str string) {
	println("in test")
	return "this is a test = " + str
}
