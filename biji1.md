# 我的python笔记
- python无需编译链接 只需要python解释器
- print(单双引号都行)2版本有无括号都行3必须加括号
- 命令行一般用来测试句子正确性
- print的东西中含有中文时 需在代码头加入#coding=utf-8
- 变量可以有字母，下划线，数字，但是不能由数字开头
- python区分大小写
- print输出变量，括号中变量位置使用%s 双引号外面使用%（变量名）
例如  print ("xingming: %s xuexiao：%s  "%(name,xuexiao))
- %s用来替换字符串，%d用来替换整数
- 加法和乘法都可以用于字符串的操作
- if 和 else 写完后都要加冒号 if 后面接多个相应语句时，一定要对齐
  if-elif-else
- print默认自动换行 后面加逗号为不换行
- input 输入函数，得到的类型不仅是字符串
- 定义类属性的时候，如果想让属性私有化需要在属性定义时加两个下划线
  在调用该属性的时候需要自己写一个内部方法给外部提供一个接口
- 私有函数定义方式类似  
- self用法类似于C++中this， 谁调用就是谁
- 类的构造函数参数（self,***,***）在类的构造函数中定义的变量自动变成属性