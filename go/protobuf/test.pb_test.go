package example

import (
	"fmt"
	"testing"

	"github.com/golang/protobuf/proto"
)

func TestHello(t *testing.T) {
	test := &Test{
		Label: "0123456789",
		Type:  17,
		Reps:  1,
		Hello: 7,
	}
	data, err := proto.Marshal(test)
	fmt.Println(len(data))
	if err != nil {
		t.Fatal(err)
	}
	newTest := &Test{}
	err = proto.Unmarshal(data, newTest)
	if err != nil {
		t.Fatal(err)
	}

	fmt.Println(newTest)
	fmt.Println(newTest.Type)
	fmt.Println(newTest.Hello)
}
