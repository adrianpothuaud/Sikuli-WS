# -*- coding:utf-8 -*-

'''Control Web Browsers within objects'''

from sikuli import *

import Application

class Browser(Application.Application):
    '''Web browser object'''
    def __init__(self, app_name, exec_path):
        '''Constructor, parameters name and path'''
        Application.__init__(self, app_name, exec_path)
        self.name = app_name
        self.path = exec_path
    def new_tab(self, target_url = False):
        '''Open a new browser tab'''
        if Env.isWindows():
            type('t', Key.CTRL)
        elif Env.isMac():
            type('t', Key.CMD)
        if target_url:
            wait(1)
            paste(target_url)
            wait(1)
            type(Key.ENTER)
            wait(1)
