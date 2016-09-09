package main

import (
	"fmt"
	"testing"
)

func getTestFields() []Field {
	conf := &DbConf{
		Host:     "rm-2ze75re47nby5u7mz.mysql.rds.aliyuncs.com",
		Port:     3306,
		UserName: "dsp_sys",
		Password: "Dsp_sys-pwd",
		DbName:   "dsp_sys",
		Charset:  "utf8",
	}

	return descTable(conf, "ad_plan")
}

func _TestDescTable(t *testing.T) {
	table := getTestFields()
	fmt.Println(table)
	fmt.Println(table[0].Field)
}

func TestParseFile(t *testing.T) {
	//fields := getTestFields()
	filename := "./examples/hello/models.go"
	tokens, err := parseFile(filename)
	if err != nil {
		t.Fatal(err)
	}

	fmt.Println(tokens)
}
