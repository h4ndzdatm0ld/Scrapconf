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
 
def get_config(task):
    ''' Extract the running xml configuration from our west-region devices via NETCONF.
    '''

    nc_extract = task.run(task=netconf_get_config, source='running')
     
def main():

    print_result(west_region.run(task=get_config))



if __name__ == "__main__":
    main()
