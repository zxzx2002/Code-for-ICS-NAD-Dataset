import pandas as pd

def label_protocol(row):
    sIP = row['sIPs']
    rIP = row['rIPs']
    
    if sIP == '192.168.10.102' and not rIP.startswith('192') and not rIP == '255.255.255.255' :
        return 'TCP'
    elif rIP == '192.168.10.102' and not sIP.startswith('192') and not sIP == '255.255.255.255' :
        return 'TCP'
    else:
        return 'BENIGN'
    protocal = row['protocol']
    #if sIP == '192.168.10.112':
        #return 'PORTSCAN'
    #else:
        #return "BENIGN"
    
try:
    df = pd.read_csv('D:/Schneider_tcpsynfin0_0710.csv', low_memory=False,encoding='utf-8',on_bad_lines='skip')
except UnicodeDecodeError:
    df = pd.read_csv('D:/Schneider_tcpsynfin0_0710.csv', encoding='ISO-8859-1',on_bad_lines='skip')


df['state'] = df.apply(label_protocol, axis=1)
df.to_csv('D:/Schneider_nmap_0710_0/Schneider_tcpsynfin0_0710.csv',index = False)