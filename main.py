import kivy
'''盒子管理器'''
from kivy.uix.boxlayout import BoxLayout
'''窗口'''
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.app import App

# 检查版本
kivy.require('1.0.6')

# APP界面，继承APP父类
class Interface(App):
    # 返回根组件
    def build(self):
        return AppWeight()


class AppWeight(BoxLayout):

    # 返回根控件，用于定义不同区域的布局管理
    def __init__(self):
        super().__init__()
        # 垂直布局
        layout = BoxLayout(orientation='vertical')
        # 基本控件绘制
        with self.canvas.before:
            # 窗口大小(仅限桌面级app)
            Window.size = (350,800)
            # 窗口底色(RGB)
            Window.clearcolor = (1,1,1,1)




























if __name__ == '__main__':
    Interface().run()