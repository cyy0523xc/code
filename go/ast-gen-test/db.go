package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

type DbConf struct {
	Host     string
	Port     int
	DbName   string
	UserName string
	Password string
	Charset  string
}

type Field struct {
	Field   string
	Type    string
	Null    string
	Default sql.NullString
}

func descTable(conf *DbConf, table_name string) []Field {
	// Open database connection
	conn_string := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s", conf.UserName, conf.Password, conf.Host, conf.Port, conf.DbName)

	db, err := sql.Open("mysql", conn_string)
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	// Execute the query
	rows, err := db.Query("desc " + table_name)
	if err != nil {
		panic(err.Error())
	}
	defer rows.Close()

	var tmp sql.NullString
	tables := []Field{}
	for rows.Next() {
		f := Field{}
		err = rows.Scan(&f.Field, &f.Type, &f.Null, &tmp, &f.Default, &tmp)
		if err != nil {
			panic(err.Error())
		}

		tables = append(tables, f)
	}

	return tables
}
