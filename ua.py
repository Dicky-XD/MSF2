# THANKS FOR LATIF176
#####################
import requests
from requests import *
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import random,os,time
RED_MAGIC = '\x03\xf3\r\nd\x83\x8e^'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda
y = "\033[0m"
z = "\033[1;92m"
x = "\033[1;97m"
I='\x1b[0;32m'
C='\x1b[0;36m'
R = "\033[1;91m"
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
Q="\x1b[00m"
U = '\x1b[1;95m'
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'
p = '\x1b[1;97m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
d = '\x1b[90;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'   
g = '\33[3;1m'
my_color = [
 P, M, H, K, B, U, O, N, j, a, b, d, u, o, h, m, N, k]
ior = random.choice(my_color)
os.system("rm -rf data/useragents.txt")
___________ugen__________ = []
browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
hitungan = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
build = random.choice(['QP1A.','PPR1.','TP1A.','TKQ1.','RKQ1.','SP1A.','RP1A.','PKQ1.'])
android_version = random.choice(['7', '8', '9', '10', '11', '12', '13'])
v1 = str(random.choice([f"RMXJ120H",f"RMXJ120F",f"RMXJ120M",f"RMXJ111M",f"RMXJ111F",f"RMXJ110H",f"RMXJ110G",f"RMXJ110F",f"RMXJ110M",f"RMXJ105H",f"RMXJ105Y",f"RMXJ105B",f"RMXJ106H",f"RMXJ106F",f"RMXJ106B",f"RMXJ106M",f"RMXJ200F",f"RMXJ200M",f"RMXJ200G",f"RMXJ200H",f"RMXJ200F",f"RMXJ200GU",f"RMXJ260M",f"RMXJ260F",f"RMXJ260MU",f"RMXJ260F",f"RMXJ260G",f"RMXJ200BT",f"RMXG532G",f"RMXG532M",f"RMXG532MT"]))
v3 = str(random.choice([f'RMXG390Y', f'RMXG390Y', f'RMXG525F', f'RMXG9006W', f'RMXG9209K', f'RMX316U',
                f'RMX318ML', f'RMX318MZ', f'RMX318MZ', f'RMX360GY', f'RMXG110B', f'RMXG110H',
                f'RMXG110M', f'RMXG130BT', f'RMXG130BU', f'RMXG130E', f'RMXG130H', f'RMXG130HN',
                f'RMXG130M', f'RMXG130U', f'RMXG150N0', f'RMXG150NK', f'RMXG150NL', f'RMXG150NS',
                f'RMXG155S', f'RMXG1600', f'RMXG1600', f'RMXG160N', f'RMXG1650', f'RMXG165N',
                f'RMXG30HN', f'RMXG310H', f'RMXG310HN', f'RMXG310R', f'RMXG310R5', f'RMXG3139',
                f'RMXG3139D', f'RMXG313F', f'RMXG313H', f'RMXG313HN', f'RMXG313HU', f'RMXG313HY',
                f'RMXG313HZ', f'RMXG313M', f'RMXG313ML', f'RMXG313MU', f'RMXG313MY', f'RMXG313U',
                f'RMXG316F', f'RMXG316HU', f'RMXG316M', f'RMXG316ML', f'RMXG316MY', f'RMXG318',
                f'RMXG318H', f'RMXG318HZ', f'RMXG318M', f'RMXG318ML', f'RMXG318MZ', f'RMXG350',
                f'RMXG3502', f'RMXG3502C', f'RMXG3502I', f'RMXG3502L', f'RMXG3502T', f'RMXG3502U',
                f'RMXG3508', f'RMXG3508I', f'RMXG3508J', f'RMXG3509', f'RMXG3509I', f'RMXG350E',
                f'RMXG350L', f'RMXG350M', f'RMXG350X', f'RMXG3518', f'RMXG3556D', f'RMXG3558',
                f'RMXG3559', f'RMXG355H', f'RMXG355HN', f'RMXG355HQ', f'RMXG355M', f'RMXG3568V',
                f'RMXG357', f'RMXG357FZ', f'RMXG357FZ', f'RMXG357M', f'RMXG3586V', f'RMXG3588V',
                f'RMXG3589W', f'RMXG3606', f'RMXG3608', f'RMXG3609', f'RMXG360AZ', f'RMXG360BT',
                f'RMXG360F', f'RMXG360F', f'RMXG360FY', f'RMXG360G', f'RMXG360GY', f'RMXG360H',
                f'RMXG360HU', f'RMXG360M', f'RMXG360P', f'RMXG360T', f'RMXG360V', f'RMXG361F',
                f'RMXG361H', f'RMXG361HU', f'RMXG368T', f'RMXG3812', f'RMXG3812B', f'RMXG3815',
                f'RMXG3818', f'RMXG3818ZM', f'RMXG3819D', f'RMXG3858', f'RMXG386F', f'RMXG386T',
                f'RMXG386T1', f'RMXG386U', f'RMXG386W', f'RMXG388F', f'RMXG389F', f'RMXG390F',
                f'RMXG390W', f'RMXG390Y', f'RMXG398FN', f'RMXG5108', f'RMXG5108Q', f'RMXG5109',
                f'RMXG5306W', f'RMXG5308W', f'RMXG5309W', f'RMXG530A', f'RMXG530AZ', f'RMXG530BT',
                f'RMXG530F', f'RMXG530FQ', f'RMXG530FZ', f'RMXG530H', f'RMXG530M', f'RMXG530MU',
                f'RMXG530P', f'RMXG530R4', f'RMXG530R7', f'RMXG530T', f'RMXG530T1', f'RMXG530W',
                f'RMXG530Y', f'RMXG530YZ', f'RMXG531BT', f'RMXG531F', f'RMXG531H', f'RMXG531M',
                f'RMXG531Y', f'RMXG532F', f'RMXG532G', f'RMXG532M', f'RMXG532MT', f'RMXG5500',
                f'RMXG550FY', f'RMXG550T', f'RMXG550T1', f'RMXG550T2', f'RMXG5510', f'RMXG5520',
                f'RMXG5528', f'RMXG570', f'RMXG5700', f'RMXG570F', f'RMXG570M', f'RMXG570Y',
                f'RMXG6000', f'RMXG600F', f'RMXG600F', f'RMXG600FY', f'RMXG600S', f'RMXG6100',
                f'RMXG610F', f'RMXG610FD', f'RMXG610K', f'RMXG610L', f'RMXG610M', f'RMXG610S',
                f'RMXG610Y', f'RMXG611F', f'RMXG611FF', f'RMXG611FFDD', f'RMXG611K', f'RMXG611L',
                f'RMXG611M', f'RMXG611M', f'RMXG611MT', f'RMXG611S', f'RMXG615F', f'RMXG615FU',
                f'RMXG6200', f'RMXG710', f'RMXG7102', f'RMXG7102T', f'RMXG7105', f'RMXG7105H',
                f'RMXG7105K', f'RMXG7105L', f'RMXG7106', f'RMXG7108', f'RMXG7108V', f'RMXG7109',
                f'RMXG710L', f'RMXG710S', f'RMXG710x', f'RMXG715F', f'RMXG715FN', f'RMXG715U',
                f'RMXG715U1', f'RMXG715W', f'RMXG715X', f'RMXG7200', f'RMXG7202', f'RMXG720AX',
                f'RMXG720N0', f'RMXG730A', f'RMXG730V', f'RMXG730W8', f'RMXG7508Q', f'RMXG7509',
                f'RMXG750A', f'RMXG750H', f'RMXG770F', f'RMXG770U1', f'RMXG780F', f'RMXG780G',
                f'RMXG780X', f'RMXG7810', f'RMXG781B', f'RMXG781BR', f'RMXG781N', f'RMXG781U1',
                f'RMXG781V', f'RMXG800A', f'RMXG800F', f'RMXG800H', f'RMXG800M', f'RMXG800R4',
                f'RMXG800Y', f'RMXG820A', f'RMXG8508S', f'RMXG850A', f'RMXG850F', f'RMXG850FQ',
                f'RMXG850K', f'RMXG850M', f'RMXG850S', f'RMXG850W', f'RMXG850X', f'RMXG850Y',
                f'RMXG860P', f'RMXG870A', f'RMXG870D', f'RMXG870F', f'RMXG870F0', f'RMXG870W',
                f'RMXG8750', f'RMXG8850', f'RMXG8858', f'RMXG885F', f'RMXG885K', f'RMXG885L',
                f'RMXG885S', f'RMXG885X', f'RMXG885Y', f'RMXG8870', f'RMXG887F', f'RMXG887N',
                f'RMXG888N0', f'RMXG889A', f'RMXG889G', f'RMXG890A', f'RMXG891', f'RMXG891A',
                f'RMXG892A', f'RMXG892A', f'RMXG892U', f'RMXG9006V', f'RMXG9008V', f'RMXG9009D',
                f'RMXG900A', f'RMXG900AZ', f'RMXG900F', f'RMXG900FD', f'RMXG900FQ', f'RMXG900H',
                f'RMXG900I', f'RMXG900J', f'RMXG900K', f'RMXG900L', f'RMXG900M', f'RMXG900MD',
                f'RMXG900P', f'RMXG900R4', f'RMXG900R6', f'RMXG900R7', f'RMXG900S', f'RMXG900T',
                f'RMXG900T1', f'RMXG900T3', f'RMXG900V', f'RMXG900W8', f'RMXG901F', f'RMXG903M',
                f'RMXG903W', f'RMXG906K', f'RMXG906L', f'RMXG906S', f'RMXG906SKL', f'RMXG9092',
                f'RMXG9098', f'RMXG9198', f'RMXG9200', f'RMXG9208', f'RMXG9209', f'RMXG9209',
                f'RMXG920A', f'RMXG920AZ', f'RMXG920F', f'RMXG920FQ', f'RMXG920G1', f'RMXG920I',
                f'RMXG920K', f'RMXG920L', f'RMXG920P', f'RMXG920R4', f'RMXG920R6', f'RMXG920R7',
                f'RMXG920S', f'RMXG920T', f'RMXG920T1', f'RMXG920V', f'RMXG920W8', f'RMXG920X',
                f'RMXG925', f'RMXG9250', f'RMXG925A', f'RMXG925F', f'RMXG925FQ', f'RMXG925I',
                f'RMXG925ID', f'RMXG925K', f'RMXG925L', f'RMXG925P', f'RMXG925R4', f'RMXG925R6',
                f'RMXG925R7', f'RMXG925S', f'RMXG925T', f'RMXG925V', f'RMXG925W8', f'RMXG925X',
                f'RMXG925X', f'RMXG925Z', f'RMXG9280', f'RMXG9287', f'RMXG9287C', f'RMXG928A',
                f'RMXG928C', f'RMXG928F', f'RMXG928G', f'RMXG928i', f'RMXG928K', f'RMXG928L',
                f'RMXG928N', f'RMXG928N0', f'RMXG928P', f'RMXG928R4', f'RMXG928S', f'RMXG928T',
                f'RMXG928V', f'RMXG928W8', f'RMXG928X', f'RMXG9298', f'RMXG9300', f'RMXG9308',
                f'RMXG930A', f'RMXG930AZ', f'RMXG930F', f'RMXG930FD', f'RMXG930K', f'RMXG930L',
                f'RMXG930P', f'RMXG930R4', f'RMXG930R6', f'RMXG930R7', f'RMXG930S', f'RMXG930SKL',
                f'RMXG930T', f'RMXG930T1', f'RMXG930U', f'RMXG930V', f'RMXG930VC', f'RMXG930VL',
                f'RMXG930W', f'RMXG930W8', f'RMXG930X', f'RMXG9350', f'RMXG935A', f'RMXG935AU',
                f'RMXG935D', f'RMXG935F', f'RMXG935FD', f'RMXG935J', f'RMXG935K', f'RMXG935L',
                f'RMXG935P', f'RMXG935R4', f'RMXG935R6', f'RMXG935R7', f'RMXG935S', f'RMXG935T',
                f'RMXG935T1', f'RMXG935U', f'RMXG935V', f'RMXG935VC', f'RMXG935W', f'RMXG935W8',
                f'RMXG935X', f'RMXG950', f'RMXG9500', f'RMXG9508', f'RMXG950D', f'RMXG950F',
                f'RMXG950FD', f'RMXG950J', f'RMXG950N', f'RMXG950U', f'RMXG950U1', f'RMXG950W',
                f'RMXG950X', f'RMXG950XC', f'RMXG955', f'RMXG9550', f'RMXG9558', f'RMXG955F',
                f'RMXG955FD', f'RMXG955J', f'RMXG955N', f'RMXG955U', f'RMXG955U1', f'RMXG955W',
                f'RMXG955X', f'RMXG955XU', f'RMXG9600', f'RMXG9608', f'RMXG960F', f'RMXG960FD',
                f'RMXG960L', f'RMXG960N', f'RMXG960U', f'RMXG960U1', f'RMXG960US', f'RMXG960UX',
                f'RMXG960W', f'RMXG960X', f'RMXG960XU', f'RMXG9650', f'RMXG965F', f'RMXG965FD',
                f'RMXG965J', f'RMXG965N', f'RMXG965U', f'RMXG965U1', f'RMXG965UX', f'RMXG965W',
                f'RMXG965X', f'RMXG965XU', f'RMXG9700', f'RMXG9708', f'RMXG970F', f'RMXG970FD',
                f'RMXG970N', f'RMXG970U', f'RMXG970U1', f'RMXG970W', f'RMXG970X', f'RMXG970XC',
                f'RMXG970XN', f'RMXG970XU', f'RMXG9730', f'RMXG9730Z', f'RMXG9738', f'RMXG973C',
                f'RMXG973D', f'RMXG973F', f'RMXG973J', f'RMXG973N', f'RMXG973U', f'RMXG973U1',
                f'RMXG973W', f'RMXG973XC', f'RMXG973XN', f'RMXG973XU', f'RMXG9750', f'RMXG9758',
                f'RMXG975F', f'RMXG975FD', f'RMXG975N', f'RMXG975U', f'RMXG975U1', f'RMXG975W',
                f'RMXG975XC', f'RMXG975XN', f'RMXG975XU', f'RMXG977B', f'RMXG977N', f'RMXG977P',
                f'RMXG977T', f'RMXG977U', f'RMXG97xF', f'RMXG980A', f'RMXG980F', f'RMXG9810',
                f'RMXG981A', f'RMXG981B', f'RMXG981C', f'RMXG981N', f'RMXG981U', f'RMXG981U1',
                f'RMXG981V', f'RMXG981W', f'RMXG985F', f'RMXG985X', f'RMXG9860', f'RMXG986B',
                f'RMXG986N', f'RMXG986U', f'RMXG986U1', f'RMXG986W', f'RMXG9880', f'RMXG988B',
                f'RMXG988BR', f'RMXG988N', f'RMXG988U', f'RMXG988W', f'RMXG990B', f'RMXG990E',
                f'RMXG990U', f'RMXG9910', f'RMXG991BR', f'RMXG991N', f'RMXG991XU', f'RMXG9960',
                f'RMXG9968', f'RMXG996BR', f'RMXG996N', f'RMXG996X', f'RMXG996XU', f'RMXG9980',
                f'RMXG9988', f'RMXG998N', f'RMXG998X', f'RMXG998XU', f'RMXJ730F', f'RMXM017F',]))
