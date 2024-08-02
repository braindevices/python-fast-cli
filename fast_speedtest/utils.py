from playwright.sync_api import sync_playwright
import playwright._impl._errors
import sys
import subprocess

def need_to_install_browsers():

    with sync_playwright() as p:
        try:
            p.chromium.launch(headless=True)
            return False
        except playwright._impl._errors.Error as e:
            if "playwright install" in e.args[0]:
                return True
            raise e


def auto_install_browsers():
    if need_to_install_browsers():
        subprocess.check_call([sys.executable, '-m', 'playwright', 'install'])
