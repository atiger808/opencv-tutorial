// 面向对象
// 1. 添加属性
// 通过this关键字， 绑定属性， 并且指定它的值
// 2. 添加方法
// 在Banner.prototype上绑定方法可以了
// 原型链 Banner.prototype.greet = function(){}  绑定方法
//
// function Banner() {
//     // 这里写的代码
//     // 相对于python中的__init__方法
//     console.log("init 构造函数")
//     // 添加属性用this关键字， 代表当前对象
//     this.person = '张三'
// }
//
// Banner.prototype.greet = function(word){
//     console.log('hello, ', word)
// }
//
// banner = new Banner();
// console.log(banner.person)
// banner.greet('李四')
//--------------------------------------------------------------------

function Banner(){

}

Banner.prototype.run = function () {
    var bannerUL = $("#banner-ul");
    // bannerUL.css({"left": (-798)*1})
    var index = 0;
    setInterval(function () {
        if(index>=3){
            index=0
        }else{
            index += 1
        }

        bannerUL.animate({"left": -798*index}, 500)
    }, 2000);
};

$(function () {
    var banner = new Banner()
    banner.run()
})