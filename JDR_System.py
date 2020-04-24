# import all functions from the tkinter
import os
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
    #pv_field.delete ( 0, END )
    pv_restant_field.delete ( 0, END )
    defe_field.delete ( 0, END )
    shield_field.delete ( 0, END )
    sel_def.set ( 1 )
    sel.set ( 1 )
    sel_attaquant.set(1)
    type_check ( )
    val_endu_field.delete ( 0, END )
    bonus_entry.delete ( 0, END )
    bonus_field.delete(0, END)
    atq_field.insert ( 0, 0 )
    var_bonus.set('Aucun')
    annulation ( )
    var_bonus_entry.set(value=0)
    defe_field.insert ( 0, 0 )
    shield_field.insert ( 0, 0 )
    #pv_field.insert ( 0, 100 )
    pv_restant.set ( pv_string.get ( ) )
    val_endu_field.insert ( 0, 0 )
    bonus_entry.insert ( 0, 0 )
    res_finaux_field.set ( '' )
    res_pv.set ( '' )
    var_type.set('Burst')
    remise.deselect()

def clear_log():
    log_file=open('dice.log','w')
    log_file.write('')
    log_file.close()

# function for checking error

def checkError() :
    """If any of the entry field is empty, show a error message. This function check also the condition."""
    if pv_field.get().isalpha( ) \
            or atq_field.get( ).isalpha( ) \
            or shield_field.get( ).isalpha( ) \
            or val_endu_field.get( ).isalpha( ) \
            or pv_restant_field.get( ).isalpha( )\
            or bonus_entry.get().isalpha()\
            or defe_field.get().isalpha():
        messagebox.showerror ( "Erreur", "Les variables ne sont pas numériques")
        clearAll ( )
        return -1
    elif test_none(pv_field.get())\
            or test_none(atq_field.get( ))\
            or test_none(shield_field.get( ))\
            or test_none(bonus_field.get( ))\
            or test_none(bonus_entry.get())\
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
    elif int(bonus_entry.get())>100:
        x='Le bonus est supérieur à 100%'
        messagebox.showerror("Erreur", x)
        clearAll()
        return -1
    elif int(shield_field.get()) > 100:
        x='Le bouclier est supérieur à 100.'
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

def choix_bonus():
    bonus=bonus_field.get ( )
    bonus_val=int(bonus_entry.get())
    dist=sel_rang.get()
    if bonus=='Pouvoir':
        b=10+bonus_val
    elif bonus=='Fusil':
        b=10+bonus_val
        if dist==1:
            b=b+5
    elif bonus=='Projectile':
        b=5+bonus_val
    elif bonus=='Epée':
        b=10+bonus_val
    elif bonus=='Contondant':
        b=15+bonus_val
    elif bonus=='Couteau':
        b=5+bonus_val
    elif bonus=='Pistolet':
        b=8+bonus_val
    elif bonus=='Artillerie':
        b=15+bonus_val
        if dist==1:
            b=b+10
    elif bonus=='Autre':
        b=bonus_val
    elif bonus=='Aucun':
        b=0
    b=int(b)
    return b

def reussite_endurance(endu_de, endu_val, PV,d, SHIELD):
    d = abs(int(d * PV))
    Bouclier = abs(int(d * (1 - SHIELD)))
    if remise_var.get()==1:
        if endu_de > endu_val or endu_de==endu_val:
            finaux = Bouclier
        elif endu_val == 0 :
            finaux = Bouclier
        else :
            finaux = Bouclier * (1 - (10 * (abs(endu_val - endu_de) + 1)) / 100)
    else:
        if endu_de > endu_val :
            finaux = Bouclier
        elif endu_val == 0 :
            finaux = Bouclier
        else :
            finaux = Bouclier * (1 - (10 * (abs ( endu_val - endu_de ) + 1)) / 100)

    if finaux >= PV :
        finaux = PV
    else :
        finaux = int ( finaux )
    return finaux

def vie_restante(finaux):
    vie = int( pv_restant_field.get( ) )
    vie = vie - finaux
    msg_pv=vie
    if vie <= 0:
        vie='0'
        msg_pv="X"
    pv_restant_field.delete(0, END)
    pv_restant_field.insert( 0, vie )
    res_pv.set(msg_pv)

