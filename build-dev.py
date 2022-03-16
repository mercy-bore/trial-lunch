import os
import subprocess
import time

CURRENT_DIR = os.getcwd()
directories = os.listdir(CURRENT_DIR)
NON_ANGULAR_DIRS = ['static', 'templates', 'venv']

for dir in directories:
    if "." not in dir and dir not in NON_ANGULAR_DIRS:
        ANGULAR_PATH = os.path.join(CURRENT_DIR, dir)
        DIST_PATH = os.path.join(ANGULAR_PATH,'dist', dir)
        
FLASK_STATIC_PATH = os.path.join(CURRENT_DIR, 'static')
FLASK_TEMPLATE_PATH = os.path.join(CURRENT_DIR, 'templates')

subprocess.call(('cd' + ANGULAR_PATH + ' && ng build --watch --base-href /static/ &'),shell=True)
dir_exists = True

while dir_exists:
    try:
        files = os.listdir(DIST_PATH)
        static_files = ""
        html_files = ""
        for f in files:
            if '.js' in f or '.js.map' or '.ico' in f:
                static_files += (f + ' ')
            if '.html' in f:
                static_files += (f + ' ')
                
        if len(static_files) > 0:
            subprocess.call(('cd' + DIST_PATH + '&&' + 'mv' +   static_files + FLASK_STATIC_PATH), shell=True)
        if len(html_files) > 0:
            subprocess.call(('cd' + DIST_PATH + '&&' + 'mv' +   html_files + FLASK_STATIC_PATH), shell=True)
    except Exception as e:
        dir_exists = False
        print(e)
        time.sleep(10.0)