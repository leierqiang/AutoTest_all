##1.【教程】
白月黑羽教Python http://www.python3.vip/tut/auto/pytest/01/

## 2.运行方法
```
python -m pytest -vs case\登录\test_错误登录3_改为数据驱动并生成测试报告.py --html=./report/report.html --self-contained-html
```
## 3.测试目标-在这个网站下载并运行
http://www.python3.vip/prac/pub/info/bysms/ 

## 4.注意
根目录下的venv是环境，可以直接用

## 5.待改进
1. 测试报告中中文显示乱码
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
2. 测试报告不是累加而是更新
3. 需要用 Pyppeteer 代替selenium 好配置环境