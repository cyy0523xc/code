package main

const (
	debug = true

	versionText = "goscan v0.1"

	usageText = `GOSQLSCAN
    根据定义从数据库生成定义结构，及Scan方法。生成的文件有两个：tables.go和scans.go.

USAGE
    goscan [options] paths...

OPTIONS
    -d, -database
        数据库名字
    -c, -charset
        数据库的编码，默认为：utf8
    -u, -user
        数据库的用户名
    -p, -password
        数据库密码
    -h, -host
        数据库的host，默认为：127.0.0.1
    -r, -port
        数据库的端口号，默认为：3306
    -v, -version
        Print version and exit.
    -h, -help
        Print help and exit.

EXAMPLES
    goscan -d database_name -u username -p password defile/defile.go
`
)