android_model =  str(random.choice([v1,v3]))
randomct = str(random.choice(['ar-ar','bg-bg','bs-ba','ca-es','da-dk','el-gr','es-la','es-es','fa-ir','fi-fi','fr-fr','fr-ca','hi-in','hr-hr','id-id','it-it','ko-kr','mk-mk','ms-my','pl-pl','pt-br','pt-pt','ro-ro','sl-si','sr-rs','th-th','vi-vn']))
########THANKS TO LATIF#######
def get_all_platforms(url = "https://user-agents.net"):
	no = 0
	r = BeautifulSoup(requests.get(url+"/devices/mobiles",headers={"user-agent":"chrome"}).text, "html.parser")
	data = {}
	for x in r.find("ul",{"class":"compact_list"}).findAll("li"):
		no += 1
		data.update({str(no):{"nama":x.find("a").string,"href":x.find("a").get("href")}})
	return data


def getUa(data, url = "https://user-agents.net"):
	no = 0
	v = data['href']
	anjing = []
	userA = []
	try:
		url = url+v
		r = get(url)
		b = bs(r.content,'html.parser')
		test = get(url).text.splitlines()
		for link in b.find('ul',{'class':'agents_list'}).find_all('a'):
			try:
				userA.append(link.text)
				for x in userA:
					uaa = x
				print(end='\r  ╰─> Mengambil (%s) Useragent'%(len(userA)))
			except:pass
		print("")
	except Exception as e:
		print(f'{P} [{M}!{P}] Gagal Mengambil Useragent Silahkan Pilih Lagi');cariuanya() 
	except KeyboardInterrupt:pass
	if len(userA) != 0:
		f = open('data/useragents.txt','w')
		for ua in userA:
			f.write(ua+'\n')
			
