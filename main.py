import kivy
'''盒子管理器'''
from kivy.uix.boxlayout import BoxLayout
'''窗口'''
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

# 检查版本
kivy.require('1.0.6')

# APP界面，继承APP父类
class Interface(App):
    # 返回根组件
    def build(self):
        return Builder.load_file(
            "/Users/jean/Desktop/python项目实战/CommunicationApplication/controls/widget.kv"
        )
    
    def add_friends(self):
        pass























if __name__ == '__main__':
    Interface().run()