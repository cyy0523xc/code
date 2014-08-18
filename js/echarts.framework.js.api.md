# 基于ECharts的可视化开发框架：js调用可视化对象的接口规范

该规范主要用于js调用可视化对象生成各种图形使用。

### 定制主题

http://echarts.baidu.com/doc/example/themeDesigner.html

### 开发规范

- 引入jquery，ECharts，主题，图形生成基类等js文件
- 在需要显示图形的地方，使用如下代码：

```
<!-- 
deeao-chart: 我们定义的图形标签
chart-type:  【必须】图形类型（如line，bar等），如果有多种类型。
             例如折线图与柱形图混搭，则用逗号分隔，如：bar,bar,line
data-url:    【必须】数据的url接口，图上的数据由该接口返回
onclick:     【可选】onclick事件，例如地图上，点击其中一个省份，则显示具体省份的数据。
-->
<deeao-chart chart-type="line" data-url="/dashboard/ajax_sales_component" onclick="handle_function()">
```

图形生成基类：

- 先查找所有的 *deeao-chart* 标签，解析其中的属性
- 根据 *data-url* 去加载数据，处理异常情况
- 根据 *chart-type* 显示图形

