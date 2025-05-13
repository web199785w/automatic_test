import re
from playwright.sync_api import Page, expect
from autotest.tools import do_login

def test_example(page: Page) -> None:
    do_login(page) 
    # page.goto("https://smartlink.fivepointtex.com/test_1/#/login")
    # page.get_by_role("textbox", name="Please enter account").click()
    # page.get_by_role("textbox", name="Please enter account").fill("Tracer")
    # page.get_by_role("textbox", name="Please enter password").click()
    # page.get_by_role("textbox", name="Please enter password").fill("Tracer938")
    # page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Inquiry").click()
    page.get_by_role("textbox", name="Please enter product").click()
    page.get_by_role("textbox", name="Please enter product").fill("8883 #1 10 #2 100m")
    page.get_by_role("button", name="Quick Analysis").click()
    page.get_by_role("textbox", name="Please enter and select").click()
    page.get_by_text("Quay Thuy Hong (K000001)").click()
    page.get_by_role("button", name="Confirm Customer").click()
