import concurrent.futures
import requests
import os
import time
proxysource = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all"
#--> Style Warna
Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
h = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu
R = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'
########color rich########
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
os.system("rm -rf good.txt")

session = requests.Session()
session.headers.update({"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
proxy_list = []
def check(proxy, idx, total):
    try:
        response = session.get("https://ipwho.is/", proxies={"http": "socks4://" + str(proxy)}, timeout=3)
        if response.status_code == 200:
            proxy_list.append({'http': 'socks4://'+str(proxy)})
            print(end='\r ['+h+'•'+P+'] Mengumpulkan (%s) Proxy'%(len(proxy_list)),flush=True)
            open('good.txt','a+').write(proxy + "\n")
    except (requests.exceptions.ProxyError, requests.exceptions.Timeout, requests.exceptions.ConnectTimeout):pass
        

def main():
    proxylist = requests.get(proxysource).text.splitlines()
    print(P+' ['+h+'•'+P+'] Total Proxy Ditemukan : '+str(len(proxylist)))
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for idx, proxy in enumerate(proxylist, start=1):
            executor.submit(check, proxy, idx, len(proxylist))
    print('\n--------------------------------------------------------------')
