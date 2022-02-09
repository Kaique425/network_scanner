from random import choice

import nmap

"""This class allow  us to scan all ips address and hosts 
   from the current machine """


class Network:
    def __init__(self, network="192.168.4.1/24"):
        self.network = network

    def networkscanner(self):
        nm = nmap.PortScanner()
        nm.scan(hosts=self.network, arguments="-sn")
        host_list = [(x, nm[x]["status"]["state"]) for x in nm.all_hosts()]
        return host_list
