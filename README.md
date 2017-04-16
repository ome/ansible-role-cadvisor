cAdvisor
========

cAdvisor container monitoring.

cAdvisor can be run in a [Docker container](https://github.com/google/cadvisor), however on RHEL/CentOS it requires [additional flags](https://github.com/google/cadvisor/blob/master/docs/running.md).
An alternative is to run it directly on the host system using this role.


Variables
=========

Optional:
- `cadvisor_port`: Listen on this port, default `9280`


Example playbook
----------------

    - hosts: localhost
      roles:
      - role: cadvisor


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
