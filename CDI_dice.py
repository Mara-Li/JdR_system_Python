# import all functions from the tkinter
import os
import sys
import tkinter.font as tkfont
from tkinter import *
# import messagebox class from tkinter
from tkinter import messagebox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr( sys, '_MEIPASS', os.path.dirname( os.path.abspath( __file__ ) ) )
    return os.path.join( base_path, relative_path )


def test_none(t):
    if not t or len(t.strip())==0:
        return True
    return False

def clearAll ( ) :
    # deleting the content from the entry box
    atq_field.delete ( 0, END )
    pv_field.delete ( 0, END )
    pv_restant_field.delete ( 0, END )
    defe_field.delete ( 0, END )
    shield_field.delete ( 0, END )
    sel_def.set ( 1 )
    sel.set ( 1 )
    type_check ( )
    val_endu_field.delete ( 0, END )
    bonus_field.delete ( 0, END )
    atq_field.insert ( 0, 0 )
    defe_field.insert ( 0, 0 )
    shield_field.insert ( 0, 0 )
    pv_field.insert ( 0, 100 )
    pv_restant.set ( pv_string.get ( ) )
    val_endu_field.insert ( 0, 0 )
    bonus_field.insert ( 0, 0 )
    res_finaux_field.set ( '' )
    res_pv.set ( '' )
# function for checking error

def checkError() :
    """If any of the entry field is empty, show a error message. This function check also the condition."""
    if pv_field.get().isalpha( ) \
            or atq_field.get( ).isalpha( ) \
            or shield_field.get( ).isalpha( ) \
            or bonus_field.get( ).isalpha( ) \
            or val_endu_field.get( ).isalpha( ) \
            or pv_restant_field.get( ).isalpha( )\
            or defe_field.get().isalpha():
        messagebox.showerror ( "Erreur", "Les variables ne sont pas numériques")
        clearAll ( )
        return -1
    elif test_none(pv_field.get())\
            or test_none(atq_field.get( ))\
            or test_none(shield_field.get( ))\
            or test_none(bonus_field.get( ))\
            or test_none(val_endu_field.get( ))\
            or test_none(pv_restant_field.get( ))\
            or test_none(defe_field.get()):
        messagebox.showerror ( "Erreur", "Les variables sont vides" )
        clearAll ( )
        return -1
    elif int(atq_field.get()) > 10:
        x='L\'attaque est supérieure à 10'
        messagebox.showerror ( "Erreur", x )
        clearAll ( )
        return -1
    elif int(defe_field.get()) > 10 :
        x='La défense est supérieure à 10'
        messagebox.showerror ( "Erreur", x )
        clearAll ( )
        return -1
    elif int(val_endu_field.get()) > 10 :
        x='L\'endurance est supérieure à 10'
        messagebox.showerror ( "Erreur", x )
        clearAll ( )
        return -1
    elif int(pv_field.get()) <= int(shield_field.get()) :
        x='Le bouclier est supérieur au PV'
        messagebox.showerror ( "Erreur", x )
        clearAll ( )
        return -1
    elif int(bonus_field.get()) > 100:
        x='Le bouclier est supérieur à 100'
        messagebox.showerror ( "Erreur", x )
        clearAll ( )
        return -1
    elif int(pv_field.get() == 0):
        x='Les pv sont égaux à 0'
        messagebox.showerror ( "Erreur", x )
        clearAll ( )
        return -1
    elif int(pv_restant_field.get()) > int(pv_field.get()):
        x='Les pv restant sont supérieurs aux pv max'
        # show the error message
        messagebox.showerror("Erreur", x)
        clearAll()
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

def vie_restante(finaux):
    vie = int( pv_restant_field.get( ) )
    vie=vie-finaux
    if vie <= 0:
        vie='0'
    pv_restant_field.delete(0, END)
    pv_restant_field.insert( 0, vie )
    res_pv.set(vie)


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
    bonus = int ( bonus_field.get ( ) )
    PV = int( pv_field.get( ) )
    ATQ = int( atq_field.get( ) )
    DEFE = int( defe_field.get( ) )

    if sel_def.get()==1:
        endu_de=DEFE
    else:
        endu_val = 0
        endu_de = 10
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
        bonus = int( bonus_field.get( ) )
        bonus = capacite_bonus( bonus ) / 100
        endu_val = int( val_endu_field.get( ) )
        d = degat_type_normaux( bonus, ATQ, DEFE )
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
    vie_restante(finaux)

