from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

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
    for intf in interfaces:
        # if intf ['linkStatus'] == 'notconnect':
        #     available_intf.append(intf)
        print(intf)
    # testvariable = task.host['facts']
    # print(type(testvariable))

results = nr.run(task=show_command_test)
print_result(results)
# import ipdb
# ipdb.set_trace()
