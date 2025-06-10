
[English](README.md) | [简体中文](README.zh-CN.md)

![AugmentFree Logo](/image/logo.png)

AugmentFree 是一个用于重置 VSCode-Augment 环境的实用工具。当您在 VSCode 中遇到 Augment AI 助手问题时，它可以帮助您清理 Augment 扩展状态。

> **免责声明**：此代码仅供学习目的使用。使用风险自负。

## 功能特点

- 重置 Augment 扩展存储文件
- 清除 Augment 状态数据库
- 支持不同操作系统（Windows、macOS、Linux）
- 简单的命令行界面

## 系统要求

- Python 3.8 或更高版本
- 安装了 Augment 扩展的 VSCode

> **注意**：此工具仅支持 VSCode 版本的 Augment。它不适用于其他 IDE 集成。

## 安装步骤

### 克隆仓库

```bash
git clone https://github.com/Lizaixuan/AugmentFree.git
# 或者
git clone https://gitee.com/BenLi19999/augment-free.git

cd AugmentFree
```

### 设置环境

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows系统
.venv\Scripts\activate
# macOS/Linux系统
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

使用 Python 运行工具：

```bash
python main.py
```

## 构建可执行文件

要自行构建可执行文件：

```bash
# 运行构建脚本
python build.py
```

这将在 `dist` 目录中为您当前的平台创建一个可执行文件。

工具将会：
1. 检测您的操作系统
2. 查找 VSCode-Augment 配置路径
3. 重置 storage.json 文件
4. 重置 state.vsdb 数据库
5. 确认重置成功

## 使用场景

在以下情况下使用 AugmentFree：
- Augment AI 助手响应不正确
- 您遇到 Augment 身份验证问题
- 扩展状态似乎已损坏
- 您想要从干净的 Augment 环境开始
- 您想重置机器码

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

该项目采用 MIT 许可证 - 有关详细信息，请参阅 LICENSE 文件。

## 作者

Zayn

## 链接

- GitHub: [https://github.com/Lizaixuan/augment-free](https://github.com/Lizaixuan/augment-free)
- Gitee: [https://gitee.com/BenLi19999/augment-free](https://gitee.com/BenLi19999/augment-free)
