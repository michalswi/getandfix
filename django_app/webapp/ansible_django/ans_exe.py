#!/usr/bin/env python

#from ...models import DbClient, DbSystem, DbServer, DbCommand, DbLog

def get_ajax(n):
  print n 
  return """
192.168.66.6 | SUCCESS | rc=0 >>
Architecture:          x86_64                                                                                                                              
CPU op-mode(s):        32-bit, 64-bit                                                                                                                      
Byte Order:            Little Endian                                                                                                                       
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 61
Model name:            Intel Core Processor (Broadwell)
Stepping:              2
CPU MHz:               2496.004
BogoMIPS:              4992.00
Virtualization:        VT-x
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              4096K
NUMA node0 CPU(s):     0
"""
