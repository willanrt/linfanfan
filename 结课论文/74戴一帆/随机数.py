import random
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
# QtCore 模块是非 GUI 的核心库。这个模块用来处理时间、文件、目录、各种类型的数据、流（stream）、URLs，mime 类型、线程和进程
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
#QtWidgets 有创建经典风格的用户界面的类。基础小组件位于 PyQt6.QtWidgets 模块

#from modules import *
#from widgets import *
#import os
#os.environ["QT_FONT_DPI"] = "96"
#对高DPI设置的支持----模块缺失

class MainWindow(QMainWindow):
#Qt中的顶层窗口称为MainWindow，属于类QMainWindow，QMainWindow也是继承于QWidget。通过子类化QMainWindow可以创建一个应用程序的窗口。MainWindow的结构分为五个部分：菜单栏（Menu Bar）、工具栏（Toolbars）、停靠窗口（Dock Widgets）、状态栏（Status Bar）和中央窗口（Central Widget）
#class mainwindow(qmainwindow):
    #def __init__(self, parent=none):
    #super(mainwindow, self).__init__(parent)
    #self.init_ui()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("随机数(整数)生成器")  # 设置应用程序标题
        # 设置图标
        self.setWindowIcon(QIcon("D:/Users/f1241/Desktop/python/python进阶/作业/结课论文/74戴一帆/aisland_reed.png"))
        self.setFixedSize(QSize(350, 400))  # 设置应用程序窗口的固定大小
        self.num_label_start = "随机数: "
        self.number_label = QLabel()  # 显示随机生成的数字的大小的标签
        #QLabel继承自 QFrame。QLabel 用于显示文本或图像且不提供用户交互功能，标签的视觉外观可以以各种方式配置
        self.button = QPushButton("生成随机数!")  # QPushButton小部件提供了一个命令按钮
        # 事件绑定（self.button.clicked.connect），首先点击按钮调用函数, 函数执行发送信号操作, 信号对应的槽函数实现窗口关闭的效果
        self.button.clicked.connect(self.generate_number)

        self.default_min, self.default_max = self.min, self.max = 0, 100 #设置随机数默认大小范围
        self.min_head = QLabel("限制最小值为:")
        self.min_input = QLineEdit()
        self.min_start = "最小值: "
        self.min_confirm = QPushButton("设置最小值")
        self.min_confirm.setEnabled(False)
        '''
        工作中有时候经常会遇到控制按钮是否可点击的时候，setEnabled() 和 setClickable() 都可以做到，只要将它们设置成false ，按钮就不可点击，设置成true，按钮就可以点击。

        它们的区别在于：setClickable():设置成true时，按钮为可点击，设置为false时，按钮不可点击，不能响应点击事件，但此时如果setEnabled()为true，那么按钮即使不可点击（setClickable()为false），也会产生变化（一闪一闪）。

        setEnabled():设置成true时，相当于激活了按钮，按钮的状态不再是死的，而是会对触摸或者点击产生反应，并且可以响应一些触发事件。而设置成false时，按钮是灰色的，无论是否可点击（即使将setClickable()设置成true），都无法响应任何触发事件。

        其实区别就在上面说的几个小地方，总的来看，setEnabled()相当于总开关，控制着按钮的状态，而setClickable()相当于具体的某个开关，控制这个开关是否可以点击。
        '''
        self.min_confirm.clicked.connect(lambda: self.set_minimum(self.min_input.text()))  # lamnda匿名函数（1.lambda只是一个表达式，函数体比def简单很多。2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。3.lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义）
        self.min_label = QLabel(f"{self.min_start}{self.min}")

        self.max_head = QLabel("限制最大值为:")
        self.max_input = QLineEdit()
        self.max_start = "最大值: "
        self.max_confirm = QPushButton("设置最大值")
        self.max_confirm.setEnabled(False)
        self.max_confirm.clicked.connect(lambda: self.set_maximum(self.max_input.text()))  
        self.max_label = QLabel(f"{self.max_start}{self.max}")

        self.min_input.textChanged.connect(lambda: self.valid_input(self.min_input.text(), self.min_confirm))
        self.max_input.textChanged.connect(lambda: self.valid_input(self.max_input.text(), self.max_confirm))

        self.recover_button = QPushButton("重置数值和设置")
        self.recover_button.clicked.connect(self.recover_values)

        # 将要添加到窗口的项目放入列表中
        objects = [
            self.number_label,
            self.button,
            self.min_head,
            self.min_input,
            self.min_label,
            self.min_confirm,
            self.max_head,
            self.max_input,
            self.max_label,
            self.max_confirm,
            self.recover_button
        ]

        layout = QVBoxLayout()  # 创建垂直框布局对象
        # 循环对象并将其添加到布局中
        for item in objects:
            layout.addWidget(item)
        
        container = QWidget()
        container.setLayout(layout)
        #父窗口->子窗口 ，父窗口的__init__函数里面先创建子窗口实例，然后再通过某个控件的信号（例如button的clicked信号）绑定某个槽（slot），槽函数直接对子窗口的控件进行操作。
        self.setCentralWidget(container)  # 将中心小部件设置为容器（主窗口子类）

    def generate_number(self):
        self.number = random.randint(self.min, self.max)  # 生成一个随机整数，范围在最小值和最大值之间
        self.number_label.setText(f"{self.num_label_start}{self.number:,d}")  # 将标签设置为随机生成的整数，格式化输出

    def set_minimum(self, num):
        self.min = int(num)
        self.min_label.setText(f"{self.min_start}{self.min:,d}")  # 更改标签的文本
        self.min_input.clear() # 清除输入框数字
        self.verify_min_max_values() #判断数值可用函数，并禁用按钮
    
    def set_maximum(self, num):
        self.max = int(num)
        self.max_label.setText(f"{self.max_start}{self.max:,d}")  # 更改标签的文本
        self.max_input.clear()  # 清除输入框数字
        self.verify_min_max_values()  # 判断数值可用函数，并禁用按钮

    def verify_min_max_values(self):
        """
        确保最小值小于最大值。如果最小值大于最大值,则禁用“生成随机数”按钮
        """
        if self.min < self.max:
            self.button.setText("生成随机数!")
            self.button.setEnabled(True)
            return
        self.button.setText("最小值大于最大值！")
        self.button.setEnabled(False)

    def valid_input(self, text, button):
        """
        确保传入的文本为整数。如果文本为整数，则将启用。如果文本不是整数，则被禁用。
        """
        try:
            int(text)
            button.setEnabled(True)
        except:
            button.setEnabled(False)
        #button.setEnabled 按钮启用禁用

    def recover_values(self):
        self.set_minimum(self.default_min)
        self.set_maximum(self.default_max)
        self.number_label.setText("")
        #重置默认范围函数
        
app = QApplication([])
#每个 PyQt6 应用程序都必须创建一个应用程序对象。sys.argv 参数是来自命令行的参数列表。Python 脚本可以从 shell 运行，这是应用启动的一种方式。
Num = MainWindow()
Num.show()
app.exec()