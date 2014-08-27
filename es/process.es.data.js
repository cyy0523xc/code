var aggs = {
    "filter_ym" : {
        "range_division" : {
            "buckets" : [
                {
                "key" : "*-100.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 11071653.99
                        },
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 6363
                    },
                    {
                        "doc_count" : 1420,
                        "sum_sales" : {
                            "value" : 8643627.85
                        },
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "key" : "50-BEVERAGE COFFEE & TEA",
                        "sum_sales" : {
                            "value" : 1039945.05
                        },
                        "doc_count" : 1292
                    },
                    {
                        "doc_count" : 1189,
                        "sum_sales" : {
                            "value" : 205583.7
                        },
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 2451925.41
                        },
                        "doc_count" : 856
                    }
                    ]
                },
                "to" : 100,
                "to_as_string" : "100.0",
                "doc_count" : 11120
            },
            {
                "from" : 100,
                "key" : "100.0-200.0",
                "from_as_string" : "100.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 347,
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 550422.78
                        }
                    },
                    {
                        "doc_count" : 136,
                        "sum_sales" : {
                            "value" : 89163.68
                        },
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 196944.25
                        },
                        "doc_count" : 87
                    },
                    {
                        "doc_count" : 42,
                        "sum_sales" : {
                            "value" : 129424.87
                        },
                        "key" : "40-BEVERAGE BEER"
                    },
                    {
                        "doc_count" : 1,
                        "key" : "50-BEVERAGE COFFEE & TEA",
                        "sum_sales" : {
                            "value" : 320
                        }
                    }
                    ]
                },
                "to_as_string" : "200.0",
                "doc_count" : 613,
                "to" : 200
            },
            {
                "doc_count" : 393,
                "to_as_string" : "300.0",
                "to" : 300,
                "from" : 200,
                "key" : "200.0-300.0",
                "from_as_string" : "200.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "sum_sales" : {
                            "value" : 453910.63
                        },
                        "key" : "30-BEVERAGE WINE",
                        "doc_count" : 206
                    },
                    {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 239636.02
                        },
                        "doc_count" : 86
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 158381.2
                        },
                        "doc_count" : 76
                    },
                    {
                        "doc_count" : 16,
                        "key" : "40-BEVERAGE BEER",
                        "sum_sales" : {
                            "value" : 55171.93
                        }
                    },
                    {
                        "doc_count" : 9,
                        "sum_sales" : {
                            "value" : 5206.72
                        },
                        "key" : "50-BEVERAGE COFFEE & TEA"
                    }
                    ]
                }
            },
            {
                "key" : "300.0-400.0",
                "from" : 300,
                "from_as_string" : "300.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 353,
                        "sum_sales" : {
                            "value" : 971608.35
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 135493.11
                        },
                        "doc_count" : 64
                    },
                    {
                        "sum_sales" : {
                            "value" : 32722.34
                        },
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 28
                    },
                    {
                        "doc_count" : 18,
                        "sum_sales" : {
                            "value" : 21890.36
                        },
                        "key" : "40-BEVERAGE BEER"
                    }
                    ]
                },
                "to" : 400,
                "to_as_string" : "400.0",
                "doc_count" : 463
            },
            {
                "to" : 500,
                "to_as_string" : "500.0",
                "doc_count" : 195,
                "from_as_string" : "400.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 155,
                        "sum_sales" : {
                            "value" : 367440.43
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "sum_sales" : {
                            "value" : 186613.75
                        },
                        "key" : "60-OPEN BEVERAGE",
                        "doc_count" : 38
                    },
                    {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 5762
                        },
                        "doc_count" : 1
                    },
                    {
                        "key" : "40-BEVERAGE BEER",
                        "sum_sales" : {
                            "value" : 497
                        },
                        "doc_count" : 1
                    }
                    ]
                },
                "from" : 400,
                "key" : "400.0-500.0"
            },
            {
                "doc_count" : 66,
                "to_as_string" : "600.0",
                "to" : 600,
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 56,
                        "sum_sales" : {
                            "value" : 139433.22
                        },
                        "key" : "30-BEVERAGE WINE"
                    },
                    {
                        "doc_count" : 7,
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 3782.82
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 10560.87
                        },
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 3
                    }
                    ]
                },
                "from_as_string" : "500.0",
                "key" : "500.0-600.0",
                "from" : 500
            },
            {
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 81946.56
                        },
                        "doc_count" : 47
                    },
                    {
                        "doc_count" : 13,
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 8780.02
                        }
                    },
                    {
                        "sum_sales" : {
                            "value" : 682.07
                        },
                        "key" : "20-BEVERAGE OTHER",
                        "doc_count" : 1
                    }
                    ]
                },
                "from_as_string" : "600.0",
                "from" : 600,
                "key" : "600.0-700.0",
                "to" : 700,
                "to_as_string" : "700.0",
                "doc_count" : 61
            },
            {
                "key" : "700.0-800.0",
                "from" : 700,
                "from_as_string" : "700.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 93594.98
                        },
                        "doc_count" : 22
                    },
                    {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 7200
                        },
                        "doc_count" : 4
                    },
                    {
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 2233
                        },
                        "doc_count" : 3
                    }
                    ]
                },
                "to" : 800,
                "doc_count" : 29,
                "to_as_string" : "800.0"
            },
            {
                "key" : "800.0-900.0",
                "from" : 800,
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 24,
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 50025.95
                        }
                    },
                    {
                        "doc_count" : 6,
                        "sum_sales" : {
                            "value" : 5318
                        },
                        "key" : "60-OPEN BEVERAGE"
                    }
                    ]
                },
                "from_as_string" : "800.0",
                "to" : 900,
                "to_as_string" : "900.0",
                "doc_count" : 30
            },
            {
                "from_as_string" : "900.0",
                "terms_type" : {
                    "buckets" : [
                        {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 93045.37
                        },
                        "doc_count" : 23
                    },
                    {
                        "doc_count" : 8,
                        "key" : "60-OPEN BEVERAGE",
                        "sum_sales" : {
                            "value" : 91493.95
                        }
                    },
                    {
                        "key" : "20-BEVERAGE OTHER",
                        "sum_sales" : {
                            "value" : 1186
                        },
                        "doc_count" : 1
                    }
                    ]
                },
                "key" : "900.0-1000.0",
                "from" : 900,
                "to" : 1000,
                "doc_count" : 32,
                "to_as_string" : "1000.0"
            },
            {
                "terms_type" : {
                    "buckets" : [
                        {
                        "doc_count" : 86,
                        "sum_sales" : {
                            "value" : 328118.94
                        },
                        "key" : "20-BEVERAGE OTHER"
                    },
                    {
                        "key" : "30-BEVERAGE WINE",
                        "sum_sales" : {
                            "value" : 143050.62
                        },
                        "doc_count" : 38
                    },
                    {
                        "doc_count" : 32,
                        "sum_sales" : {
                            "value" : 121277.79
                        },
                        "key" : "60-OPEN BEVERAGE"
                    },
                    {
                        "doc_count" : 1,
                        "sum_sales" : {
                            "value" : 19007.99
                        },
                        "key" : "40-BEVERAGE BEER"
                    }
                    ]
                },
                "from_as_string" : "1000.0",
                "from" : 1000,
                "key" : "1000.0-*",
                "doc_count" : 157
            }
            ]
        },
        "doc_count" : 13159
    }
};

var legend_labels = ['20-BEVERAGE OTHER', '30-BEVERAGE WINE', '40-BEVERAGE BEER', '50-BEVERAGE COFFEE & TEA', '60-OPEN BEVERAGE'];

var aggs_data = aggs.filter_ym.range_division.buckets;

var res = [];
var xAxis = [];

for (var label_i in legend_labels) {
    res[label_i] = [];
}

for (var col_i in aggs_data) {
    var col = aggs_data[col_i];
    xAxis[col_i] = col.key;
    var tmp_data = col.terms_type.buckets;
    var tmp_index = 0;
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

json2str(res);

function json2str(o) {
    var arr = [];
    var fmt = function(s) {
        if (typeof s == 'object' && s != null) return json2str(s);
        return /^(string|number)$/.test(typeof s) ? "'" + s + "'" : s;

    }
    for (var i in o) arr.push("'" + i + "':" + fmt(o[i]));
    return '{' + arr.join(',') + '}';
}

