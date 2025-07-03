# Mache eine Variabel namens seite_a und ein float ist.
# Der wert der Variabel gibt der User durch die input funktion ein (auf der Konsole steht "a= " und hier gibt man eine Zahl ein.
# (Mit enter wird Bestätigt)
seite_a = float(input("a=\n"))
# Hier noch mal das gleiche mit seite_b und "b= "
seite_b = float(input("b=\n"))
# Mache ein if welches schaut ob beide Zahlen grösser als 0 sind.
if (seite_a > 0) and (seite_b > 0):
# Multiplizere beide Variabeln miteinander und schreibe das resultat in die Variable A.
    A = seite_a * seite_b
# Printen sie die "Rechtecksfläche= " und danach den Wert der Variabel A.
    print("Rechtecksfläche=",A)
# Im else vom if wird eine Errormeldung gedrückt "Error: Nur Positive Zahlen sind eraubt"
else:
    print("Error: Nur Positive Zahlen sind eraubt\n")
    
