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
        # if intf ['linkStatus'] == 'notconnect':
        #     available_intf.append(intf)
        # print(intf)
    # testvariable = task.host['facts']
    # print(type(testvariable))
        if status['linkStatus'] == 'notconnect':
            # print (intf)
            available_intf.append(intf)
        # print (available_intf)
    return available_intf



results = nr.run(task=show_command_test)
print_result(results)
# import ipdb
# ipdb.set_trace()

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
