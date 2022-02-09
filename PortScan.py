import re
import socket

from Network_class import Network

""" Write all host an ip address in a file"""


def write_host_info(name, ip):
    with open("Host_info.txt", "a") as file:
        text = f"Hostname: {name} IP: {ip[0]} Status: {ip[1]} \n"
        print()
        file.write(text)


""" Write all ip that is unreachble """


def write_unreachble_ips(ip):
    with open("Unreachble_ips.txt", "a") as file:
        text = f"IP: {ip} \n"
        file.write(text)


""" This function get only the host name instead of 'example.teste299.local' """


def clean_host(host_specs):
    text = [w for w in re.split(r"[\.]+", host_specs[0]) if w != " "]
    clean_text = text[0]
    return clean_text


D = Network()
host_list = D.networkscanner()
for host_ip in host_list:
    try:
        print(f"IP found: {host_ip[0]}")
        host_info = socket.gethostbyaddr(host_ip[0])
        host_name = clean_host(host_info)
        write_host_info(host_name, host_ip)

    except Exception:
        write_unreachble_ips(host_ip[0])
        print(f"This IP: {host_ip[0]} is unreachble .")
        pass
