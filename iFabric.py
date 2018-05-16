#!/usr/bin/env python

import click
import os
import sys

@click.command()

@click.option('--stack-name', default='iFabric-infra', help='Cloudformation stack name. Must be unique',
              show_default=True)
@click.option('--no-confirm', is_flag=True,
              help='Skip confirmation prompt')

@click.option('-v', '--verbose', count=True)

			  
def createStack(stack_name=None, no_confirm=False, verbose=0):

    click.echo('Configured values:')
    click.echo('\tstack_name: %s' % stack_name)
    click.echo("")

    if not no_confirm:
         click.confirm('Continue using these values?', abort=True)
    
    playbooks = ['/home/centos/ansible-tower/ambari-install.yml']

    for playbook in playbooks:

        devnull='> /dev/null'

        if verbose > 0:
          devnull=''

        command='ansible-playbook -i /home/centos/codex-ifabric-ansible-pov/aws-ansible/inventory/hosts -e \'stack_name=%s \' %s' % (stack_name, playbook)
        status = os.system(command)

        if os.WIFEXITED(status) and os.WEXITSTATUS(status) != 0:
            sys.exit(os.WEXITSTATUS(status))


#if __name__ == '__main__':
    # if os.getenv('AWS_ACCESS_KEY_ID') is None or os.getenv('AWS_SECRET_ACCESS_KEY') is None:
     #     print('AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY **MUST** be exported as environment variables.')
     #     sys.exit(1)

     createStack()
