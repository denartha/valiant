#!/usr/bin/python

import sys
from subprocess import call

host = sys.argv[1]

def banner(host):
	print "[*]IP info for host: " + host

def reverse_dns(host):
	call(["host", host])

banner(host)
reverse_dns(host)
