    /**
     * 替换所有匹配exp的字符串为指定字符串
     * @param exp 被替换部分的正则
     * @param newStr 替换成的字符串
     */
    String.prototype.replaceAll = function (exp, newStr) {
        return this.replace(new RegExp(exp, "gm"), newStr);
    };

    /**
     * 原型：字符串格式化
     * @param args 格式化参数值
     */
    String.prototype.format = function(args) {
        var result = this;
        if (arguments.length < 1) {
            return result;
        }

        var data = arguments; // 如果模板参数是数组
        if (arguments.length == 1 && typeof (args) == "object") {
            // 如果模板参数是对象
            data = args;
        }
        for ( var key in data) {
            var value = data[key];
            if (undefined != value) {
                result = result.replaceAll("\\{" + key + "\\}", value);
            }
        }
        return result;
    }


    function genBg(n)
    {
        var fdeg = 217+n;
        var sdeg = 127+n;
        var tdeg = 336+n;
        var template = "linear-gradient({0}deg, rgba(255,0,0,.8), rgba(255,0,0,0) 70.71%),linear-gradient({1}deg, rgba(0,255,0,.8), rgba(0,255,0,0) 70.71%),linear-gradient({2}deg, rgba(0,0,255,.8), rgba(0,0,255,0) 70.71%);"

        return template.format(fdeg,sdeg,tdeg)
    }
    var flag = 0

    function changeBg()
    {
        if(flag>350)
        {
            flag=0;
        }
        else{
            flag+=1;
        }
        n = flag
        var b = b = document.getElementsByTagName('body')[0]
        b.style.cssText  = "background:"+genBg(n)
    }
