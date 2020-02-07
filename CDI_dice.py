# import all functions from the tkinter
from tkinter import *



# import messagebox class from tkinter
from tkinter import messagebox


# Function for clearing the
# contents of all text entry boxes
def clearAll() :
    # deleting the content from the entry box
    pv_field.delete(0, END)
    atq_field.delete(0, END)
    defe_field.delete(0, END)
    shield_field.delete(0, END)
    d_endu_field.delete(0, END)
    val_endu_field.delete(0,END)
    bonus_field.delete(0, END)
    #res_d_field.delete(0, END)
    #res_cuirasse_field.delete(0, END)
    #res_encaissement_field.delete(0, END)


# function for checking error
def checkError() :
    # if any of the entry field is empty
    # then show an error message and clear
    # all the entries
    if (pv_field.get() == "" or atq_field.get() == ""
            or defe_field.get() == "" or shield_field.get() == ""
            or d_endu_field.get() == "" or bonus_field.get() == ""
            or val_endu_field.get() == ""
            or int(atq_field.get())>10 or int(defe_field.get())>10 or int(d_endu_field.get())>10 or int(val_endu_field.get())>10)\
            or int(pv_field.get())<=int(shield_field.get())\
            or int(bonus_field.get())>100\
            or int(pv_field.get()==0):
        # show the error message
        messagebox.showerror("Erreur","Il y a un problème dans les valeurs rentrées !")

        # clearAll function calling
        return -1
    return 1

def calculate_degat():
    value=checkError()
    if value== -1:
        return
    else:
        cuirasse=0
        encaissement=0
        pv=int(pv_field.get())
        atq=int(atq_field.get())
        defe=int(defe_field.get())
        endu_de=int(d_endu_field.get())
        endu_val=int(val_endu_field.get())
        shield=int(shield_field.get())/100
        bonus=int(bonus_field.get())/100

        #Calcul des dégâts
        if (atq==0): #UltraCC de PJ
            #Un ultra CC outrepasse TOUTES les défense de l'adversaire, cuirasse et défense compris.
            d=0.5+bonus
            encaissement = abs(int(d * pv))
        elif (defe==0):
            d=0+bonus

        elif (atq==1): #CC de Mob/Pj normaux
            #Ici, on outrepasse la défense de l'adversaire, mais on garde tout de même la cuirasse.
            d=0.5+bonus
            d=abs(int(d * pv))
            cuirasse = abs(int(d * (1 - shield)))  # Calcul des dégâts avec prise en compte de la cuirasse

            # Verif réussite endurance
            if (endu_de > endu_val) :
                encaissement = cuirasse
            elif (endu_val == 0) :
                encaissement = cuirasse
            else :
                encaissement = cuirasse * (1 - (10 * (abs(endu_val - endu_de) + 1)) / 100)
                encaissement = int(encaissement)

        else:
            d= abs(atq - defe)
            if (d==0):
                de=0+bonus
            elif (d==1):
                de=0.05+bonus
            elif (d==2):
                de=0.1+bonus
            elif (d==4 or d==3):
                de=0.2+bonus
            elif (d==5 or d==6):
                de=0.3+bonus
            elif (d==7 or d==8):
                de=0.4+bonus
            elif (d>=9):
                de=0.5+bonus
            d=abs(int(de*pv))
            cuirasse=abs(int(d*(1-shield))) #Calcul des dégâts avec prise en compte de la cuirasse

            #Verif réussite endurance
            if (endu_de > endu_val):
                encaissement=cuirasse
            elif (endu_val==0):
                encaissement=cuirasse
            else:
                encaissement = cuirasse * (1 - (10 * (abs(endu_val - endu_de) + 1)) / 100)
        if (encaissement >= pv):
            encaissement="Overkill"
        else:
            encaissement=int(encaissement)

        #insert methode : value in the text entry box
        res_d_field.set(str(d))
        res_cuirasse_field.set(str(cuirasse))
        res_encaissement_field.set(str(encaissement))

