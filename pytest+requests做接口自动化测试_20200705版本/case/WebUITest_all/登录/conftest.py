import pytest


# @pytest.fixture(scope='package', autouse=True)  # scope=‘package’ 目录级别的动作执行顺序有BUG慎用
# def st_emptyEnv():
#     print(f'\n#### 初始化-目录甲')
#     yield
#
#     print(f'\n#### 清除-目录甲')
