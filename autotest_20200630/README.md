【教程-精】白月黑羽教Python http://www.python3.vip/tut/auto/pytest/01/

## 运行方法
```
python -m pytest -vs case\登录\test_错误登录3_改为数据驱动并生成测试报告.py --html=./report/report.html --self-contained-html
```

## 待改进
1. 测试报告中中文显示乱码
2. 测试报告不是累加而是更新
3. 需要用 Pyppeteer 代替selenium 好配置环境