from flask import request
import subprocess

def inert_fixture():
    return subprocess.check_output(request.args["command"], shell=True)
