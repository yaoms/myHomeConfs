#!/usr/bin/env python
# coding: utf-8

# example base.py

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    #clicked信号的回调函数
    def hello(self,widget,data):
        print 'hello %s this is a button clicked() test' % data

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title('测试机器人 PyGTK 版 0.1')
        #self.window.set_default_size(200,200)
        #self.window.set_border_width(100)
	#设置窗口的delete_event信号触发delete_event函数
        self.window.connect("delete_event", self.delete_event)
        #设置窗口的destroy信号触发destroy函数
        self.window.connect("destroy",self.destroy)
        #控制窗口出现的位置
        self.window.set_position(gtk.WIN_POS_CENTER)

        #设置一个不可见的横向的栏位self.box1
        self.box = gtk.HBox(True, 0)
        #把box1放到窗口中
        self.window.add(self.box)

	self.addButton('hello', self.hello)

        self.box.show()
        self.window.show()

    #destroy信号的回调函数
    def destroy(self,widget,data=None):
        gtk.main_quit()

    #添加按钮
    def addButton(self,title,action,data="PyGTK"):
        #生成按钮实例
        button = gtk.Button()
        button.set_label(title)
        button.connect('clicked',action,data)
        self.box.pack_start(button,True,True,0)
        button.show()
        

    #delete_event事件的回调函数
    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        #如果delete_event事件返回假，则会触发destroy信号，从而关闭窗口。
        #如果返回真，则不会关闭窗口。这个特性在当我们需要一个确认是否退出的选择对话框时是很有用。
        return False

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
