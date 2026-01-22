
secondi= int(input("Inserire secondi:"))
minuti= int(input("Inserire minuti:"))
ore= int(input("Inserire ore:"))
giorni= int(input("Inserire giorni:"))

minuti_sec= minuti*60
ore_sec= ore*60*60
giorni_sec= giorni*24*60*60

secondi_totali= secondi+minuti_sec+ore_sec+giorni_sec
print("Secondi totali:",secondi_totali)
