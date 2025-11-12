"""
=========================================
 Collatz-Folgen Tool
-----------------------------------------
 Autor: Rodin
 Version: 1.0
 Datum: November 2025
 Sprache: Python 3
 Bibliotheken: tkinter, matplotlib
-----------------------------------------
 Beschreibung:
 Dieses Tool visualisiert die berühmte Collatz-Folge
 (auch bekannt als "3n + 1 Problem"). Es bietet drei Modi:

 1️⃣ Einzelne Zahl – Berechnet und plottet die Collatz-Folge für eine Startzahl.
 2️⃣ Liste von Zahlen – Zeigt mehrere Folgen in einem Diagramm.
 3️⃣ Bereich – Berechnet und plottet alle Zahlen zwischen zwei Grenzen.

 Jede Folge zeigt:
   - den Startwert (grün markiert),
   - den höchsten Wert der Folge (blau),
   - und den Endpunkt bei 1 (rot).

 Entwickelt von Rodin im Rahmen des Informatikprojekts
 "Visualisierung mathematischer Folgen".
 Viel spaß :)
=========================================
"""


from tkinter import *
import matplotlib.pyplot as plt


operation_labels = ["eine zahl simulieren\n z.B. 5","liste von zahlen\nz.B. 3,6,9...","gewisser Bereich\n(einschlieslich!) z.B. 1-10"]
x_positions_operation_labels = [100, 400, 700]

berechne_btn_list = []
entry_list = []
zahl = None
zahlen_liste = []


def BERECHNEFOLGEZAHL(n):
    """
    Berechnet die Collatz-Folge für eine einzelne Zahl n
    und gibt sie als Liste zurück.
    """
    folge = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        folge.append(n)
    return folge
def BERECHNEFOLGE(liste_von_zahlen):
    """
    Berechnet die Collatz-Folgen für alle Zahlen in 'liste_von_zahlen'
    und gibt ein Dictionary zurück: {zahl: folge}
    """
    folgen_dict = {}
    for n in liste_von_zahlen:
        folge = [n]
        temp = n
        while temp != 1:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = 3 * temp + 1
            folge.append(temp)
        folgen_dict[n] = folge
    return folgen_dict


def get_nums(index):
    global zahl, zahlen_liste
    zahlen_liste.clear()
    zahl = entry_list[index].get()

    if index == 0:  # Einzelzahl
        try:
            zahl = int(zahl)
            #print(zahl)
            folge = BERECHNEFOLGEZAHL(zahl)
            PLOTT_EINZELZAHL(folge)
        except:
            print("Ungültige Zahl.")
    
    elif index == 1:  # Komma-getrennte Liste
        try:
            # String in Liste von Zahlen umwandeln
            zahlen_liste = [int(x.strip()) for x in zahl.split(",")]
            #print(zahlen_liste)
            folge = BERECHNEFOLGE(zahlen_liste)
            PLOTT_LISTE(folge)
        except:
            print("Ungültige eingabe.")
    
    elif index == 2:  # Bereich
        try:
            start, ende = [int(x.strip()) for x in zahl.split("-")]
            if start >= ende:
                raise ValueError
            zahlen_liste = list(range(start, ende + 1))
            #print(zahlen_liste)
            folge = BERECHNEFOLGE(zahlen_liste)
            PLOTT_BEREICH(folge)
        except:
            print("Ungültiger Bereich!")

    