def degat_normaux():
    bonus = int( bonus_field.get( ) )
    PV = int( pv_field.get( ) )
    ATQ = int( atq_field.get( ) )
    DEFE = int( defe_field.get( ) )
    bonus = bonus / 100
    endu_val = int( val_endu_field.get( ) )
    SHIELD = int( shield_field.get( ) ) / 100
    d = calculate_degat( bonus, ATQ, DEFE )
    if sel_def.get() == 1 :
        endu_de = DEFE
    else :
        endu_val = 0
        endu_de=10
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
    vie_restante(finaux)



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
    gui.geometry("460x300")
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)

    reset_img=PhotoImage(file=resource_path('data\\reset.png'))
    reset_img=reset_img.subsample(4,4)
    logo=resource_path('data\\logo.ico')
    gui.iconbitmap(logo)

    # StringVar
    res_finaux_field = StringVar()
    res_pv=StringVar()
    pv_string = IntVar( value=100 )
    pv_restant=IntVar(value=100)
    shield_string=IntVar(value=0)
    val_endu_string=IntVar(value=0)
    bonus_string=IntVar(value=0)
    atq_string=IntVar(value=0)
    defe_string=IntVar(value=0)
    sel_def=IntVar(value=1)

    # Frames
    cadre_defenseur = Frame(gui)
    cadre_dice = Frame(gui)
    cadre_attaquant = Frame( gui)
    cadre_defenseur.config(bd=1, relief="groove")
    cadre_defenseur.grid(row=0, column=0, rowspan=3, columnspan=5, sticky='nwes')
    cadre_dice.config(bd=1, relief="groove")
    cadre_dice.grid(row=0, column=3, rowspan=3, columnspan=5, sticky='nsew', ipadx=3)
    cadre_attaquant.config(bd=1, relief="groove")
    cadre_attaquant.grid(row=1, column=0,  rowspan=2, columnspan=1, sticky='nsew',ipadx=1000)

    # FONT
    helvetica = tkfont.Font(family='Pangolin', size=16)
    titre=tkfont.Font(family='Concert One',size=15)
    pangolin=tkfont.Font(family='Pangolin', size=13)

