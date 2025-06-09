# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:28:22 2024

@author: HP
"""
import pandas as pd

def label_protocol(value):
    if value['protocol'] == 'IPV4-ICMP':
        return 'PINGOFDEATH'
    else:
        return 'BENIGN'
def label_sIPs(row):
    if (row['rIPs'] == '192.168.10.112' ):
        return 'NMAP'
    else:
        return 'BENIGN'
    
try:
    df = pd.read_csv('D:\\Schneider_ackflood_fast_0710-.csv', low_memory=False,encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('D:\\Schneider_ackflood_fast_0710-.csv', encoding='ISO-8859-1')
#df['state'] = df['sIPs'].apply(label_protocol)
#df['state'=='TCPFIN1']['state'] = df['sIPs'].apply(label_sIPs)

df['state'] = 'BENIGN'

def check_conditions(row):
    if (row['sIPs'] == '192.168.10.102' and not row['rIPs'].startswith('192.168') and row['rIPs'] != '0.0.0.0' and row['rIPs']!='255.255.255.255'):
        return 'ACKFLOOD'
    elif (row['rIPs'] == '192.168.10.102' and not row['sIPs'].startswith('192.168') and row['sIPs'] != '0.0.0.0'and row['rIPs']!='255.255.255.255'):
        return 'ACKPFLOOD'
    else:
        return 'BENIGN'

df['state'] = df.apply(check_conditions, axis=1)

df.to_csv('D:\\Schneider_ackflood_fast_0710.csv', index=False)
