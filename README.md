

<p align="center">
    <img src="https://s2.loli.net/2023/05/10/LDUpFzo7VJiOshd.png" alt="ChartGPT logo" width=200 height=200 />
</p>
<h1 align="center">ChartGPT</h1>
<p align="center">
    <em>使用自然语言生成Echarts图表</em>
</p>

## What it does

[ChartGPT](https://charts-gpt.vercel.app/)可以让你用自然语言描述生成ECharts图表。得益于国产大模型的价格优势，现在已可以免费使用QWen2.5-7B即可实现以前ChatGPT-3.5都做不到的效果：


![demo](./demo.gif)

## How to use

### 开发
开发前新建.env文件：
```bash
URL_BASE=https://api.siliconflow.cn/v1/chat/completions

MODEL=Qwen/Qwen2.5-Coder-7B-Instruct

API_KEY=YOUR_API_KEY
```
然后：

```bash
bash ./local_dev.sh
```

然后就可以运行主程序：

```python
python app.py
```
### 部署
使用Vercel部署。根目录中新建`.env`文件：

```
API_KEY= "sk-xxxxxxxx" # 填入自己的API key

MODEL = "Qwen/Qwen2.5-Coder-7B-Instruct"

URL_BASE = "https://api.siliconflow.cn/v1/chat/completions"

```

部署时记得导入.env到vercel里面。你可以用不同语言来描述你的需求：

1.创建一个折线图，横坐标['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']，纵坐标 [150, 230, 224, 218, 135, 147, 260] 

2.创建一个雷达图，数据 为[4200, 3000, 20000, 35000, 50000, 18000]，分别对应[Sales，Administration，Information Technology，Customer Support，Development,Marketing] 这几项内容

3.创建一个K线图，横坐标 ['2017-10-24', '2017-10-25', '2017-10-26', '2017-10-27']，纵坐标[[20, 34, 10, 38],[40, 35, 30, 50],[31, 38, 33, 44],[38, 15, 5, 42]]


## 参考

感谢

* [wishtodaya/ChartGenie: 一个可以使用自然语言生成图表的网站 ](https://github.com/wishtodaya/ChartGenie)的灵感提供与Prompt参考；

* [skyerhxx/COVID-19_Tracking: 基于Python+Flask+Echarts的疫情爬虫&数据可视化项目](https://github.com/skyerhxx/COVID-19_Tracking)中ajax和flask的数据交互参考；

* [Siliconflow](https://cloud.siliconflow.cn/) 中稳定可靠的API调用。
