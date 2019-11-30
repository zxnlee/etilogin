from django.conf import settings
settings.configure()
import django
django.setup()
from django.contrib.auth.models import User
from django.test.client import Client
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


def test_login():
    c = Client()
    c.login(username="zxnlee", password="P@ssw0rd")
