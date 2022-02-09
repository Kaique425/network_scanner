from random import choice

import nmap

"""This class allow  us to scan all ips address and hosts 
   from the current machine """


class Network:
    def __init__(self, choice):
        self.choice = choice

    def networkscanner(self):
        network = "192.168.4.1/24"
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments="-sn")
        host_list = [(x, nm[x]["status"]["state"]) for x in nm.all_hosts()]
        return host_list


if __name__ == "__main__":
    D = Network("192.168.1.1/24")
    D.networkscanner()
