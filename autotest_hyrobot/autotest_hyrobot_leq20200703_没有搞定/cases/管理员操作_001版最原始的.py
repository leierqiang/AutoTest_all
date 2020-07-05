from hyrobot.common import *


class c1(object):
    """
    一个c1是一个用例(或一个功能)
    """
    name = "管理员首页 UI-0101"  # 用例可能是口语化的名字或者不规范，所以不放在类名中

    def teststeps(self):
        STEP(1, '登录')  # 在控制台输出日志，注print只会出现在报告中，不会出现在控制台
        from selenium import webdriver
        wd = webdriver.Chrome()
        wd.implicitly_wait(5)
        wd.get('http:127.0.0.1/mgr/sign.html')
        # 根据id找到并输入账号密码
        wd.find_element_by_id('username').send_keys('byhy')
        wd.find_element_by_id('password').send_keys('88888888')

        STEP(2, '获取左侧信息')  # 在控制台输出日志
        # 根据标签名找到元素
        wd.find_element_by_tag_name('button').click()
        # 先找到上层节点再缩小范围
        sidebarMenu = wd.find_element_by_class_name('sidebar-menu')
        # 再找到内部的各个元素
        element = sidebarMenu.find_elements_by_tag_name('span')

        STEP(3, '对比是否符合预期')  # 在控制台输出日志
        menuTitles = []
        for ele in element:
            print(ele.text)
            menuTitles.append(ele.text)

        print('*****检查点*****  侧边栏菜单是否正确----------', end='')
        if menuTitles[:3] == ['客户', '药品', '订单']:
            print('通过')
        else:
            print("不通过")
            exit(1)
        wd.quit()


class c2(object):
    name = "管理员首页 UI-0201"

    def teststeps(self):
        pass
