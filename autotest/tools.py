def do_login(page):
    page.goto("https://smartlink.fivepointtex.com/test_1/#/login")
    page.get_by_role("textbox", name="Please enter account").click()
    page.get_by_role("textbox", name="Please enter account").fill("Tracer")
    page.get_by_role("textbox", name="Please enter password").click()
    page.get_by_role("textbox", name="Please enter password").fill("Tracer938")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("https://smartlink.fivepointtex.com/test_1/#/")