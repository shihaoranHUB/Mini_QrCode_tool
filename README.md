# Mini_QrCode_tool
下面是通俗易懂的英文翻译：

### 1. Overview
This QR code generator is a desktop application developed using Python. It leverages the PyQt6 library for building the user interface and the qrcode library to generate QR codes. The tool can quickly create QR codes based on text or web links provided by the user and supports saving the generated QR codes as images.

### 2. Features
- **Flexible Input**: Accepts both plain text and web links to generate QR codes.
- **Real-time Preview**: Displays the generated QR code instantly on the application interface.
- **Save Functionality**: Allows users to save the generated QR code as a PNG image.
- **Help Information**: Provides a help window with instructions and guidance on input formats.

### 3. Technical Implementation
- **User Interface**: Utilizes PyQt6 to create a simple and intuitive graphical user interface (GUI) with input fields, buttons, and a QR code display area.
- **QR Code Generation**: Employs the qrcode library to generate QR code images from user input.
- **Error Handling**: Implements error detection and feedback for issues that may occur during QR code generation, display, or saving.

### Instructions for Use

#### 1. Launch the Application
Run the Python script to start the application. The main interface will appear.

#### 2. Enter Content
In the input field labeled "Enter text or web link", type the content you want to convert into a QR code:
- **Plain Text**: Enter any text directly, e.g., "Hello, World!".
- **Web Link**: Ensure the link starts with `https://`, e.g., `https://www.example.com`.

#### 3. Generate QR Code
Click the "Generate" button. The application will create a QR code based on your input and display it on the screen.

#### 4. Save the QR Code
After generation, a prompt will ask if you want to save the QR code:
- **Save**: Click "Yes" to open a file dialog. Choose a location and filename, then click "Save".
- **Don't Save**: Click "No" to discard the temporary QR code image.

#### 5. Get Help
If you encounter issues or need guidance on formatting links, click the "Help" button for instructions.

#### 6. Exit the Application
Close the application window to exit.

### Notes
- Web links must start with `https://` to ensure proper QR code generation.
- Ensure you have write permissions in the selected directory when saving QR code images.
- Error messages will appear if issues occur during generation, display, or saving. Follow the prompts to resolve them.

- ### 1. 概述
这个二维码生成器是一款用Python开发的桌面应用程序。它利用PyQt6库构建用户界面，使用qrcode库生成二维码。该工具能根据用户提供的文本或网页链接快速生成二维码，并支持将生成的二维码保存为图片。

### 2. 功能特性
- **输入灵活**：既可以接受纯文本，也能接受网页链接来生成二维码。
- **实时预览**：生成的二维码会立即显示在应用程序界面上。
- **保存功能**：允许用户将生成的二维码保存为PNG格式的图片。
- **帮助信息**：提供带有使用说明和输入格式指南的帮助窗口。

### 3. 技术实现
- **用户界面**：利用PyQt6创建一个简单直观的图形用户界面（GUI），包含输入框、按钮和二维码显示区域。
- **二维码生成**：借助qrcode库根据用户输入内容生成二维码图片。
- **错误处理**：在二维码生成、显示或保存过程中，对可能出现的问题进行错误检测和反馈。

### 使用说明
#### 1. 启动应用程序
运行Python脚本启动应用程序，主界面将会出现。

#### 2. 输入内容
在标有“输入文本或网页链接”的输入框中，输入你想要转换成二维码的内容：
- **纯文本**：直接输入任意文本，例如“你好，世界！”。
- **网页链接**：链接必须以`https://`开头，例如`https://www.example.com`。

#### 3. 生成二维码
点击“生成”按钮。应用程序会根据你的输入生成二维码，并显示在屏幕上。

#### 4. 保存二维码
生成二维码后，会弹出一个提示框询问你是否保存该二维码：
- **保存**：点击“是”，会打开一个文件对话框。选择保存位置和文件名，然后点击“保存”。
- **不保存**：点击“否”，临时生成的二维码图片将被丢弃。

#### 5. 获取帮助
如果你遇到问题或需要输入链接格式方面的指导，点击“帮助”按钮获取相关说明。

#### 6. 退出应用程序
关闭应用程序窗口即可退出。

### 注意事项
- 网页链接必须以`https://`开头，以确保二维码能正确生成。
- 保存二维码图片时，请确保你在所选目录中有写入权限。
- 如果在生成、显示或保存二维码时出现问题，将会弹出错误提示。按照提示信息进行解决。 
