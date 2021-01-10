#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

from flask import Blueprint, render_template

member = Blueprint(name="member", import_name=__name__)


@member.route("/register/")
def register():
    return render_template("member/register.html")


@member.route("/login/")
def login():
    return render_template("member/login.html")
