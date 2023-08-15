########THANKS TO DAPUNTA#########
def password(nama):
	pw = []
	nl = nama.lower().split(' ')
	if len(nl) > 1:
		nd = nl[0]
		nb = nl[-1]
		if len(nd) < 3:
			pw.append(nd+'12345')
		elif 2 < len(nd) < 6:
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
		else:
			pw.append(nd)
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
		if len(nb) < 3:
			pw.append(nb+'12345')
		elif 2 < len(nb) < 6:
			pw.append(nb+'123')
			pw.append(nb+'1234')
			pw.append(nb+'12345')
		else:
			pw.append(nb)
			pw.append(nb+'123')
			pw.append(nb+'1234')
			pw.append(nb+'12345')
	else:
		nd = nl[0]
		if len(nd) < 3:
			pw.append(nd+'12345')
		elif 2 < len(nd) < 6:
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
		else:
			pw.append(nd)
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
	if len(nama) > 5:
		pw.append(nama.lower())
	return(pw)

def panjang(nama):
	pw = []
	nl = nama.lower().split(' ')
	if len(nl) > 1:
		nd = nl[0]
		nb = nl[-1]
		if len(nd) < 3:
			pw.append(nd+'12345')
		elif 2 < len(nd) < 6:
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
		else:
			pw.append(nd)
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
		if len(nb) < 3:
			pw.append(nb+'12345')
		elif 2 < len(nb) < 6:
			pw.append(nb+'123')
			pw.append(nb+'1234')
			pw.append(nb+'12345')
		else:
			pw.append(nb)
			pw.append(nb+'123')
			pw.append(nb+'1234')
			pw.append(nb+'12345')
	else:
		nd = nl[0]
		if len(nd) < 3:
			pw.append(nd+'12345')
		elif 2 < len(nd) < 6:
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
		else:
			pw.append(nd)
			pw.append(nd+'123')
			pw.append(nd+'1234')
			pw.append(nd+'12345')
	if len(nama) > 5:
		pw.append(nama.lower())
		pw.append("sayang")
		pw.append("ganteng")
		pw.append("bondowoso")
		pw.append("sayangkamu")
		pw.append("123456")
		pw.append("sayangku")
		pw.append("sayang123")
		pw.append("bismillah")
		pw.append("anjing")
		pw.append("anakkontol")
		pw.append("anakngentot")
		pw.append("katasandi")
		pw.append("sandi123")
		pw.append("kontol")
		pw.append("rahasia")
		pw.append("doraemon")
		pw.append("kotabaru")
		pw.append("kotatua")
	return(pw)