def capacite_bonus(bonus):
    atq = int(atq_field.get())
    if atq == 0:
        bonus=bonus*1.8
    elif atq == 1:
        bonus=bonus*1.4
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
def degat_burst(bonus, ATQ, DEFE, endu_val):
    if ATQ == 0 :  # UltraCC de PJ
        d = 0.25+bonus
        endu_val=0
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0  # Permet de sortir de la boucle !
    elif ATQ == 1:
        d=calculate_degat(bonus, ATQ, DEFE)
    else:
        d = calculate_degat( bonus, ATQ, DEFE)
    return d, endu_val

def degat_burst_bouclier(bonus, ATQ, DEFE, endu_val):
    if ATQ==0:
        d=0.38+bonus
        endu_val = 0
    elif DEFE==0:
        d=0
    elif ATQ==1:
        d=calculate_degat(bonus, ATQ, DEFE)
    else:
        d=calculate_degat(bonus, ATQ, DEFE)
    return d, endu_val

def degat_perforant(bonus, ATQ, DEFE,endu_val):
    if ATQ == 0 :  # UltraCC de PJ
        d = 0.40+bonus
        endu_val = 0
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0  # Permet de sortir de la boucle !
    elif ATQ == 1:
        d=calculate_degat(bonus, ATQ, DEFE)
    else:
        d = calculate_degat( bonus, ATQ, DEFE)
    return d, endu_val

def degat_autre(bonus, ATQ, DEFE, endu_val):
    if ATQ == 0 :  # UltraCC de PJ
        d = 0.5+bonus
        endu_val = 0
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0
        # Permet de sortir de la boucle !
    elif ATQ == 1:
        d=calculate_degat(bonus, ATQ, DEFE)
    else:
        d = calculate_degat( bonus, ATQ, DEFE)
    return d, endu_val

def degat_types():
    bonus = int(bonus_entry.get())
    PV = int( pv_field.get( ) )
    ATQ = int( atq_field.get( ) )
    DEFE = int( defe_field.get( ) )

    if sel_def.get()==1:
        endu_de=DEFE
    else:
        if remise_var.get() == 0:
            if DEFE <= ATQ / 2:
                DEFE = 0
                endu_de = 0
            else:
                endu_val = 0
                endu_de = 10
        else:
            if DEFE < ATQ / 2:
                DEFE = 0
                endu_de = 0
            else:
                endu_val = 0
                endu_de = 10
    SHIELD = int( shield_field.get( ) ) / 100

    if type_capa.get( ) == 'Burst' :
        endu_val = int( val_endu_field.get( ) )
        SHIELD = int ( shield_field.get ( ) ) / 100
        if SHIELD != 0:
            bonus_type = capacite_bonus ( 15 )
            bonus = (bonus_type+bonus) / 100
            d, endu_val=degat_burst_bouclier(bonus, ATQ, DEFE, endu_val)
        else:

            bonus_type = capacite_bonus ( 25 )
            bonus= (bonus+bonus_type)/ 100
            d, endu_val = degat_burst( bonus, ATQ, DEFE, endu_val )

    elif type_capa.get()=='Autre' :
        bonus_attaque = choix_bonus()
        bonus = capacite_bonus( bonus )
        bonus= (bonus_attaque+bonus)/ 100
        endu_val = int( val_endu_field.get( ) )
        d, endu_val = degat_autre( bonus, ATQ, DEFE , endu_val)
        SHIELD = int( shield_field.get( ) ) / 100

    elif type_capa.get( ) == 'Perforante' :
        bonus_type = capacite_bonus ( 15 )
        bonus = (bonus_type + bonus) / 100
        endu_val = 0
        SHIELD = 0
        d, endu_val = degat_perforant( bonus, ATQ, DEFE, endu_val)
    finaux = reussite_endurance ( endu_de, endu_val, PV, d, SHIELD )
    finaux=int(finaux/1.4)
    max = finaux
    if PV >= 1000 :
        max = 200
    elif PV > 100 and PV < 1000 :
        max = 100
    elif PV <= 100 :
        max = 80
    if finaux > max:
        finaux=max
    # insert methode : value in the text entry box
    res_finaux_field.set( str( finaux ) )
    vie_restante(finaux)

