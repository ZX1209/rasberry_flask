server ip 159.89.155.162 
# 平常不开...

# 
首先，数字信号和模拟信号都可以作为电源来输出，，
两者的输出的电压取决与输入的电压也就是vcc　接了多少
但是，一般的模拟信号向数值（arudino 模拟信号口读入）的转换都是以０－５ｖ映射到０－１０２４上的

数字信号没有实验过，但是我想还是一样的．．或许是用电平表示０，１也说不一定呢．．．




# todos
- 语音识别与播报...
    这...
- 水循环
    主要是浇水是虽然会有一定的水往下漏,但是会掺着杂质,可能对水泵造成影响呢..
    
    直接浇水或者是间接加水

- 树莓派或者是server建一个数据库?

- 警报装置 探索

- 再购买一些传感器...??

- 报告...

- 内网穿透
    现阶段,,是树莓派单方面传数据给服务器

[*] arduino 树莓派,双向通讯与控制...
    嗯..
    首先,由于温度信息提取有一定延迟,timeout最好设置为 2s
    其次,arduino接受的信息是bytes,python的话要把unicode字符转换为bytes类型(b'')
    read 的各种问题...

- 总信息页面...
    明天吧..
[*] 测试完LED灯珠,有源,无源蜂鸣器,光强传感器,温度传感器(无法转换),倾斜传感器,霍尔开关传感器
    DS18b20线性温度传感器,
    还有些,难以观测的部件,火焰,干簧管等传感器...
[*] 温度模块测试成功，有点麻烦啊．．．这个．．
    主要是有１s的延迟呢．．．
    arduino getTemplate() return 'C 值．．．
[*]  土壤,水泵,旋钮模块的基本逻辑构成(基本智能花盆api层)
    现在准备拆了重组...

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
    


[*] 等待快递...

[*] fix zh input problem in rasberry pi
    使用google pingxin scitm
- link sui and tu
    有点危险呢...
[*] use request to tran message to server side
[*] build the info page fo this project in server
    基本完成 info.html

- 树莓派 模拟信号 输入输出
