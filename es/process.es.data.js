// 处理es的结果集
// @author Alex

var aggs = {
    "filter_ym" : {
        "doc_count" : 18260,
        "range_division" : {
            "buckets" : [
                {
                "to" : 50,
                "key" : "*-50.0",
                "to_as_string" : "50.0",
                "doc_count" : 6368,
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 3917233.43
                        },
                        "doc_count" : 3610,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 460138.13
                        },
                        "doc_count" : 258
                    },
                    {
                        "doc_count" : 808,
                        "sum_sales" : {
                            "value" : 1752127.39
                        },
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "key" : "50-BEVERAGE COFFEE & TEA",
                        "doc_count" : 1310,
                        "sum_sales" : {
                            "value" : 1171568.2
                        }
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 55457.75
                        },
                        "doc_count" : 382
                    }
                    ]
                }
            },
            {
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 5804,
                        "sum_sales" : {
                            "value" : 12435565.28
                        },
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 3204261.58
                        },
                        "doc_count" : 998
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "sum_sales" : {
                            "value" : 10533098.04
                        },
                        "doc_count" : 1353
                    },
                    {
                        "key" : "50-BEVERAGE COFFEE & TEA",
                        "doc_count" : 137,
                        "sum_sales" : {
                            "value" : 202478.51
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 177958.43
                        },
                        "doc_count" : 647,
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                },
                "from_as_string" : "50.0",
                "from" : 50,
                "doc_count" : 8939,
                "to" : 100,
                "key" : "50.0-100.0",
                "to_as_string" : "100.0"
            },
            {
                "from_as_string" : "100.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 498760.74
                        },
                        "doc_count" : 352,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "sum_sales" : {
                            "value" : 123540
                        },
                        "doc_count" : 103,
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "sum_sales" : {
                            "value" : 249478.87
                        },
                        "doc_count" : 58
                    },
                    {
                        "key" : "50-BEVERAGE COFFEE & TEA",
                        "sum_sales" : {
                            "value" : 1005
                        },
                        "doc_count" : 4
                    },
                    {
                        "sum_sales" : {
                            "value" : 71245.27
                        },
                        "doc_count" : 85,
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                },
                "from" : 100,
                "doc_count" : 602,
                "key" : "100.0-150.0",
                "to" : 150,
                "to_as_string" : "150.0"
            },
            {
                "to_as_string" : "200.0",
                "key" : "150.0-200.0",
                "to" : 200,
                "doc_count" : 253,
                "from" : 150,
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 286230
                        },
                        "doc_count" : 143
                    },
                    {
                        "doc_count" : 21,
                        "sum_sales" : {
                            "value" : 103633.95
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "doc_count" : 28,
                        "sum_sales" : {
                            "value" : 31782.91
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 21346.66
                        },
                        "doc_count" : 61,
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                },
                "from_as_string" : "150.0"
            },
            {
                "from_as_string" : "200.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 72,
                        "sum_sales" : {
                            "value" : 370905.46
                        },
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 34834.06
                        },
                        "doc_count" : 56
                    },
                    {
                        "sum_sales" : {
                            "value" : 15411.33
                        },
                        "doc_count" : 11,
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 43,
                        "sum_sales" : {
                            "value" : 97015.41
                        }
                    }
                    ]
                },
                "doc_count" : 182,
                "from" : 200,
                "to_as_string" : "250.0",
                "key" : "200.0-250.0",
                "to" : 250
            },
            {
                "from" : 250,
                "doc_count" : 344,
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 70394.28
                        },
                        "doc_count" : 56,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 598642.68
                        },
                        "doc_count" : 222
                    },
                    {
                        "sum_sales" : {
                            "value" : 21647.32
                        },
                        "doc_count" : 7,
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "doc_count" : 9,
                        "sum_sales" : {
                            "value" : 7803.6
                        },
                        "key" : "50-BEVERAGE COFFEE & TEA"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 50,
                        "sum_sales" : {
                            "value" : 239566.23
                        }
                    }
                    ]
                },
                "from_as_string" : "250.0",
                "to" : 300,
                "key" : "250.0-300.0",
                "to_as_string" : "300.0"
            },
            {
                "from_as_string" : "300.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 33069.26
                        },
                        "doc_count" : 24,
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 582715.37
                        },
                        "doc_count" : 263
                    },
                    {
                        "sum_sales" : {
                            "value" : 3570.67
                        },
                        "doc_count" : 6,
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 57,
                        "sum_sales" : {
                            "value" : 244902.12
                        }
                    }
                    ]
                },
                "doc_count" : 350,
                "from" : 300,
                "to_as_string" : "350.0",
                "key" : "300.0-350.0",
                "to" : 350
            },
            {
                "key" : "350.0-400.0",
                "to" : 400,
                "to_as_string" : "400.0",
                "from" : 350,
                "doc_count" : 354,
                "from_as_string" : "350.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 14,
                        "sum_sales" : {
                            "value" : 12359.29
                        }
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "doc_count" : 266,
                        "sum_sales" : {
                            "value" : 804712.31
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 31728.67
                        },
                        "doc_count" : 26,
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "doc_count" : 48,
                        "sum_sales" : {
                            "value" : 302775.02
                        },
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                }
            },
            {
                "to" : 450,
                "key" : "400.0-450.0",
                "to_as_string" : "450.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 4,
                        "sum_sales" : {
                            "value" : 43509.5
                        },
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "doc_count" : 116,
                        "sum_sales" : {
                            "value" : 264559.94
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 212081.64
                        },
                        "doc_count" : 51,
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                },
                "from_as_string" : "400.0",
                "from" : 400,
                "doc_count" : 171
            },
            {
                "to_as_string" : "500.0",
                "to" : 500,
                "key" : "450.0-500.0",
                "doc_count" : 149,
                "from" : 450,
                "from_as_string" : "450.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "doc_count" : 123,
                        "sum_sales" : {
                            "value" : 268969.58
                        }
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "sum_sales" : {
                            "value" : 8216.76
                        },
                        "doc_count" : 6
                    },
                    {
                        "doc_count" : 20,
                        "sum_sales" : {
                            "value" : 14995.5
                        },
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                }
            },
            {
                "key" : "500.0-*",
                "from" : 500,
                "doc_count" : 548,
                "from_as_string" : "500.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 351794.98
                        },
                        "doc_count" : 86
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 724187.42
                        },
                        "doc_count" : 312
                    },
                    {
                        "sum_sales" : {
                            "value" : 657.8
                        },
                        "doc_count" : 1,
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "sum_sales" : {
                            "value" : 1505223.67
                        },
                        "doc_count" : 149,
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                }
            }
            ]
        }
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

