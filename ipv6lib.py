#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import ipaddress

def check_ip(arg):
    '''This function checks: the passed arg an is ip address or not. '''
    
    try:
        if ipaddress.ip_address(arg): # includes ipv6 addresses!
            return True
        else:
        	return False
    except ValueError:
        pass

def ipv6_is_global(arg):
    '''This function checks: the passed arg is a global ipv6 address or not. '''
    
    try:
        if ipaddress.ip_address(arg).is_global: # includes ipv6 addresses!
            return True
        else:
        	return False
    except ValueError:
        pass

if __name__ == '__main__':
	print('None - is not defined\n')
	for i in sys.argv[1:]:
		print(i, 'Is an ip address?', check_ip(i))
		print(i, "Is a global ipv6?", ipv6_is_global(i))
