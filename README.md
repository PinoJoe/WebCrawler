# WebCrawler
基础爬虫架构：1）爬虫调度器 ；2）URL管理器；3）HTML下载器；4）HTML解析器；5）数据存储器 

# Scrapy
　　Scrapy是一个用Python写的Crawler Framework，简单轻巧，并且非常方便。Scrapy使用Twisted这个异步网络库来处理网络通信，架构清晰，并且包含了各种中间件接口，可以灵活地完成各种需求。Scrapy整体架构如图所示。
<br><br>
![](https://github.com/PinoJoe/WebCrawler/raw/master/img/Scrapy.png)
<br><br>
　　根据架构图介绍一下Scrapy中的各大组件及其功能：
* Scrapy引擎（Engine）。引擎负责控制流在系统的所有组件中流动，并在相应动作发生时触发事件。
* 调度器（Scheduler）。调度器从引擎接收Request并将它们入队，以便之后引擎请求request时提供给引擎。
* 下载器（Downloader）。下载器负责获取页面数据并提供给引擎，而后提供给Spider。
* Spider。Spider是Scrapy用户编写用于分析Response并提取Item（即获取到的Item）或额外跟进的URL的类。每个Spider负责处理一个特定（或一些）网站。
* Item Pipeline。Item Pipeline负责处理被Spider提取出来的Item。典型的处理有清理验证及持久化（例如存储到数据库中）。
*下载中间件（Downloader middlewares）。下载器中间件是在引擎及下载器之间的特定钩子（specific hook），处理Downloader传递给引擎的Response。其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
*Spider中间件（Spider middlewares）。Spider中间件是在引擎及Spider之间的特定钩子（specific hook），处理Spider的输入（response）和输出（Items及Requests）。其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。<br>
　　一个成熟的爬虫框架包含的也是基础简单爬虫的各个模块。通过数据流的流向，可以清楚地看到Scrapyy的工作流程。Scrapy中的数据流由执行引擎控制，其过程如下：<br>
　　1）引擎打开一个网站（open a domain），找到处理该网站的Spider并向该Spider请求第一个要爬取的URL。<br>
　　2）引擎从Spider中获取到第一个要爬取的URL并通过调度器（Scheduler）以Request进行调度。<br>
　　3）引擎向调度器请求下一个要爬取的URL。<br>
　　4）调度器返回下一个要爬取的URL给引擎，引擎将URL通过下载中间件（请求（request）方向）转发给下载器（Downloader）。<br>
　　5）一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件（返回（response）方向）发送给引擎。<br>
　　6）引擎从下载器中接收到Response并通过Spider中间件（输入方向）发送给Spider处理。<br>
　　7）Spider处理Response并返回爬取到的Item及（跟进的）新的Request给引擎。<br>
　　8）引擎将（Spider返回的）爬取到的ITem给Item Pipeline，将（Spider返回的）Request给调度器。<br>
　　9）（从第二步）重复直到调度器中没有更多的Request，引擎关闭该网站。
