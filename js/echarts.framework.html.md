# 基于ECharts的可视化开发框架：使用规范

该规范主要用于js调用可视化对象生成各种图形使用。

### 定制主题

http://echarts.baidu.com/doc/example/themeDesigner.html

我们可以形成几套不同风格的主题，具体项目根据需要进行选择。

### 开发规范

- 引入jquery，ECharts，主题，图形生成基类等js文件
- 在需要显示图形的地方，使用如下代码：

```
<!-- 
deeao-chart: 我们定义的图形标签
chart-type:  【必须】图形类型（如line，bar等），如果有多种类型。
             例如折线图与柱形图混搭，则用逗号分隔，如：bar,bar,line
data-url:    【必须】数据的url接口，图上的数据由该接口返回
             url接口规范见：echarts.framework.md
width:       【必须】宽度
height:      【必须】高度
title:       【可选】标题
onclick:     【可选】onclick事件，例如地图上，点击其中一个省份，则显示具体省份的数据。
-->
<deeao-chart chart-type="line" data-url="/dashboard/ajax_sales_component" width="100" height="100" title="图形标题" onclick="handle_function()">
</deeao-chart>
```

### 图形生成基类

这个类是框架最关键的部分，追求的目标：友好，健壮，易用，易扩展。处理的主要功能：

- 先查找所有的 *deeao-chart* 标签，解析其中的属性
- 根据 *data-url* 去加载数据，处理异常情况
- 数据开始加载时候，可以预先显示提示：数据正在拼命加载中...
- 如果数据加载异常或者出错，显示一个数据加载异常的提示
- 根据 *chart-type* 显示图形

具体项目并不会直接使用该基类，而是使用它的子类。这个子类的作用就是实现一些项目特有的扩展。
尽可能减少需要在子类的处理，通用的东西在基类应该都已经实现了。



