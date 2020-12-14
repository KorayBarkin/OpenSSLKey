import os.path
import subprocess

def execute_it(cmd):
	output = subprocess.check_output(['bash','-c',cmd])
	return output.decode("utf-8")

def fonksiyon1(degisken, numara):
	cmd1 = "openssl genrsa -out keys/"+degisken+" "+numara
	execute_it(cmd1) 
	return degisken, numara
def fonksiyon2(degisken2,isim):
	cmd2 = "openssl req -new -x509 -days 1460 -subj '/C=TR/ST=Ankara/L=Cankaya/O=aciklab/CN=pardus3' -key keys/"+degisken2+"  -out keys/KokCA.crt"
	execute_it(cmd2)
	return degisken2,isim
def fonksiyon3(isim):
	cmd3 = "openssl req -new -key keys/"+isim+" -out keys/AraCA.csr -subj '/C=TR/ST=Ankara/L=Cankaya/O=aciklab/CN=pardus3'"
	execute_it(cmd3)
	return isim
def fonksiyon4(isim1,isim2,isim3):
	cmd4 = "openssl x509 -req -days 730 -in keys/"+isim1+" -CA keys/"+isim2+" -CAkey keys/"+isim3+" -CAcreateserial -out keys/AraCA.crt"
	execute_it(cmd4)
	return isim1,isim2,isim3
def fonksiyon5(csrtalebi):
	cmd6 = "openssl req -new -key keys/"+csrtalebi+" -out keys/Sunucu.csr -subj '/C=TR/ST=Ankara/L=Cankaya/O=aciklab/CN=pardus3'"
	execute_it(cmd6)
	return csrtalebi
def fonksiyon6(degisken1,degisken2,degisken3):
	cmd7 = "openssl x509 -req -days 365 -in "+degisken1+" -CA "+degisken2+" -CAkey "+degisken3+" -set_serial 0101 -out Sunucu.crt -sha256"
	execute_it(cmd7)
	return degisken1,degisken2,degisken3
degisken, numara = fonksiyon1("KokCA.key","4096")
degisken2,isim = fonksiyon2("KokCA.key","pardus3")
degisken, numara = fonksiyon1("AraCA.key","4096")
fonksiyon3("AraCA.key")
isim1,isim2,isim3 = fonksiyon4("AraCA.csr", "KokCA.crt", "KokCA.key")
degisken, numara = fonksiyon1("Sunucu.key","2048")
fonksiyon5("Sunucu.key")
degisken1,degisken2,degisken3 = fonksiyon6("Sunucu.csr","AraCA.crt","AraCA.key")
