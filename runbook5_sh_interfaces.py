from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import json

nr = InitNornir(config_file="config.yaml")

def show_command_test(task):
    available_intf = []
    interfaces_result = task.run(task=send_command, command="show interface status | json")
    task.host['facts'] = json.loads(interfaces_result.result)
    interfaces = task.host['facts']['interfaceStatuses']
    for intf, status in interfaces.items():
        if '/' not in intf and 'Port' not in intf and 'Management' not in intf:
            if status['linkStatus'] == 'notconnect' and 'Ethernet' in intf:
                available_intf.append(intf)
    print(f'{task.host} available interfaces', len(available_intf))

results = nr.run(task=show_command_test)
# import ipdb
# ipdb.set_trace()
