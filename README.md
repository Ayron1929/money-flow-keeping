# 可视化智能记账

**这是一个用Python实现的可视化智能记账小程序。**

**可以用它轻松记录每日不同银行卡的收支情况、自由增减划分类别、进行备注说明，并且具有提示最近一次记账的日期以及当前账本已存备注的功能。**

**完成记账后退出界面时，所有收支都会保存在自动生成的即时csv中，另外在本文件夹内会自动地生成一份关于当前已记录流水的报告，其中会统计账户分别和总共的收支、所有分类的概览和单独某一个的细则。**

**Fork并将本项目克隆到本地**

## 运行脚本前

搭建虚拟环境来安装所使用的包
1. 推荐使用Visual Studio Code，Python版本需要在3.11.0及以上
2. 打开终端，定位到当前文件夹的目录
3. 创建并激活venv
   > **Mac**: 输入 `python(3) -m venv venv`  和 `source venv/bin/activate`
   
   > **Windows**: 输入 `python(3) -m venv venv`， `(Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser) `和 `venv\Scripts\activate`
4. 下载所有包
   >  **Mac/Windows**: 输入 `pip install -r requirements.txt`

## 使用说明

1. 打开`run.py`，按需依照注释修改部分代码
2. 打开终端，确保虚拟环境已经成功激活
   > **Mac/Windows**: 输入 `python(3) -m run`

**祝使用愉快！**

## 示例

**`demo.csv` 和 `demo.pdf`**

## 反馈

邮箱: **ayron1929@gmail.com** 和 **irisshao1008@gmail.com**

<!-- License:
