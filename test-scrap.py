# test-scrap.py

import logging
from scrapli_netconf.driver import NetconfScrape
logging.basicConfig(filename="scrapli.log", level=logging.INFO)
logger = logging.getLogger("scrapli")
DEVICE = {
    "host": "192.168.0.222",
    "port": 830,
    "auth_username": "netconf",
    "auth_password": "NCadmin123",
    "auth_strict_key": False,
}
conn = NetconfScrape(**DEVICE)
conn.open()
result = conn.get_config()
print(result.result)
print(result.get_xml_elements())