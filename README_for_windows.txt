首先应当安装如下两个依赖
(1)
*
安装python相关依赖: 
windows系统使用文件夹里提供的 python-3.8.0-amd64 文件, 双击该文件以安装
!注意安装之前勾选 ADD python 3.8 to PATH
安装完成之后需要重启电脑
*
(2)
*
安装flask框架:
windows系统使用,需要网络
按下键盘上的 windows键(有些电脑上叫start) 与 R键, 弹出 运行 窗口后, 在栏内输入: cmd, 并点击 确定 按钮
在弹出的终端内输入 pip3 install flask (注意各单词之间有空格), 然后按下 Enter键
等待安装完成即可(安装完成后, 字段里有 successful , 然后显示新的命令行供我们输入)
*

windows系统运行教学
1.按下键盘上的 windows键(有些电脑上叫start) 与 R键, 弹出 运行 窗口后, 在栏内输入: cmd, 并点击 确定 按钮
2.在弹出的终端内输入 python , 先不要按下 Enter键 , 将文件夹里的 index.py 文件拖拽入这个终端
然后使用键盘的 左方向键 将光标移动至 python 之后, 添加上一个空格, 形式效果如下:
python C:\Users\lenovo\Desktop\design\index.py
(以上不同计算机有不同的路径, 只要形式上相同即可)
然后按下 Enter键 运行
3.出现 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 字段即表示成功运行
4.打开浏览器(推荐使用 Google Chrome )
5.在网址栏输入 http://127.0.0.1:5000