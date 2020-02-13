# import all functions from the tkinter
import tkinter.font as tkfont
from tkinter import *
# import messagebox class from tkinter
from tkinter import messagebox


# function for checking error
def checkError() :
    """If any of the entry field is empty, show a error message. This function check also the condition."""
    if (pv_field.get() == "" or atq_field.get() == ""
        or defe_field.get() == "" or shield_field.get() == ""
        or d_endu_field.get() == "" or bonus_field.get() == ""
        or val_endu_field.get() == ""
        or int(atq_field.get()) > 10 or int(defe_field.get()) > 10 or int(d_endu_field.get()) > 10 or int(
                val_endu_field.get()) > 10) \
            or int(pv_field.get()) <= int(shield_field.get()) \
            or int(bonus_field.get()) > 100 \
            or int(pv_field.get() == 0) :
        # show the error message
        messagebox.showerror("Erreur", "Il y a un problème dans les valeurs entrées !")
        return -1
    return 1

def reussite_endurance(endu_de, endu_val, PV,d, SHIELD):
    d = abs(int(d * PV))
    Bouclier = abs(int(d * (1 - SHIELD)))
    if endu_de > endu_val :
        finaux = Bouclier
    elif endu_val == 0 :
        finaux = Bouclier
    else :
        finaux = Bouclier * (1 - (10 * (abs(endu_val - endu_de) + 1)) / 100)

    if finaux >= PV :
        finaux = "Overkill  "
    else :
        finaux = int(finaux)
    return finaux


def capacite_bonus(bonus):
    atq = int(atq_field.get())
    if atq == 0:
        bonus=bonus*2
    elif atq == 1:
        bonus=bonus*1.5
    return bonus

def calculate_degat(bonus, ATQ, DEFE):
    d = abs(ATQ - DEFE)
    if d == 0 :
        d = 0 + bonus
    elif d == 1 :
        d = 0.05 + bonus
    elif d == 2 :
        d = 0.1 + bonus
    elif d == 4 or d == 3 :
        d = 0.2 + bonus
    elif d == 5 or d == 6 :
        d = 0.3 + bonus
    elif d == 7 or d == 8 :
        d = 0.4 + bonus
    elif d >= 9 :
        d = 0.5 + bonus
    return d

def degat_burst(bonus, ATQ, DEFE):
    if ATQ == 0 :  # UltraCC de PJ
        d = 0.15+bonus
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0  # Permet de sortir de la boucle !
    elif ATQ == 1:
        d=0.1+bonus
    else:
        d = calculate_degat( bonus, ATQ, DEFE)
    return d

def degat_type_normaux(bonus, ATQ, DEFE):
    if ATQ == 0 :  # UltraCC de PJ
        d = 0.2+bonus
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0  # Permet de sortir de la boucle !
    elif ATQ == 1:
        d=0.15+bonus
    else:
        d = calculate_degat( bonus, ATQ, DEFE)
    return d

def degat_types():
    bonus = int( bonus_field.get( ) )
    PV = int( pv_field.get( ) )
    ATQ = int( atq_field.get( ) )
    DEFE = int( defe_field.get( ) )
    endu_de = int( d_endu_field.get( ) )
    SHIELD = int( shield_field.get( ) ) / 100
    if type_capa.get( ) == 'Burst' :
        if SHIELD != 0:
            bonus = bonus + 20
        else:
            bonus= bonus+30
        bonus = capacite_bonus( bonus )/ 100
        endu_val = int( val_endu_field.get( ) )
        d = degat_burst( bonus, ATQ, DEFE )
        SHIELD = int( shield_field.get( ) ) / 100
    elif type_capa.get()=='Autre' :
        bonus = capacite_bonus( bonus ) / 100
        endu_val = int( val_endu_field.get( ) )
        d = degat_burst( bonus, ATQ, DEFE )
        SHIELD = int( shield_field.get( ) ) / 100
    elif type_capa.get( ) == 'Perforante' :
        bonus = bonus + 15
        bonus = capacite_bonus( bonus ) / 100
        endu_val = 0
        SHIELD = 0
        d = degat_type_normaux( bonus, ATQ, DEFE)
    finaux = reussite_endurance( endu_de, endu_val, PV, d, SHIELD )

    # insert methode : value in the text entry box
    res_finaux_field.set( str( finaux ) )

def degat_normaux():
    bonus = int( bonus_field.get( ) )
    PV = int( pv_field.get( ) )
    ATQ = int( atq_field.get( ) )
    DEFE = int( defe_field.get( ) )
    endu_de = int( d_endu_field.get( ) )
    bonus = bonus / 100
    endu_val = int( val_endu_field.get( ) )
    SHIELD = int( shield_field.get( ) ) / 100
    d = calculate_degat( bonus, ATQ, DEFE )
    # Calcul des dégâts
    if ATQ == 0 :  # UltraCC de PJ
        # Un ultra CC outrepasse TOUTES les défense de l'adversaire, Bouclier et défense compris.
        d = 0.5 + bonus
        endu_val = 0
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0  # Permet de sortir de la boucle !
    elif ATQ == 1 :  # CC de Mob/Pj normaux
        endu_val = 0
    finaux = reussite_endurance( endu_de, endu_val, PV, d, SHIELD )

    # insert methode : value in the text entry box
    res_finaux_field.set( str( finaux ) )



