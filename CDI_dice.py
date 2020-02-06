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
            or int(atq_field.get())>10 or int(defe_field.get())>10 or int(d_endu_field.get())>10 or int(val_endu_field.get())>10):
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
        pv=int(pv_field.get())
        atq=int(atq_field.get())
        defe=int(defe_field.get())
        endu_de=int(d_endu_field.get())
        endu_val=int(val_endu_field.get())
        shield=int(shield_field.get())/100
        bonus=int(bonus_field.get())/100

        #Calcul des dégâts
        d= abs(atq - defe)
        if (d==0):
            d=0+bonus
        elif (d==1):
            d=0.5+bonus
        elif (d==2):
            d=0.1+bonus
        elif (d==4 or d==3):
            d=0.2+bonus
        elif (d==5 or d==6):
            d=0.3+bonus
        elif (d==7 or d==8):
            d=0.4+bonus
        elif (d>=9):
            d=0.5+bonus

        d=abs(int(d*pv))
        cuirasse=abs(int(d*(1-shield))) #Calcul des dégâts avec prise en compte de la cuirasse

        #Verif réussite endurance
        if (endu_de > endu_val):
            encaissement=0
        else:
            encaissement = cuirasse * (1 - (10 * (abs(endu_val - endu_de) + 1)) / 100)
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
    gui.title("Aide CDI")

    # Set the configuration of GUI window
    gui.geometry("500x300")

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
    d_endu= Label(gui, text="Endurance")

    #RESULTATS
    degat=Label(gui, textvariable= res_d_field, fg="grey")
    degat_label=Label(gui, text="Dégât basique : ", fg="grey")

    res_cuirasse=Label(gui, textvariable=res_cuirasse_field, fg="grey")
    res_cuirasse_label=Label(gui, text="Dégât avec cuirasse : ", fg= "grey")

    res_encaissement=Label(gui, textvariable=res_encaissement_field, fg="grey")
    res_encaissement_label=Label(gui, text="Dégât après encaissement : ", fg="grey")


    #TITRE
    stats=Label(gui, text="CARACTERISTIQUES",fg="maroon")
    dice=Label(gui, text="DÉS", fg="maroon")
    res=Label(gui, text="RESULTATS", fg="maroon")


    #Boutton résultat
    resultat=Button(gui, text="Résultat",bg ="bisque", fg="maroon", command=calculate_degat)

    #Clear
    clearEntry=Button(gui,text="Effacer tout",bg ="bisque", fg="maroon", command=clearAll)

    #Remplissage
    pv_field=Entry(gui,bg ="bisque", fg="maroon", width="7")
    atq_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")
    defe_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")
    shield_field=Entry(gui,bg ="bisque", fg="maroon", width="7")
    d_endu_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")
    val_endu_field=Spinbox(gui, from_=0, to=10, width=5,bg ="bisque", fg="maroon")
    bonus_field=Entry(gui,bg ="bisque", fg="maroon", width="7")

    #res_d_field=Entry(gui)
    #res_cuirasse_field=Entry(gui)
    #res_encaissement_field=Entry(gui)


    #Menu
    #ETAT
    stats.grid(row=0, column=1)

    pv.grid(row=1, column=0)
    pv_field.grid(row=1, column=1)

    val_endu.grid(row=2, column=0)
    val_endu_field.grid(row=2, column=1)

    shield.grid(row=3, column=0)
    shield_field.grid(row=3, column=1)

    bonus.grid(row=4, column=0)
    bonus_field.grid(row=4, column=1)

    #DICES
    dice.grid(row=0, column=4)

    atq.grid(row=1, column=3)
    atq_field.grid(row=1, column=4)

    d_endu.grid(row=2, column=3)
    d_endu_field.grid(row=2, column=4)

    defe.grid(row=3, column=3)
    defe_field.grid(row=3, column=4)

    #RESULTAT

    resultat.grid(row=5, column=1)

    degat_label.grid(row=6, column=0)
    degat.grid(row=6, column=1)
    #res_d_field.grid(row=6, column=1)

    res_cuirasse_label.grid(row=7, column=0)
    res_cuirasse.grid(row=7, column=1)
    #res_cuirasse_field.grid(row=7, column=1)

    res_encaissement_label.grid(row=8, column=0)
    res_encaissement.grid(row=8, column=1)
    #res_encaissement_field.grid(row=8, column=1)
    clearEntry.grid(row=9, column=1)

    #start
    gui.mainloop()












