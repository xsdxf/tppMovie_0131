# -*- coding:utf-8 -*-
from flask import Flask

from eagleEye.configs import RegexConverter, DevelopmentConfig, TestingConfig, ProductionConfig

def create_app():
    # 创建app对象
    app = Flask("ttpMovie")

    # 加载配置
    app.config.from_object(DevelopmentConfig)
    # 注册转换器类
    app.url_map.converters["regex"] = RegexConverter

    # 三方对象加载app对象

    # 注册路由

    return app






