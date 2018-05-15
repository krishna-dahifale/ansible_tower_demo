Cloudformation infra
====================

Creates cloud formation infrastructure for ifabric ambari cluster.

Requirements
------------

A registered domain must be added to Route53 as a Hosted Zone before installation. This registered domain can be purchased through AWS.

Role Variables
--------------

None

Dependencies
------------

None

Run Playbook
----------------

How to include and run the role in playbook:

	- hosts: localhost
	  connection: local
	  gather_facts: no
	  become: no
	  roles:
	  - cloudformation-infra

License
-------

None

Author Information
------------------

Atos iFabric Team
