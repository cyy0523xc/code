package main

import (
	"errors"
	"os"
	"strings"
	"text/template"
)

// 生成文件
func genFile(out_file, pkg string, unexport bool, toks []structToken) error {
	if len(toks) < 1 {
		return errors.New("no structs found")
	}

	fout, err := os.Create(out_file)
	if err != nil {
		return err
	}
	defer fout.Close()

	data := struct {
		PackageName string
		Tokens      []structToken
		Visibility  string
	}{
		PackageName: pkg,
		Visibility:  "S",
		Tokens:      toks,
	}

	if unexport {
		// func name will be scanFoo instead of ScanFoo
		data.Visibility = "s"
	}

	fnMap := template.FuncMap{"title": strings.Title}
	tmpl, err := template.New("scans").Funcs(fnMap).Parse(tempText)
	if err != nil {
		return err
	}

	if err := tmpl.Execute(fout, data); err != nil {
		return err
	}

	return nil
}