def degat_normaux():
    bonus = choix_bonus()
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
        if remise_var.get()==0:
            if DEFE <= ATQ/2 :
                DEFE=0
                endu_de=0
            else:
                endu_val=0
                endu_de=10
        else:
            if DEFE < ATQ/2 :
                DEFE=0
                endu_de=0
            else:
                endu_val=0
                endu_de=10

    # Calcul des dégâts
    if ATQ == 0 :  # UltraCC de PJ
        # Un ultra CC outrepasse TOUTES les défense de l'adversaire, Bouclier et défense compris.
        d = 0.50 + bonus
        endu_val = 0
    elif DEFE == 0 :  # CC de défense : quelque soit l'attaque, elle ne passera pas, sauf en cas de 0/0, où l'attaquant à priorité
        d = 0  # Permet de sortir de la boucle !
    elif ATQ == 1 :  # CC de Mob/Pj normaux
        endu_val = 0
    finaux = reussite_endurance( endu_de, endu_val, PV, d, SHIELD )
    finaux=int(finaux/1.4)
    max=finaux
    if PV >= 1000:
        max=200
    elif PV > 100 and PV < 1000:
        max=100
    elif PV <=100:
        max=80
    if finaux > max:
        finaux=max

    # insert methode : value in the text entry box
    res_finaux_field.set( str( finaux ) )
    vie_restante(finaux)

def log_ecriture():
    PV =  pv_field.get ( )
    pv_restant=pv_restant_field.get()
    ATQ = atq_field.get ( )
    DEFE = defe_field.get ( )
    bonus=bonus_entry.get()
    bonus_type=bonus_field.get()
    endu_val = val_endu_field.get ( )
    SHIELD = shield_field.get ( )
    log_file=open('dice.log','a')
    selection_type=int(sel.get())
    attaquant=sel_attaquant.get()
    defense=sel_def.get()
    type_cap=type_capa.get()
    resultat=res_finaux_field.get()
    if int(pv_restant)<=0:
        pv_restant='X'
    if selection_type==1:
        selection_type='Attaque normale'
    else:
        if type_cap=='Burst':
            selection_type='Burst'
        elif type_cap=='Perforante':
            selection_type='Perforante'
        else:
            selection_type='Autre'
    if attaquant==1:
        attaquant='Actif'
    else:
        attaquant='Monstre'
    if defense==1:
        defense='Endurance'
    else:
        if remise_var.get()==1:
            if int(DEFE) < int(int(ATQ)/2):
                defense='Esquive réussie'
            else:
                defense='Esquive raté'
        else:
            if int(DEFE) <= int(int(ATQ)/2):
                defense='Esquive réussie'
            else:
                defense='Esquive ratée'
    if remise_var.get()==1:
        remise="UTILISE"
    else:
        remise='NON UTILISE'

    log_file.write ( '=================\n' )
    log_file.write ( selection_type + '\n' )
    log_file.write ( "\n" )
    log_file.write ( "DEFENSEUR\n" )
    log_file.write ( "PV MAX : " + PV + '\n' )
    log_file.write ( "BOUCLIER : " + SHIELD + '\n' )
    log_file.write ( "ENDURANCE : " + endu_val + '\n' )
    log_file.write ( '\n' )
    log_file.write ( "ATTAQUANT\n" )
    log_file.write ( 'BONUS : ' + bonus_type + '\n' )
    log_file.write ( 'VALEUR DU BONUS : ' + bonus + '\n' )
    log_file.write ( 'ATTAQUANT : ' + attaquant + '\n' )
    log_file.write ( '\n' )
    log_file.write ( 'DES\n' )
    log_file.write ( 'ATQ : ' + ATQ + '\n' )
    log_file.write ( 'DEF : ' + DEFE + '\n' )
    log_file.write ('REMISE : ' + remise + '\n')
    log_file.write ( 'TYPE DE DEFENSE : ' + defense + '\n' )
    log_file.write ( '\n' )
    log_file.write ( 'RESULTAT\n' )
    log_file.write ( 'DEGATS : ' + resultat + '\n' )
    log_file.write ( "PV RESTANT : " + pv_restant + '\n' )
    log_file.write ( '\n' )

    log_file.close()

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
    log_ecriture()
