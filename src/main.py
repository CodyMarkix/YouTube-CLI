#!/usr/bin/env python3
import frontend
import oobe
import os

def main():
    if os.path.isfile(os.path.join(os.path.expanduser("~"), ".local", "share", "ytcli", "apikey.json")):
        frontend.menus.enterMenu()
    else:
        oobe.firstsetup.setup()

main()