from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import json

nr = InitNornir(config_file="config.yaml")

# def show_command_test(task):
#     interfaces_result = task.run(task=send_command, command="show interface status | json")
#     task.host['interfaces'] = interfaces_result.result

# results = nr.run(task=show_command_test)
# # import ipdb
# # ipdb.set_trace()
# print_result(results)

def show_command_test(task):
    available_intf = []
    interfaces_result = task.run(task=send_command, command="show interface status | json")
    task.host['facts'] = json.loads(interfaces_result.result)
    interfaces = task.host['facts']['interfaceStatuses']
    for intf, status in interfaces.items():
        if status['linkStatus'] == 'notconnect':
            available_intf.append(intf)
    return available_intf

# import ipdb
# ipdb.set_trace()

results = nr.run(task=show_command_test)
# print_result(results)


"""
available_intf = []
for k, v in something.items():
    new_values = v
    for intf, info in new_values.items():
        # print(intf)
        # print(info)
        # print(type(info))
        if info['linkStatus'] == 'notconnect' and info['description'] == '':
            # print('ha got you, you are spare')
            available_intf.append(intf)
print('spare ports list: ', available_intf)
"""
