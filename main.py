from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.image import Image as ComcoreImage
from kivy.uix.floatlayout import FloatLayout

# 确保版本
kivy_version = "2.1.0"


class Widget(FloatLayout):
    def __init__(self):
        super().__init__()
        pass

    def loading_file(self):
        pass


# App入口
class Interface(App):
    def __init__(self):
        super().__init__()
        self.title = "Communication Application"
        # 设置窗口大小
        Window.size = (400, 800)
        # 设置窗口颜色RGB(white Color)
        Window.clearcolor = (1, 1, 1, 1)

    # 返回根控件
    def build(self):
        # 加载kv文件
        Builder.load_file(
            "/Users/jean/Desktop/python项目实战/CommunicationApplication/controls/widget.kv"
        )
        return Widget()


if __name__ == "__main__":
    Interface().run()
