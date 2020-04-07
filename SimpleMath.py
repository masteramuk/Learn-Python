
# Procedure menu()
def menu():
    print("Kalkulator Bermenu")
    print("1. Tambah")
    print("2. Tolak")
    print("3. Darab")
    print("4. Bahagi")
    print("5. Kuasa")
    print("6. Punca Kuasa")
    print("7. Tamat")

# Function dptPilihanPengguna()    
def dptPilihanPengguna():
    noPilihan = 0
    while (noPilihan < 1) or (noPilihan > 7):
        noPilihan = int(input("Pilihan anda [1 hingga 7]:"))
    return noPilihan    

#Function dptDuaNombor()
def dptDuaNombor():
  nombor1 = int(input("Masukkan nombor pertama: "))
  nombor2 = int(input("Masukkan nombor kedua: "))
  return nombor1, nombor2

#Function dptSatuNombor()
def dptSatuNombor():
  nombor1 = int(input("Masukkan nombor pertama: "))
  nombor2 = 0
  return nombor1, nombor2

#Procedure kiraCetak()
def kiraCetak(jenisOperator, a, b):
  if jenisOperator == 1:
    print("Output: " + str(a) + " + " + str(b) + " = " + str(a + b) +"\n")
  elif jenisOperator == 2:
    print("Output:" + str(a) + "-" + str(b) + "=" + str(a-b) +"\n")
  elif jenisOperator == 3:
    print("Output:"+ str(a) + " * " + str(b) + " = " + str(a * b) +"\n") 
  elif jenisOperator == 4:
    print("Output:" + str(a) + "/" + str(b) + "=" + str(a/b) +"\n")
  elif jenisOperator == 5:
    print("Output:" + str(a) + "**" + str(b) + "=" + str(a**b) +"\n" )
  elif jenisOperator == 6:
    import math
    print(math.sqrt(a))  
  
#main-------------------------------------------------------------------7
aktif = 1
while aktif == 1:
    menu()
    jenisOperasi = dptPilihanPengguna()
    if jenisOperasi == 7:
      aktif = 0
    elif jenisOperasi == 6:
      [nom1, nom2] = dptSatuNombor()
      kiraCetak(jenisOperasi, nom1, nom2 )
    else:
      [nom1, nom2] = dptDuaNombor()
      kiraCetak(jenisOperasi, nom1, nom2 )
print("Terima kasih kerana menggunakan saya.")

#----------------------------------------------------------------------------------            





















