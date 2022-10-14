####### have file in ~/.local/lib/python3.6/site-packages/ansiblelint/rules/

from ansiblelint.rules import AnsibleLintRule

class testAwsCred(AnsibleLintRule):
    """Rule to not allow aws_access_key_id or aws_secret_access_key in the playbook"""

    id = 'AWS_CRED_TEST'
    shortdesc = 'Playbook may not contain any aws credentials in variables, especially if they are stored publically'
    description = 'Playbook may not contain any aws credentials in variables, especially if they are stored publically'
    tags = ['variables']

    def match(self, line):
        if "aws_access_key_id" in line or "aws_secret_access_key" in line:
            return True
        return False