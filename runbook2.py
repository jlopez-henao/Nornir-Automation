from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_test(task):
    task.run(task=send_command, command="show interface status | grep notconnect")

results = nr.run(task=show_command_test)
print_result(results)

+--project_directory
   +--snapshot
   |  +--configs
   |     +--EOS1.cfg
   |     +--VX1.cfg
   |     +--XR1.cfg
   +--main.py


3
$ python3.9 -m venv venv
$ source venv/bin activate
(venv)$ pip install pybatfish