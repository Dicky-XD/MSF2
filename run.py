import os
import logo as ngontol
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

if __name__ == "__main__":
	os.system("clear");ngontol.logomenu()
	print(f" {P}[{H}1{P}] Menu Facebook \n {P}[{H}2{P}] Menu Instagram")
	___pilihan__ = input(f" {P}[{U}?{P}] Pilih : ")
	if ___pilihan__ in ['1','01','001','a']:
		try:
			os.system("clear")
			os.system("python MSF2.py")
		except Exception as e:
			exit(str(e))
	elif ___pilihan__ in ['2','02','002','b']:
		try:
			os.system("clear")
			os.system("python ig.py")
		except Exception as e:
			exit(str(e))
	else:pass
