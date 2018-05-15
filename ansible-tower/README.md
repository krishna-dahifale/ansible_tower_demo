The iFabric Ambari cluster on Amazon Web Services
========================================================================

This repository contains the scripts used to deploy an iFabric Ambari cluster on Amazon Web Services.

Overview
--------
The repository contains Ansible playbooks which deploy 1 bastion, 1 ambari-server, 1 ambari-agent and 1 nginx machine.
The code in this repository handles all of the AWS specific components and installation of ambari.


Prerequisites
-------------

iFabric Ansible control Machine must be up and running.

A registered domain must be added to Route53 as a Hosted Zone before installation. This registered domain can be purchased through AWS.

Below environment variable are available on Asible control Machine.

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY 


Dependencies
------------

None

Deploying iFabric Ambari cluster
--------------------------------

How to run Python to create iFabric Ambari cluster up and running:

python codex-ifabric-ansible-pov/aws-ansible/iFabric.py --stack-name=stack-name --no-confirm

License
-------

None

Author Information
------------------

Atos iFabric Team