def calculate() :
    value = checkError()
    if value == -1 :
        return
    else :
        selection = int( sel.get( ) )
        if selection == 2:
            degat_types()
        elif selection == 1:
            degat_normaux()

# driver code
if __name__ == "__main__" :
    # Create a GUI window
    gui = Tk()
    # set the name of tkinter GUI window
    gui.title("Helper")

    # Set the configuration of GUI window
    gui.geometry("380x200")
    #gui.resizable(0, 0)
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)

    # StringVar
    res_finaux_field = StringVar()

    # Frames
    cadre_statistique = Frame(gui)
    cadre_dice = Frame(gui)
    cadre_statistique.config(bd=1, relief="groove")
    cadre_statistique.grid(row=0, column=0, rowspan=3, columnspan=5, sticky='nwes')
    cadre_dice.config(bd=1, relief="groove")
    cadre_dice.grid(row=0, column=3, rowspan=3, columnspan=6, sticky='nsew', ipadx=3)


    # STATISTIQUES
    pv = Label(cadre_statistique, text="PV")
    shield = Label(cadre_statistique, text="Bouclier")
    val_endu = Label(cadre_statistique, text="Endurance")
    bonus = Label(cadre_statistique, text="Bonus")

    # DICES
    atq = Label(cadre_dice, text="      ATQ")
    defe = Label(cadre_dice, text="      DEF")
    d_endu = Label(cadre_dice, text="      END")

    # RESULTATS
    helvetica = tkfont.Font(family='Helvetica', size=14)
    res_finaux = Label(gui, textvariable=res_finaux_field, fg="maroon", font=helvetica)

    # TITRE
    stats = Label(cadre_statistique, text="CARACTÉRISTIQUES", fg="maroon")
    dice = Label(cadre_dice, text="DÉS", fg="maroon")

    # Boutton résultat
    resultat = Button(gui, text="Dégâts finaux :  ", bg="bisque", fg="maroon", command=calculate, relief=GROOVE,
                      takefocus=1, overrelief=GROOVE
                      , width=3)
    # Remplissage
    pv_string=IntVar(value=100)
    pv_field = Spinbox(cadre_statistique, from_=2, to=1000000, textvariable=pv_string, bg="bisque", fg="maroon", width="7")
    atq_field = Spinbox(cadre_dice, from_=0, to=10, width=5, bg="bisque", fg="maroon")
    defe_field = Spinbox(cadre_dice, from_=0, to=10, width=5, bg="bisque", fg="maroon")
    shield_field = Spinbox(cadre_statistique, from_=0, to=999999, bg="bisque", fg="maroon", width="7")
    val_endu_field = Spinbox(cadre_statistique, from_=0, to=10, width=5, bg="bisque", fg="maroon")
    d_endu_field = Spinbox(cadre_dice, from_=0, to=10, width=5, bg="bisque", fg="maroon")
    bonus_field = Spinbox(cadre_statistique, from_=0, to=99, bg="bisque", fg="maroon", width="7")


        #Button Attaque
    capacite=['Perforante', 'Autre','Burst']
    capacite=capacite[::-1]
    var_type=StringVar()
    type_capa = Spinbox(cadre_statistique, values=capacite,wrap=True, command=lambda: print(var_type.get()),width="10")
    type_capa.grid(row=6, column=1, sticky='n')
    type_capa.configure(state='disabled')

    # IntVar
    sel = IntVar(value=1)

    def type_check():
        if sel.get() == 2:
            type_capa.configure(state='readonly',readonlybackground='bisque', fg='maroon')
        else:
            type_capa.configure(state='disable')

    normal = Radiobutton(cadre_statistique, text="Attaque normale", variable=sel, value=1, command=type_check).grid(row=5, column=0, sticky='w', columnspan=2,padx=50)
    capacite = Radiobutton(cadre_statistique, text="Capacité", variable=sel, value=2, command=type_check).grid(row=6, column=0, sticky='w', columnspan=2, padx=50)

    # Menu
    # ETAT

    stats.grid(row=0, column=0, sticky="nsew", columnspan=3, padx=100)
    pv.grid(row=1, column=0, sticky="nsew")
    pv_field.grid(row=1, column=1, sticky="nsew")
    shield.grid(row=2, column=0, sticky="nsew")
    shield_field.grid(row=2, column=1, sticky="nsew")
    val_endu.grid(row=3, column=0, sticky="nsew")
    val_endu_field.grid(row=3, column=1, sticky="nsew")
    bonus.grid(row=4, column=0, sticky="nsew")
    bonus_field.grid(row=4, column=1, sticky="nsew")

    # DICES
    dice.grid(row=0, column=3, sticky="nsew")
    atq.grid(row=1, column=2, sticky="nsew")
    atq_field.grid(row=1, column=3, sticky="nsew")
    d_endu.grid(row=3, column=2, sticky="nsew")
    d_endu_field.grid(row=3, column=3, sticky="nsew")
    defe.grid(row=2, column=2, sticky="nsew")
    defe_field.grid(row=2, column=3, sticky="nsew")

    # RESULTAT
    resultat.grid(row=6, column=0, ipadx=100000, sticky='ns')
    res_finaux.grid(row=6, column=5, columnspan=100, sticky='s')

    # start
    gui.mainloop()
