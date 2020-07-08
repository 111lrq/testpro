import os
import shlex
import signal
import subprocess

import pytest


# @pytest.fixture(scope="module", autouse=True)
def record_video():
    cmd = shlex.split("scrcpy --record ../results/tmp1.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.SIGTERM)
    ##此部分内容待进一步深入实践学习
    # os.kill(p.pid, signal.SIGKILL)
    # os.popen('taskkill.exe /pid:' + str(p.pid))
    # os.kill(p.pid, signal.CTRL_C_EVENT)#由于pytest会将CTRL+C识别为中断程序，故此处使用kill pid的方法来停止录屏

