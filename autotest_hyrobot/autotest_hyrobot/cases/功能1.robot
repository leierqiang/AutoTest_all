*** Settings ***

Library  功能1.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     冒烟测试   订单功能  

Default Tags     优先级7

Library  功能1.c00001   WITH NAME  c00001

Library  功能1.c00002   WITH NAME  c00002

Library  功能1.c00003x   WITH NAME  c00003x



*** Test Cases ***

添加订单 - 00001
  [Tags]      本次不测   now
  [Setup]     c00001.setup
  [Teardown]  c00001.teardown

  c00001.teststeps


添加订单 - 00002
  [Teardown]  c00002.teardown

  c00002.teststeps


登录 - 000031
  [Teardown]  c00003x.teardown

  c00003x.teststeps   ${0}


登录 - 000032
  [Teardown]  c00003x.teardown

  c00003x.teststeps   ${1}


登录 - 000033
  [Teardown]  c00003x.teardown

  c00003x.teststeps   ${2}
