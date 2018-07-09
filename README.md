# rasberry_flask
falsk run -h 0.0.0.0 -p 


# 
首先，数字信号和模拟信号都可以作为电源来输出，，
两者的输出的电压取决与输入的电压也就是vcc　接了多少
但是，一般的模拟信号向数值（arudino 模拟信号口读入）的转换都是以０－５ｖ映射到０－１０２４上的

数字信号没有实验过，但是我想还是一样的．．或许是用电平表示０，１也说不一定呢．．．




# todos
[*] 温度模块测试成功，有点麻烦啊．．．这个．．
    主要是有１s的延迟呢．．．
    arduino getTemplate() return 'C 值．．．
-  土壤,水泵,旋钮模块的基本逻辑构成(基本智能花盆api层)
- 总信息页面...

- 警报装置 探索

- 再购买一些传感器...??

- 报告...

[*] 测试　土壤湿度模块
    输出范围０～１０２４　插在一般的土壤中是８００多
    插在湿润的土壤中一般３５０多．．
[*] 测试　水泵
    3.3v 红接电源　黑接地
[*] arduino 与 树莓派的连接通讯
    python serial lib

[*] 基本信息界面...
    树莓派 post json 数据(json.dumps(),requests)
    服务器端,直接request.get_json(force=True)
    真是方便呢...
    

- 内网穿透
    现阶段,,是树莓派单方面传数据给服务器

[*] 等待快递...

[*] fix zh input problem in rasberry pi
    使用google pingxin scitm
- link sui and tu
    有点危险呢...
[*] use request to tran message to server side
[*] build the info page fo this project in server
    基本完成 info.html

- 树莓派 模拟信号 输入输出
