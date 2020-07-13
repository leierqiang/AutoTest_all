## 1.在“测试目标”文件夹中下载文件并运行(解压后双击runserver.bat)
- 初始界面 http://127.0.0.1/mgr/sign.html  byhy/88888888
- 参考资料：http://www.python3.vip/prac/pub/info/bysms/ 

## 2.安装依赖
根据requests.txt安装必须的库
```
pip install -r requirements.txt
```

## 3.运行测试用例
```
python -m pytest -vs case\APITest_all\test_添加客户.py --html=./report/report.html --self-contained-html

或
python -m pytest -vs case\APITest_all --html=./report/report.html --self-contained-html

```

## 4.在report/report.html 查看测试报告

## 5.注意
1、测试报告中中文显示乱码问题解决办法(注：如果使用的虚拟环境，就是修改原本的依赖的环境的文件)
```python
# 打开该插件对应的代码文件，通常在解释器目录下：site-packages\pytest_html\plugin.py
# 找到如下代码
class TestResult:
    def __init__(self, outcome, report, logfile, config):
        self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
# 改为
class TestResult:
    def __init__(self, outcome, report, logfile, config):
        # 白月黑羽修改方法，解决乱码问题
        # self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape")
        self.test_id = report.nodeid
```
2、在Pycharm中部分报红色(找不到包)但是可以正常运行,进行如下操作
```
（右键点击工程最外层目录）→ Mark Direct as → Sources Root
```
3、可以用 Pyppeteer 代替selenium，好配置环境 

## 6.感谢&推荐
白月黑羽教Python http://www.python3.vip/tut/auto/pytest/01/