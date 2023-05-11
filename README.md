

<p align="center">
    <img src="https://s2.loli.net/2023/05/10/LDUpFzo7VJiOshd.png" alt="ChartGPT logo" width=200 height=200 />
</p>
<h1 align="center">ChartGPT</h1>
<p align="center">
    <em>使用自然语言生成Echarts图表</em>
</p>

## How to use

根目录中新建`config.json`文件：

```json
{
    "url": "https://openai.api2d.net/v1/chat/completions",
    "model":"gpt-3.5-turbo",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR-KEY"
    }
}
```

填写`key`与`url`即可，支持api2d，其余参数与openai的api一致。

运行`app.py`即可。

## 参考

感谢

* [wishtodaya/ChartGenie: 一个可以使用自然语言生成图表的网站 ](https://github.com/wishtodaya/ChartGenie)的灵感提供与Prompt参考；

* [skyerhxx/COVID-19_Tracking: 基于Python+Flask+Echarts的疫情爬虫&数据可视化项目]中ajax和flask的数据交互参考；

* API2d：https://api2d.com/r/186769国内稳定的接口调用

感谢今天读的论文很难才导致有闲心和时间把这个东西写出来^_^

## 
