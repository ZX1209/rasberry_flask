 // 获取当前 delay 的秒数
var qs = function qs(sel) {return document.querySelector(sel);};
var current = new Date();
var ss = -1 - current.getSeconds();
var ms = ss - current.getMinutes() * 60;
var hs = ms - current.getHours() % 12 * 3600;
// 当前指针的指向角度，用 animation-delay 实现
qs('.hand-second').style.animationDelay = ss + 's';
qs('.hand-minute').style.animationDelay = ms + 's';
qs('.hand-hour').style.animationDelay = hs + 's';