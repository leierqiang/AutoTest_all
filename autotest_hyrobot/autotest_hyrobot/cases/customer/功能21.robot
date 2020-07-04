*** Settings ***

Library  功能21.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Test Setup    F.test_setup

Test Teardown    F.test_teardown

Force Tags     冒烟测试   订单功能  

Default Tags     优先级7

Library  功能21.c1   WITH NAME  c1

Library  功能21.c2   WITH NAME  c2



*** Test Cases ***

添加订单 - 00001
  [Tags]      本次不测   now
  [Setup]     c1.setup
  [Teardown]  c1.teardown

  c1.teststeps


添加订单 - 00002
  [Teardown]  c2.teardown

  c2.teststeps
