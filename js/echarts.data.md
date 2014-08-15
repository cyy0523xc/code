# echarts的数据格式



### 标准数据格式

```
周一, 周二, 周三, 周四, 周五, 周六, 周日

最高气温 : 
11, 11, 15, 13, 12, 13, 10

最低气温 : 
1, -2, 2, 5, 3, 2, 0

```

折线图和柱形图

### 饼图

```
[
    {value:335, name:'直接访问'},
    {value:310, name:'邮件营销'},
    {value:234, name:'联盟广告'},
    {value:135, name:'视频广告'},
    {value:1548, name:'搜索引擎'}
]
```

嵌套饼图则返回两个这样的数据结构


### 雷达图

```
# 配置
[
    { text: '销售（sales）', max: 6000},
    { text: '管理（Administration）', max: 16000},
    { text: '信息技术（Information Techology）', max: 30000},
    { text: '客服（Customer Support）', max: 38000},
    { text: '研发（Development）', max: 52000},
    { text: '市场（Marketing）', max: 25000}
]

# 值
[
    {
        value : [4300, 10000, 28000, 35000, 50000, 19000],
        name : '预算分配（Allocated Budget）'
    },
    {
        value : [5000, 14000, 28000, 31000, 42000, 21000],
        name : '实际开销（Actual Spending）'
    }
]
```

### 漏斗图

```
[
    {value:100, name:'展现'},
    {value:80, name:'点击'},
    {value:60, name:'访问'},
    {value:40, name:'咨询'},
    {value:20, name:'订单'}
]
```

### 关系网络

```
# 分类
categories : [
    {
        name: '人物'
    },
    {
        name: '家人'
    },
    {
        name:'朋友'
    }
]


# 数据
nodes:[
    {category:0, name: '乔布斯', value : 10},
    {category:1, name: '丽萨-乔布斯',value : 2},
    {category:1, name: '保罗-乔布斯',value : 3},
    {category:1, name: '克拉拉-乔布斯',value : 3},
    {category:1, name: '劳伦-鲍威尔',value : 7},
    {category:2, name: '史蒂夫-沃兹尼艾克',value : 5},
    {category:2, name: '奥巴马',value : 8},
    {category:2, name: '比尔-盖茨',value : 9},
    {category:2, name: '乔纳森-艾夫',value : 4},
    {category:2, name: '蒂姆-库克',value : 4},
    {category:2, name: '龙-韦恩',value : 1},
],
links : [
    {source : '丽萨-乔布斯', target : '乔布斯', weight : 1},
    {source : '保罗-乔布斯', target : '乔布斯', weight : 2},
    {source : '克拉拉-乔布斯', target : '乔布斯', weight : 1},
    {source : '劳伦-鲍威尔', target : '乔布斯', weight : 2},
    {source : '史蒂夫-沃兹尼艾克', target : '乔布斯', weight : 3},
    {source : '奥巴马', target : '乔布斯', weight : 6},
    {source : '比尔-盖茨', target : '乔布斯', weight : 6},
    {source : '乔纳森-艾夫', target : '乔布斯', weight : 1},
    {source : '蒂姆-库克', target : '乔布斯', weight : 1},
    {source : '龙-韦恩', target : '乔布斯', weight : 1},
    {source : '克拉拉-乔布斯', target : '保罗-乔布斯', weight : 1},
    {source : '奥巴马', target : '保罗-乔布斯', weight : 1},
    {source : '奥巴马', target : '克拉拉-乔布斯', weight : 1},
    {source : '奥巴马', target : '劳伦-鲍威尔', weight : 1},
    {source : '奥巴马', target : '史蒂夫-沃兹尼艾克', weight : 1},
    {source : '比尔-盖茨', target : '奥巴马', weight : 6},
    {source : '比尔-盖茨', target : '克拉拉-乔布斯', weight : 1},
    {source : '蒂姆-库克', target : '奥巴马', weight : 1}
]
```

### 散点图

```
女性 : 
161.2, 51.6
167.5, 59
159.5, 49.2
157, 63
155.8, 53.6
170, 59
159.1, 47.6
166, 69.8

男性 : 
174, 65.6
175.3, 71.8
193.5, 80.7
186.5, 72.6
187.2, 78.8
181.5, 74.8
167.6, 64.5
170.2, 77.3
167.6, 72.3
188, 87.3
```

### K线图

```
// 开盘，收盘，最低，最高
[2320.26,2302.6,2287.3,2362.94],
[2300,2291.3,2288.26,2308.38],
[2295.35,2346.5,2295.35,2346.92],
[2347.22,2358.98,2337.35,2363.8]
```






