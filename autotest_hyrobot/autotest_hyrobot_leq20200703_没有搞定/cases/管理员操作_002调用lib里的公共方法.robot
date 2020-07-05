*** Settings ***

Library  管理员操作_002调用lib里的公共方法.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Library  管理员操作_002调用lib里的公共方法.c1   WITH NAME  c1



*** Test Cases ***

管理员首页 UI-0101
  [Setup]     c1.setup
  [Teardown]  c1.teardown

  c1.teststeps
