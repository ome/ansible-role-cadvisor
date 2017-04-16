import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_service(Service):
    assert Service('cadvisor').is_running
    assert Service('cadvisor').is_enabled


def test_metrics(Command):
    out = Command.check_output('curl http://localhost:9280/metrics')
    assert 'cadvisor_version_info{' in out
