#!/usr/bin/env python 3
# Scrapli Example 1

import xmltodict, json
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import (
    netconf_lock,
    netconf_unlock,
    netconf_get,
    netconf_get_config,
    netconf_rpc,
    netconf_commit
)

__author__ = "Hugo Tinoco"
__email__ = "hugotinoco@icloud.com"

# Specify a custom con
  #   region: west-regionfig yaml file.
nr = InitNornir("config.yml")

# Filter the hosts by the 'west-region' site key.
west_region = nr.filter(region="west-region")

def xml_helper(nornir_result):
    '''Post process scrapli_netconf's netconf_get_config to prettify 
        Nokias returned xml output.

    Args:
        nornir_result = nornir_result (str)
    '''
    from xml.dom.minidom import parseString
    reply = parseString(nornir_result)
    return '\n'.join([line for line in reply.toprettyxml(indent=' ').split('\n') if line.strip()])

def get_config(task):
    ''' Extract the running xml configuration from our west-region devices via NETCONF.
    '''
    nc_extract = task.run(task=netconf_get_config, source='running')
    
    if task.host.platform == 'alcatel_sros':
        print(xml_helper(nc_extract.result))

    elif task.host.platform == 'iosxr':
        print(nc_extract.result)
        

def main():

    west_region.run(task=get_config)

if __name__ == "__main__":
    main()