# driver code
if __name__ == "__main__" :
    # Create a GUI window
    gui = Tk()
    # set the name of tkinter GUI window
    gui.title("JDR System")

    # Set the configuration of GUI window
    gui.geometry("500x330")
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)

    reset_img=PhotoImage(file=resource_path('data\\reset.png'))
    reset_log=PhotoImage(file=resource_path('data\\log_file.png'))
    reset_img=reset_img.subsample(4,4)
    reset_log=reset_log.subsample(4,4)
    # change to your folder !!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    gui.iconbitmap(r"D:\\Documents\\GitHub\\CDI_Dice_Help\\data\\logo.ico")




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
    cadre_dice.grid(row=0, column=3, rowspan=3, columnspan=3, sticky='nsew', ipadx=3)
    cadre_attaquant.config(bd=1, relief="groove")
    cadre_attaquant.grid(row=1, column=0,  rowspan=2, columnspan=1, sticky='nsew',ipadx=1000)

    # FONT
    helvetica = tkfont.Font(family='Pangolin', size=16)
    titre=tkfont.Font(family='Concert One',size=15)
    pangolin=tkfont.Font(family='Pangolin', size=13)

    #Fonction lien PV max - restant

    def setting_entry(event):
        pv_restant.set ( pv_string.get ( ) )

    def setting_arrow():
        pv_restant.set ( pv_string.get ( ) )

    #Fonction entry - start (même fonction que le bouton)
    def final_entry(e=None):
        calculate()

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
    # REMPLISSAGE
        #DEFENSEUR


    pv_field = Spinbox ( cadre_defenseur, from_=2, to=1000000, textvariable=pv_string, bg="#a8c9ca", fg="#566c6c",
                         width="7", command=setting_arrow ,wrap=True)
    pv_restant_field = Spinbox ( cadre_defenseur, from_=2, to=1000000, textvariable=pv_restant, bg="#a8c9ca",
                                 fg="#566c6c", width="7" ,wrap=True)
    shield_field = Spinbox( cadre_defenseur, from_=0, to=99, bg="#a8c9ca", fg="#566c6c", width="7",
                            textvariable=shield_string ,wrap=True)
    val_endu_field = Spinbox( cadre_defenseur, from_=0, to=10, width=5, bg="#a8c9ca", fg="#566c6c",
                              textvariable=val_endu_string ,wrap=True)

        #ATTAQUANT
    bonus_type=['Aucun', 'Autre','Artillerie','Fusil','Pistolet','Contondant','Epée','Projectile','Couteau','Pouvoir']
    var_bonus_entry=IntVar(value=0)
    bonus_entry = Spinbox ( cadre_attaquant, from_=0, to=99, width=4, wrap=True, textvariable=var_bonus_entry)
    bonus_entry.grid ( row=1, column=0, sticky='w', padx=220 )
    bonus_entry.configure(state='disabled')
    var_bonus=StringVar()
    def annulation():
        if bonus_field.get()!='Aucun':
            bonus_entry.configure(state="normal",bg='#a8c9ca', fg='#566c6c')
        else:
            bonus_entry.configure(state='disable')

    bonus_field = Spinbox ( cadre_attaquant, readonlybackground='#a8c9ca', fg='#566c6c', values=bonus_type,
                            command=annulation, textvariable=var_bonus,
                            width=13, wrap=True )
    bonus_field.configure ( state='readonly' )


    #Type d'attaquant :
    sel_attaquant=IntVar(value=1)
    #actif=Radiobutton(cadre_attaquant, text="Actif", variable=sel_attaquant, value=1)
    #monstre = Radiobutton ( cadre_attaquant, text="Monstre", variable=sel_attaquant, value=2 )

    #rang :
    sel_rang=IntVar(value=1)
    rang1=Radiobutton(cadre_attaquant, text='Corps-à-corps', variable=sel_rang, value=1)
    rang2=Radiobutton(cadre_attaquant, text='Distance', variable=sel_rang, value=2)
    #rang3=Radiobutton(cadre_attaquant, text='Distance', variable=sel_rang, value=3)

        #Button Attaque
    capacite=['Perforante', 'Autre','Burst']
    capacite=capacite[::-1]
    var_type=StringVar()
    type_capa = Spinbox(cadre_attaquant, values=capacite,wrap=True, textvariable=var_type,width="19")
    type_capa.grid(row=4, column=0,padx=126, sticky='w',ipadx=3)
    type_capa.configure(state='disabled')

    # IntVar
    sel = IntVar(value=1)
    remise_var=IntVar()

    def type_check():
        if sel.get() == 2:
            type_capa.configure(state='readonly',readonlybackground='#a8c9ca', fg='#566c6c')
        else:
            type_capa.configure(state='disable')

    normal = Radiobutton(cadre_attaquant, text="Attaque normale", variable=sel, value=1, command=type_check).grid(row=3, column=0, sticky='nw', columnspan=2,padx=40)
    capacite = Radiobutton(cadre_attaquant, text="Capacité", variable=sel, value=2, command=type_check).grid(row=4, column=0, sticky='nw', padx=40)

    # DICE
    atq_field = Spinbox ( cadre_dice, from_=0, to=10, width=5, bg="#a8c9ca", fg="#566c6c", textvariable=atq_string,
                          wrap=True )
    defe_field = Spinbox ( cadre_dice, from_=0, to=10, width=5, bg="#a8c9ca", fg="#566c6c", textvariable=defe_string,
                           wrap=True )

    endurance = Radiobutton ( cadre_dice, text="Endurance", variable=sel_def, value=1 )
    esquive = Radiobutton ( cadre_dice, text="Esquive raté", variable=sel_def, value=2 )
    reset_bouton = Button ( cadre_dice, text="Reset", image=reset_img, bg="#b1b3b3", command=clearAll, relief=GROOVE,
                            takefocus=1, overrelief=GROOVE )
    reset_log_button=Button(cadre_dice, text='Log', image=reset_log, bg="#b1b3b3", command=clear_log, relief=GROOVE, takefocus=1, overrelief=GROOVE)
    remise=Checkbutton(cadre_dice, text="Remise", variable=remise_var)


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
    attaquant.grid(row=0, column=0, columnspan=3, padx=100, sticky="w")
    bonus.grid(row=1, column=0, sticky='nw', rowspan=2, padx=40)
    bonus_field.grid ( row=1, column=0, padx=126, sticky='w' )

    #actif.grid(row=1, column=0, sticky="nw",padx=270)
    #monstre.grid(row=4, column=0, sticky="nw", padx=270)

    rang1.grid(row=5, column=0, sticky='nw', padx=80)
    rang2.grid(row=5, column=0, sticky='nw', padx=200)
    #rang3.grid(row=5, column=0, sticky='nw', padx=270)


    # DICES
    dice.grid(row=0, column=2, sticky='nw', padx=40)
    atq.grid(row=1, column=1, sticky="nsew")
    atq_field.grid(row=1, column=2, sticky="nw", ipadx=30)
    endurance.grid(row=3, column=2,sticky='nw')
    esquive.grid(row=4, column=2, sticky='nw')
    defe.grid(row=2, column=1, sticky="nsew")
    defe_field.grid(row=2, column=2, sticky="nw")
    remise.grid(row=2, column=2, sticky="nsew", padx=45)
    reset_bouton.grid(row=5, column=2,pady=40,stick='sw',padx=20)
    reset_log_button.grid(row=5, column=2, pady=40, padx=50, stick='sw')


    # RESULTAT
    resultat.grid(row=6, column=0, ipadx=100000, sticky='nsew')
    pv_finaux_titre=Label(gui, text="PV restant : ", fg='grey', anchor='e').grid(row=7, column=0, ipadx=100000, sticky='e')
    res_finaux.grid(row=6, column=5, sticky='sw')
    pv_finaux.grid(row=7, column=4, sticky='sw')

    #Binding button
    pv_field.bind ( "<Button-1>", setting_entry )
    pv_field.bind ( "<FocusOut>", setting_entry )
    gui.bind('<Return>', final_entry)

    # start
    gui.mainloop()
