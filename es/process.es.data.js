// 处理es的结果集
// @author Alex

var aggs = {
    "filter_ym" : {
        "range_division" : {
            "buckets" : [
                {
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 9414,
                        "sum_sales" : {
                            "value" : 16352798.71
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 12285225.43
                        },
                        "doc_count" : 2161,
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "sum_sales" : {
                            "value" : 1374046.71
                        },
                        "doc_count" : 1447,
                        "key" : "50-BEVERAGE COFFEE & TEA"
                    },
                    {
                        "doc_count" : 1256,
                        "sum_sales" : {
                            "value" : 3664399.71
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 1029,
                        "sum_sales" : {
                            "value" : 233416.18
                        }
                    }
                    ]
                },
                "doc_count" : 15307,
                "to_as_string" : "100.0",
                "to" : 100,
                "key" : "*-100.0"
            },
            {
                "from" : 100,
                "key" : "100.0-200.0",
                "to" : 200,
                "from_as_string" : "100.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 495,
                        "sum_sales" : {
                            "value" : 784990.74
                        },
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 92591.93
                        },
                        "doc_count" : 146
                    },
                    {
                        "sum_sales" : {
                            "value" : 227173.95
                        },
                        "doc_count" : 124,
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "doc_count" : 86,
                        "sum_sales" : {
                            "value" : 281261.78
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 1005
                        },
                        "doc_count" : 4,
                        "key" : "50-BEVERAGE COFFEE & TEA"
                    }
                    ]
                },
                "doc_count" : 855,
                "to_as_string" : "200.0"
            },
            {
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 278,
                        "sum_sales" : {
                            "value" : 633476.74
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "sum_sales" : {
                            "value" : 441299.74
                        },
                        "doc_count" : 128,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "sum_sales" : {
                            "value" : 336581.64
                        },
                        "doc_count" : 93,
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "sum_sales" : {
                            "value" : 37058.65
                        },
                        "doc_count" : 18
                    },
                    {
                        "key" : "50-BEVERAGE COFFEE & TEA",
                        "doc_count" : 9,
                        "sum_sales" : {
                            "value" : 7803.6
                        }
                    }
                    ]
                },
                "doc_count" : 526,
                "from_as_string" : "200.0",
                "to_as_string" : "300.0",
                "from" : 200,
                "to" : 300,
                "key" : "200.0-300.0"
            },
            {
                "from" : 300,
                "to" : 400,
                "key" : "300.0-400.0",
                "from_as_string" : "300.0",
                "doc_count" : 704,
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 1387427.68
                        },
                        "doc_count" : 529
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 105,
                        "sum_sales" : {
                            "value" : 547677.14
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 45428.55
                        },
                        "doc_count" : 38,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "doc_count" : 32,
                        "sum_sales" : {
                            "value" : 35299.34
                        },
                        "key" : "40-BEVERAGE BEER"
                    }
                    ]
                },
                "to_as_string" : "400.0"
            },
            {
                "to" : 500,
                "key" : "400.0-500.0",
                "from" : 400,
                "to_as_string" : "500.0",
                "from_as_string" : "400.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 533529.52
                        },
                        "doc_count" : 239
                    },
                    {
                        "sum_sales" : {
                            "value" : 227077.14
                        },
                        "doc_count" : 71,
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "doc_count" : 6,
                        "sum_sales" : {
                            "value" : 8216.76
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 43509.5
                        },
                        "doc_count" : 4,
                        "key" : "20-BEVERAGE OTHER"
                    }
                    ]
                },
                "doc_count" : 320
            },
            {
                "to" : 600,
                "key" : "500.0-600.0",
                "from" : 500,
                "to_as_string" : "600.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 87,
                        "sum_sales" : {
                            "value" : 118519.17
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "sum_sales" : {
                            "value" : 553575.82
                        },
                        "doc_count" : 21,
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 17500
                        },
                        "doc_count" : 3
                    },
                    {
                        "sum_sales" : {
                            "value" : 657.8
                        },
                        "doc_count" : 1,
                        "key" : "40-BEVERAGE BEER"
                    }
                    ]
                },
                "doc_count" : 112,
                "from_as_string" : "500.0"
            },
            {
                "from" : 600,
                "key" : "600.0-700.0",
                "to" : 700,
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "doc_count" : 58,
                        "sum_sales" : {
                            "value" : 80945.09
                        }
                    },
                    {
                        "doc_count" : 13,
                        "sum_sales" : {
                            "value" : 10742.76
                        },
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                },
                "doc_count" : 71,
                "from_as_string" : "600.0",
                "to_as_string" : "700.0"
            },
            {
                "from_as_string" : "700.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 89017.47
                        },
                        "doc_count" : 37,
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "sum_sales" : {
                            "value" : 223422
                        },
                        "doc_count" : 8,
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "doc_count" : 3,
                        "sum_sales" : {
                            "value" : 3825
                        },
                        "key" : "20-BEVERAGE OTHER"
                    }
                    ]
                },
                "doc_count" : 48,
                "to_as_string" : "800.0",
                "from" : 700,
                "key" : "700.0-800.0",
                "to" : 800
            },
            {
                "to" : 900,
                "key" : "800.0-900.0",
                "from" : 800,
                "to_as_string" : "900.0",
                "from_as_string" : "800.0",
                "doc_count" : 45,
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 32,
                        "sum_sales" : {
                            "value" : 60797.17
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "sum_sales" : {
                            "value" : 16197.35
                        },
                        "doc_count" : 13,
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                }
            },
            {
                "doc_count" : 48,
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 166573.33
                        },
                        "doc_count" : 43
                    },
                    {
                        "sum_sales" : {
                            "value" : 11976
                        },
                        "doc_count" : 3,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 2134
                        },
                        "doc_count" : 2
                    }
                    ]
                },
                "from_as_string" : "900.0",
                "to_as_string" : "1000.0",
                "from" : 900,
                "key" : "900.0-1000.0",
                "to" : 1000
            },
            {
                "from_as_string" : "1000.0",
                "doc_count" : 224,
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 92,
                        "sum_sales" : {
                            "value" : 699151.74
                        }
                    },
                    {
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 77,
                        "sum_sales" : {
                            "value" : 318493.98
                        }
                    },
                    {
                        "doc_count" : 55,
                        "sum_sales" : {
                            "value" : 208335.19
                        },
                        "key" : "30-BEVERAGE WINE"
                    }
                    ]
                },
                "key" : "1000.0-*",
                "from" : 1000
            }
            ]
        },
        "doc_count" : 18260
    }
};