def cariuanya():
	menu = get_all_platforms()
	print('-'*70)
	for k in menu:
		print(f"  [{k}] {H}{menu[k]['nama']}{P}")
	try:
		print('-'*70)
		chose = sol().input(f"  DickyXD > Choose Type : ")
		getUa(menu[chose])
	except IndexError:
		print(f'{P} [{M}!{P}] Pilihan Tidak Ada');cariuanya() 

#######USERAGENT KHUSUS FACEBOOK########
def random_useragent(total): ########THANKS TO ROZHAK#######
	for _ in range(total):
		useragent7 = f"Opera/9.80 (S60; SymbOS; Opera Mobi/1181; U; en-GB) Presto/2.5.28 Version/10.1"
		useragent6 = f"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012211514; U; en) Presto/2.6.35 Version/10.1"
		useragent5 = f"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012272315; U; pl) Presto/2.7.60 Version/10.5"
		useragent4 = f"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"
		useragent3 = f"Mozilla/4.0 (compatible; Windows Mobile; WCE; Opera Mobi/WMD-50433; U; de) Presto/2.4.13 Version/10.00"
		useragent2 = f"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00"
		useragent   = f"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1011151731; U; de) Presto/2.5.28 Version/10.1"
		redbul = str(random.choice([useragent7,useragent6,useragent5,useragent4,useragent3,useragent2,useragent]))
		return redbul

