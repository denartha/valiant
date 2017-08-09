#!/usr/bin/python

import json
import urllib
import sys
from subprocess import call

host = sys.argv[1]

def banner(host):
	print "[*]IP info for host: " + host

def reverse_dns(host):
	call(["host", host])

def virus_total_ip(host):
	 url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
	 parameters = {'ip': host, 'apikey': '65d2d3b5872ce5fa28eebea752486ee1aa9656dfcba0381fb6445938cff87321'}
	 response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
	 response_dict = json.loads(response)
	 print "[*]Virus Total Information",
	 print json.dumps(response_dict, indent=1)


banner(host)
reverse_dns(host)
virus_total_ip(host)
