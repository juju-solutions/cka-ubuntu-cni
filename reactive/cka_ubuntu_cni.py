from charms.reactive import when, when_not, set_state
from charmhelpers.core import hookenv

@when_not('cka-ubuntu-cni.installed')
def install_cka_ubuntu_cni():
    set_state('cka-ubuntu-cni.installed')

@when('cni.connected')
@when_not('cni.configured')
def configure_cni(cni):
    ''' Set master configuration on the CNI relation. This lets the CNI
    subordinate know that we're the master so it can respond accordingly. '''
    cni.set_config(is_master=True, kubeconfig_path='')
    hookenv.status_set('active', 'ready')
