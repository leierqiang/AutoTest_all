## 版本

1.03

## 已知bug

### 0001 

套件目录中的初始化文件 __st__.py里面的 test_setup  test_teardown 会导致没有自身初始化清除的用例执行失败。

出现  No keyword with name 'D.test_setup' found 的错误提示。
这个应该是robotframework自身的bug。 因为 suite_setup 就没有这样的问题。


参考 https://github.com/robotframework/robotframework/issues/3416

### 0002

本层目录和上层目录如果使用 同名的  用例文件，里面的用例类也同名， 会出现执行时，使用上层目录中的测试类teststeps。

应该也是 robotframework 本身的bug。 

参考 https://github.com/robotframework/robotframework/issues/3590