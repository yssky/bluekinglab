# -*- coding: utf-8 -*-
from config import RUN_VER
if RUN_VER == 'open':
    from blueapps.patch.settings_open_saas import *  # noqa
else:
    from blueapps.patch.settings_paas_services import *  # noqa

# 正式环境
RUN_MODE = 'PRODUCT'

# 正式环境的日志级别可以在这里配置
# V2
# import logging
# logging.getLogger('root').setLevel('INFO')


# 正式环境数据库可以在这里配置
DATABASES.update(
    {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bluekinglabdb',  # 数据库名
            'USER': 'root',  # 数据库用户
            'PASSWORD': 'Uqv.83WuNm',  # 数据库密码
            'HOST': '10.0.1.192',  # 数据库主机
            'PORT': '3306',  # 数据库端口
        },
    }
)