def PLOTT_EINZELZAHL(folge):
    """
    Plottet die Collatz-Folge für eine einzelne Zahl mit Markierungen:
    - Startwert (grün)
    - Höchster Wert (blau)
    - Stoppzeit (rot)
    """
    startwert = folge[0]
    max_wert = max(folge)
    max_index = folge.index(max_wert)
    endwert = folge[-1]

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(folge)), folge, color="#ff6f61", linewidth=2, label=f"Startwert {startwert}")

    # Punkte markieren
    plt.scatter(0, startwert, color="limegreen", s=80, zorder=5)
    plt.text(0, startwert + 1, "Startwert", color="limegreen", fontsize=9, ha="center")

    plt.scatter(max_index, max_wert, color="deepskyblue", s=80, zorder=5)
    plt.text(max_index, max_wert + 1, "Höchster Wert", color="deepskyblue", fontsize=9, ha="center")

    plt.scatter(len(folge) - 1, endwert, color="red", s=80, zorder=5)
    plt.text(len(folge) - 1, endwert + 1, "Stoppzeit", color="red", fontsize=9, ha="center")

    # Plot-Layout
    plt.title(f"Collatz-Folge für {startwert}")
    plt.xlabel("Schritt")
    plt.ylabel("Wert")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def PLOTT_LISTE(folgen_dict):
    """
    Plottet mehrere Collatz-Folgen (Dictionary mit {zahl: folge})
    Jede Zahl bekommt:
    - Eigene Linie
    - Markierungen für Startwert, Höchstwert und Ende
    """
    plt.figure(figsize=(10, 6))

    for startwert, folge in folgen_dict.items():
        max_wert = max(folge)
        max_index = folge.index(max_wert)
        endwert = folge[-1]

        # Hauptlinie
        plt.plot(range(len(folge)), folge, linewidth=2, label=f"{startwert}")

        # Punkte markieren
        plt.scatter(0, startwert, color="limegreen", s=50, zorder=5)
        plt.scatter(max_index, max_wert, color="deepskyblue", s=50, zorder=5)
        plt.scatter(len(folge) - 1, endwert, color="red", s=50, zorder=5)

    plt.title("Collatz-Folgen mehrerer Startwerte")
    plt.xlabel("Schritt")
    plt.ylabel("Wert")
    plt.legend(title="Startwerte", loc="upper right")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()



def PLOTT_BEREICH(folgen_dict):
    """
    Plottet die Collatz-Folgen eines Bereichs (Dictionary mit {zahl: folge}).
    Jede Zahl im Bereich bekommt eine eigene Linie.
    Markiert:
    - Startwert (grün)
    - Höchster Wert (blau)
    - Stoppzeit (rot)
    """
    plt.figure(figsize=(10, 6))

    for startwert, folge in folgen_dict.items():
        max_wert = max(folge)
        max_index = folge.index(max_wert)
        endwert = folge[-1]

        # Linie zeichnen
        plt.plot(range(len(folge)), folge, linewidth=1.5, label=f"{startwert}")

        # Punkte markieren
        plt.scatter(0, startwert, color="limegreen", s=40, zorder=5)
        plt.scatter(max_index, max_wert, color="deepskyblue", s=40, zorder=5)
        plt.scatter(len(folge) - 1, endwert, color="red", s=40, zorder=5)

    plt.title("Collatz-Folgen eines Zahlenbereichs")
    plt.xlabel("Schritt")
    plt.ylabel("Wert")
    plt.legend(title="Startwerte", loc="upper right", fontsize=8)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()




# Fenster erstellen
window = Tk()
window.title("Collatz-Folgen Tool")   # Titel des Fensters
window.geometry("1000x700")             # Fenstergröße (Breite x Höhe)
window.configure(bg="#1e1e2f")         # Schicker dunkler Hintergrund (modernes Dunkelblau/Violett)
window.resizable(False, False)         # Größe fixieren, kein Vergrößern/Verkleinern

#Willkommenstext
label = Label(window, text="Willkommen zu meinem Collatz-Folgen Tool!",
              font=("Helvetica", 16, "bold"),
              fg="#f0f0f0",     # Schriftfarbe hell
              bg="#1e1e2f")     # Hintergrundfarbe gleich wie Fenster
label.pack(pady=50)                    # Abstand nach oben/unten


for each_label in range(len(operation_labels)):
    Label(window, text=operation_labels[each_label],
              font=("Helvetica", 16, "bold"),
              fg="#f0f0f0",     # Schriftfarbe hell
              bg="#1e1e2f").place(x=x_positions_operation_labels[each_label],y=100)    
    
    entry = Entry(window, width=20, font=("Helvetica",12))
    entry.place(x=x_positions_operation_labels[each_label],y=170)
    entry_list.append(entry)

    button = Button(window, text="Berechnen!", 
                font=("Helvetica", 12, "bold"), 
                fg="#ffffff",           # Schriftfarbe weiß
                bg="#ff6f61",           # Knalliges Orange-Rot
                activebackground="#ff9a85",
                activeforeground="#ffffff",
                padx=20, 
                command=lambda i=each_label: get_nums(i),
                pady=10).place(x=x_positions_operation_labels[each_label]+30,y=200)
    berechne_btn_list.append(button)

# Fenster anzeigen
window.mainloop()
