# TaoBao-goods-bought
淘宝 已购商品的订单，selenium 模拟登陆，post发送请求获取信息


第一个get_cookies.py 是selenium 模拟登陆，在get_info.py中运行，用于获取cookies。
第二个get_info.py是已购商品的爬虫，主要难点是：翻页为AJAX，而且不是普通的可以通过URL变换看出(像offset=**)


不断点击下一页 可以看出AJAX 是个POST请求，需要提交data。

![image1](https://raw.githubusercontent.com/zhouzheru/TaoBao-goods-bought/master/1.jpg)



![image2](https://raw.githubusercontent.com/zhouzheru/TaoBao-goods-bought/master/2.jpg)