def random_ua_custom(): ########THANKS TO DAPUNTA#######
	for _ in range(900):
		_file_ = open('data/useragents.txt','r').read()
		if 'Android' in str(_file_):
			ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
			os_ver = 'Android ' + str(random.randrange(10,13))
			ua1 = _file_.replace(ad_ver,os_ver)
		else: ua1 = _file_
		if 'Build' in str(_file_):
			od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
			bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A','PKQ1'])
			dv_ver = random.randrange(100000,250000)
			sd_ver = random.randrange(1,10)
			nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
			ua2 = ua1.replace(od_ver,nw_str)
		else: ua2 = ua1
		if 'Chrome' in str(_file_):
			ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
			a = random.randrange(110,113)
			b = random.randrange(1000,10000)
			c = random.randrange(10,100)
			ch_ver = f'{a}.0.{b}.{c}'
			ch_new = 'Chrome/' + str(ch_ver)
			ua3 = ua2.replace(ch_old,ch_new)
		else: ua3 = ua2
		return(ua3)

def vers():
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,49.0.0.15.89,48.0.0.15.98,47.0.0.16.96,46.0.0.15.96,45.0.0.17.93,44.0.0.9.93,43.0.0.10.97,42.0.0.19.95,41.0.0.13.92,40.0.0.14.95,39.0.0.19.93,38.0.0.13.95,37.0.0.21.97,36.0.0.13.91,35.0.0.20.96,34.0.0.12.93,33.0.0.11.92,32.0.0.16.94,31.0.0.10.94,30.0.0.12.95,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi

