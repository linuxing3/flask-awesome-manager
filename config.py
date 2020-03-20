#!/usr/bin/env python3

import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your-never-guess"
    SERVER_NAME = "http://0.0.0.0:8000"
