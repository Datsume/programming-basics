
cents_utente= int(input ("Inserire Cents:"))
spesa= int(200)
reso= cents_utente-spesa

Penny = int(1)
Nickel = int(5) 
Dime = int(10) 
Quarter = int(25) 
Loonie = int(100) 
Toonie = int(200) 

monete_toonie= reso//Toonie
print ("Toonie:", monete_toonie)
reso_toonie= reso-(Toonie*(int(monete_toonie)))

monete_loonie= reso_toonie//Loonie
print ("Loonie:", monete_loonie)
reso_loonie= reso_toonie-(Loonie*monete_loonie)

monete_quarter= reso_loonie//Quarter
print ("Quarter", monete_quarter)
reso_quarter= reso_loonie-(Quarter*monete_quarter)

monete_dime= reso_quarter//Dime
print ("Dime:", monete_dime)
reso_dime= reso_quarter-(Toonie*monete_dime)

monete_nickel= reso_dime//Nickel
print ("Nickel:", monete_nickel)
reso_nickel= reso_dime-(Nickel*monete_nickel)

monete_penny= reso_nickel//Penny
print ("Penny", monete_penny)
reso_penny= reso_nickel-(Nickel*monete_penny)

