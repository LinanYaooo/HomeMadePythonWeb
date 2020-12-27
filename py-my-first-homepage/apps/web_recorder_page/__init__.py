# 依赖引入
from flask import Blueprint, render_template_string,blueprints

# 视图函数引入
from .view import PageView

# 创建蓝图
web_recorder = Blueprint("WebRecorder", __name__, url_prefix="")


@web_recorder.route("/")
def index():
    return render_template_string(PageView.index())
