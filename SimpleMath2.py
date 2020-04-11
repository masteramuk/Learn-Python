
#setkan pemboleh ubah
pi=3.142

#Procedure menu()
def menu():
  print("\n....................................................")
  print("Menu Mengira Isi padu")
  print("....................................................")
  print("1. kuboid")
  print("2. silinder")
  print("3. kon")
  print("4. sfera")
  print("5. TAMAT~")
  print(".....................................................")

# Function dptPilihanPengguna()    
def dptPilihanPengguna():
    noPilihan = 0
    while (noPilihan < 1) or (noPilihan > 5):
        noPilihan = int(input("Pilihan anda [1 hingga 5]:"))
    return noPilihan  

# Procedure kiraCetak
def kiraCetak(jenisBentuk):
  if jenisBentuk == 1:
      panjang = float(input("Masukkan panjang(cm):"))
      lebar = float(input("Masukkan lebar(cm):"))
      tinggi = float(input("Masukkan tinggi(cm):"))
      kuboid = panjang*lebar*tinggi
      print ("\nisipadu KUBOID:", round(kuboid,2), "cm padu.") 
    
  elif jenisBentuk == 2 :
      tinggi = float(input("Masukkan tinggi(cm):"))
      jejari = float(input("Masukkan jejari(cm):")) 
      silinder = 2*pi*jejari*jejari*tinggi
      print ("\nIsipadu SILINDER:", round(silinder,2) ,"cm padu.")

  elif jenisBentuk == 3:
      tinggi = float(input("Masukkan tinggi(cm):"))
      jejari = float(input("Masukkan jejari(cm):"))
      kon = (1/3)*(pi*jejari*jejari)*tinggi
      print ("\nIsipadu KON:", round(kon,2) ,"cm padu.")

  elif jenisBentuk == 4:
      jejari = float(input("Masukkan jejari(cm):"))
      sfera = (4/3)*(pi*jejari*jejari*jejari)
      print ("\nIsipadu SFERA:", round(sfera,2) ,"cm padu.")  

# main.......................................................
aktif=1
while aktif == 1:
  menu()
  jenisBentuk=dptPilihanPengguna()
  if jenisBentuk==5:
      aktif=0
  else:
      kiraCetak(jenisBentuk)
print ("Terima kasih kerana mengunakan saya:)")
#............................................................
