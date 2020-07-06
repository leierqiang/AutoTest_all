*** Settings ***

Library  管理员操作_001版最原始的.py   WITH NAME  F

Library  管理员操作_001版最原始的.c1   WITH NAME  c1

Library  管理员操作_001版最原始的.c2   WITH NAME  c2



*** Test Cases ***

管理员首页 UI-0101

  c1.teststeps


管理员首页 UI-0201

  c2.teststeps
