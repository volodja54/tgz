#!/usr/bin/python3

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        versions_dir = "versions"
        if not isdir(versions_dir):
            local("mkdir -p {}".format(versions_dir))
        file_name = "{}/web_static_{}.tgz".format(versions_dir, date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