#driver code
if __name__ == "__main__" :
    # Create a GUI window
    gui = Tk()
    # set the name of tkinter GUI window
    gui.title("Helper")

    # Set the configuration of GUI window
    gui.geometry("290x150")
    gui.resizable(0, 0)
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)

    #StringVar
    res_d_field=StringVar()
    res_cuirasse_field=StringVar()
    res_encaissement_field=StringVar()

    #STATISTIQUES
    pv = Label(gui, text="PV")
    val_endu = Label(gui, text="Endurance")
    bonus = Label(gui, text="Bonus")
    shield = Label(gui, text="Cuirasse")

    # DICES
    atq= Label(gui, text="ATQ")
    defe= Label(gui, text="DEF")
    d_endu= Label(gui, text="END")

    #RESULTATS
    degat=Label(gui, textvariable= res_d_field, fg="grey")
    degat_label=Label(gui, text="Dégât sans défense : ", fg="grey")
    res_cuirasse=Label(gui, textvariable=res_cuirasse_field, fg="grey")
    res_cuirasse_label=Label(gui, text="Dégât avec cuirasse : ", fg= "grey")
    res_encaissement=Label(gui, textvariable=res_encaissement_field, fg="grey")
    res_encaissement_label=Label(gui, text="Dégât finaux : ", fg="grey")


    #TITRE
    stats=Label(gui, text="CARACTÉRISTIQUES",fg="maroon")
    dice=Label(gui, text="DÉS", fg="maroon")
    res=Label(gui, text="RÉSULTATS", fg="maroon")
    vide=Label(gui, text="")
    ligne=Label(gui, text="", relief="groove",bd=1, width=1)


    #Boutton résultat
    resultat=Button(gui, text="Dégâts finaux : ",bg ="bisque", fg="maroon", command=calculate_degat)

    #Clear
    #clearEntry=Button(gui,text="Effacer tout",bg ="bisque", fg="maroon", command=clearAll)

    #Remplissage
    pv_field=Spinbox(gui, from_=2, to=1000000, bg ="bisque", fg="maroon", width="7")
    atq_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")
    val_endu_field = Spinbox(gui, from_=0, to=10, width=5, bg="bisque", fg="maroon")
    defe_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")
    shield_field=Spinbox(gui, from_=0, to=999999, bg ="bisque", fg="maroon", width="7")
    d_endu_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")

    bonus_field=Spinbox(gui, from_=0, to=99, bg ="bisque", fg="maroon", width="7")

    #res_d_field=Entry(gui)
    #res_cuirasse_field=Entry(gui)
    #res_encaissement_field=Entry(gui)


    #Menu
    #ETAT

    stats.grid(row=0, column=1,sticky="nsew")

    pv.grid(row=1, column=0,sticky="nsew")
    pv_field.grid(row=1, column=1,sticky="nsew")

    val_endu.grid(row=2, column=0,sticky="nsew")
    val_endu_field.grid(row=2, column=1,sticky="nsew")

    shield.grid(row=3, column=0,sticky="nsew")
    shield_field.grid(row=3, column=1,sticky="nsew")

    bonus.grid(row=4, column=0,sticky="nsew")
    bonus_field.grid(row=4, column=1,sticky="nsew")

    #DICES
    ligne.grid(row=0, column=2, sticky="nsew", rowspan=6, ipadx=0, ipady=0)
    dice.grid(row=0, column=3,sticky="nsew")
    #dice.grid_bbox(0, 0, 1, 1)

    atq.grid(row=1, column=2,sticky="nsew")
    atq_field.grid(row=1, column=3,sticky="nsew")

    d_endu.grid(row=3, column=2,sticky="nsew")
    d_endu_field.grid(row=3, column=3,sticky="nsew")

    defe.grid(row=2, column=2,sticky="nsew")
    defe_field.grid(row=2, column=3,sticky="nsew")

    #RESULTAT
    vide.grid(row=5, column=0,sticky="nsew")
    resultat.grid(row=6, column=0,pady=1, padx=1)

    #degat_label.grid(row=6, column=0)
    #degat.grid(row=6, column=1)
    #res_d_field.grid(row=6, column=1)

    #res_cuirasse_label.grid(row=7, column=0)
    #res_cuirasse.grid(row=7, column=1)
    #res_cuirasse_field.grid(row=7, column=1)

    #res_encaissement_label.grid(row=6, column=0)
    res_encaissement.grid(row=6, column=1)
    #res_encaissement_field.grid(row=8, column=1)
    #clearEntry.grid(row=8, column=1,sticky="nsew")

    #start
    gui.mainloop()