#LABEL :

    # STATISTIQUES
    pv = Label(cadre_defenseur, text="PV (max)")
    shield = Label(cadre_defenseur, text="Bouclier")
    val_endu = Label(cadre_defenseur, text="Endurance")
    vie=Label(cadre_defenseur, text="PV (restant)")
    bonus = Label(cadre_attaquant, text="Bonus")

    # DICES
    atq = Label(cadre_dice, text="      ATQ")
    defe = Label(cadre_dice, text="      DEF")

    #RESULTAT
    res_finaux = Label(gui, textvariable=res_finaux_field, fg="#16356d", font=helvetica, anchor="e")
    pv_finaux=Label(gui, textvariable=res_pv, font=pangolin, fg='grey', anchor="w")

    # TITRE
    stats = Label(cadre_defenseur, text="DEFENSEUR", fg="#2e57a0", font=titre)
    dice = Label(cadre_dice, text="DÉS", fg="#2e57a0", font=titre)
    attaquant = Label(cadre_attaquant, text="ATTAQUANT", fg="#2e57a0", font=titre)

    # Boutton
    resultat = Button(gui, text="Dégâts finaux :", bg="#a8c9ca", fg="#253a61", command=calculate, relief=GROOVE,
                      takefocus=1, overrelief=GROOVE
                      , width=3)
    # SPINBOX
        #DEFENSEUR

    pv_field = Spinbox(cadre_defenseur, from_=2, to=1000000, textvariable=pv_string, bg="#a8c9ca", fg="#566c6c", width="7")
    pv_restant_field = Spinbox( cadre_defenseur, from_=2, to=1000000, textvariable=pv_restant, bg="#a8c9ca",
                                fg="#566c6c", width="7" )
    shield_field = Spinbox( cadre_defenseur, from_=0, to=999999, bg="#a8c9ca", fg="#566c6c", width="7",
                            textvariable=shield_string )
    val_endu_field = Spinbox( cadre_defenseur, from_=0, to=10, width=5, bg="#a8c9ca", fg="#566c6c",
                              textvariable=val_endu_string )

        #ATTAQUANT
    bonus_field = Spinbox( cadre_attaquant, from_=0, to=99, bg="#a8c9ca", fg="#566c6c", width="10",
                           textvariable=bonus_string )
        #DICE
    atq_field = Spinbox(cadre_dice, from_=0, to=10, width=5, bg="#a8c9ca", fg="#566c6c", textvariable=atq_string)
    defe_field = Spinbox(cadre_dice, from_=0, to=10, width=5, bg="#a8c9ca", fg="#566c6c",textvariable=defe_string)

    endurance=Radiobutton(cadre_dice, text="Endurance", variable=sel_def, value=1)
    esquive=Radiobutton(cadre_dice, text="Esquive raté", variable=sel_def, value=2)



        #Button Attaque
    capacite=['Perforante', 'Autre','Burst']
    capacite=capacite[::-1]
    var_type=StringVar()
    type_capa = Spinbox(cadre_attaquant, values=capacite,wrap=True, command=lambda: print(var_type.get()),width="10")
    type_capa.grid(row=4, column=0, columnspan=2,padx=130, sticky='ew')
    type_capa.configure(state='disabled')

    # IntVar
    sel = IntVar(value=1)

    def type_check():
        if sel.get() == 2:
            type_capa.configure(state='readonly',readonlybackground='#a8c9ca', fg='#566c6c')
        else:
            type_capa.configure(state='disable')

    normal = Radiobutton(cadre_attaquant, text="Attaque normale", variable=sel, value=1, command=type_check).grid(row=3, column=0, sticky='nw', columnspan=2,padx=40)
    capacite = Radiobutton(cadre_attaquant, text="Capacité", variable=sel, value=2, command=type_check).grid(row=4, column=0, sticky='nw', padx=40)
    reset_bouton = Button(cadre_dice, text="Reset", image=reset_img, bg="#b1b3b3", command=clearAll, relief=GROOVE,
                          takefocus=1, overrelief=GROOVE)


    # AFFICHAGE / GRID :

    # DEFENSEUR

    stats.grid(row=0, column=0, sticky="nsew", columnspan=3, padx=100)
    pv.grid(row=1, column=0, sticky="nsew")
    pv_field.grid(row=1, column=1, sticky="nsew")
    vie.grid(row=2, column=0, sticky="nsew")
    pv_restant_field.grid(row=2, column=1, sticky="nsew")
    shield.grid(row=3, column=0, sticky="nsew")
    shield_field.grid(row=3, column=1, sticky="nsew")
    val_endu.grid(row=4, column=0, sticky="nsew")
    val_endu_field.grid(row=4, column=1, sticky="nsew")

    #ATTAQUANT
    attaquant.grid(row=0, column=0, columnspan=3, padx=100)
    bonus.grid(row=1, column=0, sticky='nw', rowspan=2, padx=40)
    bonus_field.grid(row=1, column=0, padx=121, ipadx=0, sticky='ew')



    # DICES
    dice.grid(row=0, column=3, sticky="nsew")
    atq.grid(row=1, column=2, sticky="nsew")
    atq_field.grid(row=1, column=3, sticky="nsew")
    endurance.grid(row=3, column=3,sticky='nw')
    esquive.grid(row=4, column=3, sticky='nw')
    defe.grid(row=2, column=2, sticky="nsew")
    defe_field.grid(row=2, column=3, sticky="nsew")
    reset_bouton.grid(row=5, column=3,pady=40,stick='sw',padx=20)


    # RESULTAT
    resultat.grid(row=6, column=0, ipadx=100000, sticky='nsew')
    pv_finaux_titre=Label(gui, text="PV restant : ", fg='grey', anchor='e').grid(row=7, column=0, ipadx=100000, sticky='e')
    res_finaux.grid(row=6, column=5, sticky='sw')
    pv_finaux.grid(row=7, column=4, sticky='sw')

    # start
    gui.mainloop()
