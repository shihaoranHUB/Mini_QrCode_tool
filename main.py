import sys
import os
import qrcode
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QFileDialog, QMessageBox, QTextEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('食用帮助')

        # 设置窗口无边框
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

        layout = QVBoxLayout()

        # 添加长文本域
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # 设置为只读模式

        # 要插入的文本
        help_text = """
<html>
<p>### 二维码生成工具介绍</p>

<p>#### 1. 概述</p>
<p>此二维码生成工具是一款借助 Python 语言开发的桌面应用程序，运用了 PyQt6 库构建用户界面，同时利用 qrcode 库生成二维码。它能够依据用户输入的文本或者网页链接，快速生成对应的二维码，并且支持保存生成的二维码图片。</p>

<p>#### 2. 功能特性</p>
<ul>
    <li>**输入灵活**：既可以输入普通文本，也能输入网页链接来生成二维码。</li>
    <li>**实时预览**：生成二维码后，会在应用界面实时显示。</li>
    <li>**保存功能**：用户可以选择将生成的二维码保存为 PNG 格式的图片。</li>
    <li>**帮助信息**：提供使用和输入链接帮助窗口，为用户答疑解惑。</li>
</ul>

<p>#### 3. 技术实现</p>
<ul>
    <li>**用户界面**：采用 PyQt6 库创建了简洁易用的图形用户界面（GUI），包含输入框、按钮、图片显示区域等组件。</li>
    <li>**二维码生成**：借助 qrcode 库依据用户输入的内容生成二维码图片。</li>
    <li>**错误处理**：在生成、显示和保存二维码的过程中，对可能出现的错误进行了捕获和提示。</li>
</ul>

<p>### 使用说明</p>

<p>#### 1. 启动应用</p>
<p>运行该 Python 脚本，应用程序将会启动，显示主界面。</p>

<p>#### 2. 输入内容</p>
<p>在“输入文本或网页链接”的输入框中，输入你想要生成二维码的内容。</p>
<ul>
    <li>**普通文本**：直接输入任意文本，例如“你好，世界！”。</li>
    <li>**网页链接**：需使用 <code>https://xxx.xxx</code> 格式输入链接，例如 <code>https://www.example.com</code>。</li>
</ul>

<p>#### 3. 生成二维码</p>
<p>点击“生成”按钮，程序会依据你输入的内容生成对应的二维码，并在界面上显示。</p>

<p>#### 4. 保存二维码</p>
<p>生成二维码后，会弹出提示框询问你是否保存生成的二维码。</p>
<ul>
    <li>**保存**：点击“是”，会弹出文件保存对话框，你可以选择保存的路径和文件名，然后点击“保存”即可。</li>
    <li>**不保存**：点击“否”，生成的临时二维码图片会被删除。</li>
</ul>

<p>#### 5. 获取帮助</p>
<p>若你在使用过程中遇到问题，或者不清楚如何输入链接，可以点击“使用和输入链接帮助”按钮，会弹出帮助窗口，为你提供相关信息。</p>

<p>#### 6. 退出应用</p>
<p>关闭应用窗口即可退出程序。</p>

<p><span style="color:red">### 注意事项</span></p>
<ul style="color:red">
    <li>输入的网页链接必须以 <code>https://</code> 开头，否则可能无法正确识别和生成对应的二维码。</li>
    <li>保存二维码图片时，请确保你有足够的权限在所选路径下创建文件。</li>
    <li>若在生成、显示或保存二维码的过程中出现错误，会弹出错误提示框，你可以根据提示信息进行相应处理。</li>
</ul>
</html>
        """

        self.text_edit.setText(help_text)
        layout.addWidget(self.text_edit)

        # 添加关闭按钮
        close_button = QPushButton("关闭当前窗口")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        # 窗口最大化显示
        self.showMaximized()


class QRCodeGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.help_window = None
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        text_label = QLabel("输入文本或网页链接:")
        self.text_input = QLineEdit()
        text_layout = QHBoxLayout()
        text_layout.addWidget(text_label)
        text_layout.addWidget(self.text_input)
        layout.addLayout(text_layout)

        generate_button = QPushButton("生成")
        generate_button.clicked.connect(self.generate_qr_code)
        layout.addWidget(generate_button)

        help_button = QPushButton("使用和输入链接帮助")
        help_button.clicked.connect(self.show_help_window)
        layout.addWidget(help_button)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        author_label = QLabel("By haoran")
        author_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        author_label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(author_label)

        self.setLayout(layout)
        self.setWindowTitle('二维码生成器 QrCode')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def generate_qr_code(self):
        text = self.text_input.text()
        try:
            if text.startswith(('http://', 'https://')):
                img = qrcode.make(text)
            else:
                img = qrcode.make(text)

            temp_file_path = "temp_qr.png"
            img.save(temp_file_path)
            self.show_image(temp_file_path)
            self.ask_to_save(temp_file_path)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成二维码时出错: {str(e)}")

    def show_image(self, file_path):
        try:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.AspectRatioMode.KeepAspectRatio))
        except Exception as e:
            QMessageBox.critical(self, "错误", f"显示图片时出错: {str(e)}")

    def ask_to_save(self, temp_file_path):
        reply = QMessageBox.question(self, '保存文件', '是否保存生成的二维码？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            file_path, _ = QFileDialog.getSaveFileName(self, "保存二维码", "", "PNG Images (*.png)")
            if file_path:
                try:
                    os.replace(temp_file_path, file_path)
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"保存文件时出错: {str(e)}")
        else:
            try:
                os.remove(temp_file_path)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"删除临时文件时出错: {str(e)}")

    def show_help_window(self):
        if self.help_window is None or not self.help_window.isVisible():
            self.help_window = HelpWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QRCodeGeneratorApp()
    sys.exit(app.exec())