var legend_labels = ['20-BEVERAGE OTHER', '30-BEVERAGE WINE', '40-BEVERAGE BEER', '50-BEVERAGE COFFEE & TEA', '60-OPEN BEVERAGE'];

var aggs_data = aggs.filter_ym.range_division.buckets;

var res = [];
var xAxis = [];

// 结果数组初始化
for (var label_i in legend_labels) {
    res[label_i] = [];
}

// 处理aggs data
for (var col_i in aggs_data) {
    var col = aggs_data[col_i];
    var tmp_data = col.terms_type.buckets;
    var tmp_index = 0;
    xAxis[col_i] = col.key;

    for (var label_i in legend_labels) {
        res[tmp_index][col_i] = 0;
        for (var col_item_i in tmp_data) {
            var col_item = tmp_data[col_item_i];
            if (col_item.key == legend_labels[label_i]) {
                res[tmp_index][col_i] = col_item.sum_sales.value;
            }
        }

        tmp_index++;
    }
}

json2str(xAxis);
json2str(res);

// 输出json字符串
function json2str(o) {
    var arr = [];
    var fmt = function(s) {
        if (typeof s == 'object' && s != null) return json2str(s);
        return s;
        //return /^(string|number)$/.test(typeof s) ? "'" + s + "'" : s;
    }

    for (var i in o) arr.push(fmt(o[i]));
    return '[' + arr.join(',') + ']';
}