def ua_khusus_instagram():
		rr = random.randint;rc = random.choice;dpis = random.choice(["240dpi", "540dpi","480dpi", "320dpi", "440dpi", "640dpi","133dpi","320dpi","515dpi","160dpi","332dpi","640dpi","240dpi","120dpi","800dpi","480dpi","225dpi","768dpi","216dpi","1024dpi","213dpi","450dpi"])
		pxl=rc(["1440x2560","720x1280","480x744","1080x2076","1080x1920","1080x1794","1080x1920","800x1216","1080x1776","480x854","720x1515","2400x1080","3200x1440","1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"]);akhir = rr(399993134,444761830);com=rc(["qcom","mt6833","mt6765","mt8168","samsungexynos8895","hi3635","samsungexynos9810"]);ver = rc(["7","8","9","10","11","12","13"]);si = rr(72,120);andro=rc([f"30/{rr(4,23)}",f"31/{rr(4,13)}",f"29/{rr(4,13)}"])
		xiaomi=rc(['M2004J19C','Redmi Note 9S','Pixel','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G'])
		mod=rc(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','onyx','lima','trlte','alto5_sporty','D2105','dreamlte','mido','HWGRA','OnePlus5','mt8168','JWT','mt6582','astro','marlin','raphael','vili','taoyao','ginkgo','renoir','haydn'])
		versi = vers()
		uami=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/Redmi; {xiaomi}; {mod}; {com}; in_ID)")
		uami2=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Pixel; {xiaomi}; {mod}; {com}; en_US)")
		uami3=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; {dpis}; {xiaomi}; {mod}; {com}; pt_BR)")
		uami4=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; samsung; SM-N910F; {mod}; {com}; pt_PT)")
		uami5=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; TCL; 7048X; {mod}; {com}; pt_PT)")
		uami6=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Sony; D2105; {mod}; {com}; ru_RU)")
		uami7=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; samsung; SM-G950F; {mod}; {com}; ru_UA)")
		uami8=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/xiaomi; Redmi Note 4; {mod}; {com}; uk_UA)")
		uami9=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; HUAWEI; HUAWEI GRA-L09; {mod}; {com}; hu_HU)")
		uami10=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; OnePlus; ONEPLUS A5000; {mod}; {com}; ru_UA)")
		uami11=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Amazon; KFONWI; {mod}; {com}; en_US)")
		uami12=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; SHARP/KDDI; SHV41; {mod}; {com}; ja_JP)")
		uami13=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; 1201; {mod}; {com}; in_ID)")
		uami14=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; motorola; motorola one fusion; {mod}; {com}; pt_PT)")
		uami15=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Redmi; {xiaomi}; {mod}; {com}; in_ID)")
		uami16=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Realme; {xiaomi}; {mod}; {com}; in_ID)")
		uanyates = rc([uami,uami2,uami3,uami4,uami5,uami6,uami7,uami8,uami9,uami10,uami11,uami12,uami13,uami14,uami15,uami16])
		return uanyates
	
