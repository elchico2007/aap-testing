#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from pexpect import pxssh
import re

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        opengear_host=dict(type='str', required=True),
        opengear_user=dict(type='str', required=True),
        opengear_password=dict(type='str', required=True, no_log=True),
        port=dict(type='int', required=True),
        network_user=dict(type='str', required=True),
        network_password=dict(type='str', required=True, no_log=True),
        commands=dict(type='list', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    # # use whatever logic you need to determine whether or not this module
    # # made any modifications to your target
    # if module.params['new']:
    #     result['changed'] = True

    try:
        client = pxssh.pxssh(options={"StrictHostKeyChecking": "no"})
        client.login(module.params['opengear_host'], module.params['opengear_user'], module.params['opengear_password'])

        client.sendline("./opengear.sh")
        client.prompt()
        #client.PROMPT = r'Connect to port>'
        client.sendline(f"{module.params['port']}")
        client.prompt()
        #client.PROMPT = r'Username:'
        client.sendline(f"{module.params['network_user']}")
        client.prompt()
        #client.PROMPT = r'Password:'
        client.sendline(f"{module.params['network_password']}")
        client.prompt()
        #client.PROMPT = r'\w+>'
        for command in module.params['commands']:
            client.sendline(command)
            client.prompt()
            #client.PROMPT = r'\w+>'

        module.exit_json(msg=client.before.decode().replace("\r", "").split("\n"))


    except pxssh.ExceptionPxssh as e:
        module.fail_json(e)

    # client = paramiko.client.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # client.connect(module.params['opengear_host'], username=module.params['opengear_user'], password=module.params['opengear_password'])

    #_stdin, _stdout,_stderr = client.exec_command("./opengear.sh")

    #module.exit_json(msg=_stdout.read())

    # result['output'] = _stdout.read().decode()
    # result['output_lines'] = result['output'].split('\n')

    # result['output_err'] = _stderr.read().decode()
    # if result['output_err'] != "":
    #     module.fail_json(msg='Something went wrong', **result)
    
    client.close()

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()