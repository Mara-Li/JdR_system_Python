/*
A faire :
- Ajouter un bouton pour clear les champs
- Permettre de lancer le programme avec "ENTER"
- Faire que le champ pv restant change automatiquement quand on change les pv totaux/max
- Mettre la boite pour les LOGS
- aligner les boutons
*/

/*Valeurs des boutons radio et selections:
 * 
 *  des_esquive -> 0 pour Endurance, 1 pour esquive raté
 * 
 *  arme -> 0 pour aucun, 1 pour pouvoir, 2 fusil, 3 projectile, 4 épée,
 *          5 contondant, 6 couteau, 7 pistolet, 8 artillerie, 9 autre
 *  
 *  atk_type -> 0 pour atk normale, 1 pour capacité
 *  
 *  capacite_type -> 0 pour Burst, 1 perforant, 2 autre
 *  
 *  dist_atk -> 0 pour cac, 1 distance
 */

const elemIDs = [
    "pv_max",
    "pv_reste",
    "bouclier",
    "endurance",
    "des_atk",
    "des_def",
    "arme",
    "bonus",
    "capacite_type",
    "des_bonus_def"
];

const radioGroupsName = [
    "des_esquive",
    "atk_type",
    "dist_atk"
]

class Elements_getter{
    constructor(lstID, lstRadio){
        this._idLst = lstID;
        this._radioLst = lstRadio;
        lstID.forEach(id => {
            this[id] = document.getElementById(id);
        });
        lstRadio.forEach(name => {
            this[name] = this.getValueFromRadio(name);
        });
    }
    
    getValueFromRadio(group_name){
        var lst_radio = document.getElementsByName(group_name)
        for(var i = 0; i < lst_radio.length; i++){
            if(lst_radio[i].checked){
                return lst_radio[i];
            };
        };
        return undefined;
    }
    
    refresh(){
        this._idLst.forEach(id => {
            this[id] = document.getElementById(id);
        });
        this._radioLst.forEach(name => {
            this[name] = this.getValueFromRadio(name);
        });
        return this;
    }
}

var elem_inputs = new Elements_getter(elemIDs, radioGroupsName);
document.onload = elem_inputs.refresh();


function choix_bonus(){
    let b;
    bonus=elem_inputs.arme.value;
    bonus_val=elem_inputs.bonus.value;
    dist=elem_inputs.dist_atk.checked ; //récupération du bouton distance sur la boite bonus
    switch (bonus) {
        case 0: //Aucun
            b = 0;
            break;    
        case 1: //Pouvoir
            b = 10 + bonus_val;
            break;
        case 2: //Fusil
            b = 10 + bonus_val;
            if (dist) { //est checked
                b = b + 5;
            };
            break;
        case 3: //Projectile
            b = 5 + bonus_val;
            break;
        case 4: //Épée
            b = 10 + bonus_val;
            break;
        case 5: //Contondant
            b = 15 + bonus_val;
            break;
        case 6: //Couteau
            b = 5 + bonus_val;
            break;
        case 7: //Pistolet
            b = 8 + bonus_val;
            break;
        case 8: //Artillerie
            b = 15 + bonus_val;
            if (dist) { //est check
                b = b + 10;
            };
            break;
        case 9: //Autre
            b = bonus_val;
            break;
    }
    return b;
}
    
    
    function reussite_endurance(endu_de, endu_val, PV, d, shield)
    {
        d=Math.abs(d*PV);
        var bouclier=Math.abs(d*(1-shield)); //au besoin, placé des int pour convertir les valeurs
        remise=elem_inputs.bonus.checked//checkbox "bonus"
        var finaux=0;
        if (remise) //est check
        {
            if ((endu_de > endu_val) || (endu_de==endu_val))
            {
                finaux=bouclier;
            }
            else if (endu_val == 0)
            {
                finaux=bouclier;
            }
            else {
                finaux=bouclier*(1-(10*Math.abs((endu_val - endu_de)+1))/100);
            }
        }
        else {
            if (endu_de > endu_val)
            {
                finaux=bouclier;
            }
            else if (endu_val==0)
            {
                finaux=bouclier
            }
            else
            {
                finaux= bouclier*(1-(10*Math.abs((endu_val - endu_de)+1))/100)
            }
        }
        if (finaux >= PV)
        {
            finaux=PV
        }
    }
    
    function vie_restante(finaux)
    {
        vie = elem_inputs.pv_reste.value - finaux //champ pv restant
        msg_pv=vie;
        if (vie <= 0)
        {
            vie=0; //au besoin, mettre en caractère
            msg_pv='X';
        }
        //vider le champ "PV_restant"
        //inserer la valeur de vie restante
        //inserer msg_pv
    }
    
    function capacite_bonus(bonus)
    {
        atq = elem_inputs.des_atk.value //valeur dé champ Attaque
        if (atq==0){
            bonus=bonus*1.8;
        }
        else if (atq==1){
            bonus=bonus*1.4;
        }
        return bonus;
    }
    
    function calculate_degat(bonus, atq, defe){
        var d;
        d = Math.abs((ATQ - DEFE));
        if ((d === 0)) {
            d = (0 + bonus);
        } else if ((d === 1)) {
            d = (0.05 + bonus);
        }
        else if ((d === 2)) {
            d = (0.1 + bonus);
        }
        else if (((d === 4) || (d === 3))) {
            d = (0.2 + bonus);
        }
        else if (((d === 5) || (d === 6))) {
            d = (0.3 + bonus);
        }
        else if (((d === 7) || (d === 8))) {
            d = (0.4 + bonus);
        }
        else if ((d >= 9)) {
            d = (0.5 + bonus)
        }
        return d;
        
    }
    
    function degat_burst(bonus, atq, defe, endu_val)
    {
        var d;
        if ((ATQ === 0)) {
            d = (0.25 + bonus);
            endu_val = 0;
        } else if ((DEFE === 0)) {
            d = 0;
        }
        else if ((ATQ === 1))
        {
            d = calculate_degat(bonus, ATQ, DEFE)
        }
        else
        {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        return [d, endu_val];
    }
    
    function degat_burst_bouclier(bonus, atq, defe, endu_val)
    {
        var d;
        if ((ATQ === 0)) {
            d = (0.38 + bonus);
            endu_val = 0;
        }
        else if ((DEFE === 0)) {
            d = 0;
        } else if ((ATQ === 1)) {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        else {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        return [d, endu_val];
    }
    
    function degat_perforant(bonus, atq, defe, endu_val)
    {
        var d;
        if ((ATQ === 0))
        {
            d = (0.4 + bonus);
            endu_val = 0;
        }
        else if ((DEFE === 0))
        {
            d = 0;
        }
        else if ((ATQ === 1))
        {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        else
        {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        return [d, endu_val];
    }
    
    function degat_autre(bonus, atq, defe, endu_val)
    {
        var d;
        if ((ATQ === 0))
        {
            d = (0.5 + bonus);
            endu_val = 0;
        }
        else if ((DEFE === 0))
        {
            d = 0;
        } else if ((ATQ === 1))
        {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        else
        {
            d = calculate_degat(bonus, ATQ, DEFE);
        }
        return [d, endu_val];
    }
    
    function degat_type()
    {
        var bonus_attaque, bonus_type, d, endu_de, endu_val, finaux, max;
        var bonus = elem_inputs.bonus.value //valeur du champ "bonus"
        var pv = elem_inputs.pv_max.value //valeur du champ PV au départ
        var atq = elem_inputs.des_atk.value //valeur du dés d'Attaque
        var defe = elem_inputs.des_def.value //valeur du dé de défense
        var sel_defe = elem_inputs.des_esquive.value //type de défense - valeur dans dés [Endurance ou Esquive raté]
        var type_capa = elem_inputs.capacite_type.value //Valeur de la spinbox dans capacité ["Burst", "Autre", "Perforante"]
        var shield = elem_inputs.bouclier.value/100 //valeur du champ "Bouclier"
        var endu_val = elem_inputs.endurance.value //valeur champ "endurance" dans stats
        
        switch (sel_defe) {
            case 0: //Endurance
                endu_de = defe;
                break;
            case 1: //Esquive raté
                endu_val = 0;
                endu_de = 10;
                break;
        }

        switch (type_capa) {
            case 0: //burst
                if (shield !==0)
                {
                    bonus_type = capacite_bonus(15);
                    bonus = ((bonus_type + bonus) / 100);
                    [d, endu_val] = degat_burst_bouclier(bonus, atq, defe, endu_val); //est ce qu'on peut faire ça en JS ?
                }
                else {
                    bonus_type = capacite_bonus(25);
                    bonus = ((bonus + bonus_type) / 100);
                    [d, endu_val] = degat_burst(bonus, atq, defe, endu_val);
                }
                break;
        
            case 1: //Perforant
                bonus_type = capacite_bonus(15);
                bonus = ((bonus_type + bonus) / 100);
                endu_val = 0;
                shield=0;
                [d, endu_val] = degat_perforant(bonus, ATQ, DEFE, endu_val);
                break;
            
            case 2: //Autre
                bonus_attaque = choix_bonus();
                bonus = capacite_bonus(bonus);
                bonus = ((bonus_attaque + bonus) / 100);
                endu_val = elem_inputs.endurance.value//récupérer la valeur du champ d'endurance
                shield = elem_inputs.shield.value//???
                [d, endu_val] = degat_autre(bonus, atq, defe, endu_val);
        }

        finaux=reussite_endurance(endu_de, endu_val, pv, d, shield);
        finaux=(finaux/1.4) //Au besoin, convertir en int
        max=finaux;
        if (pv >= 1000)
        {
            max=200;
        }
        else if ( (pv > 100) && (pv < 1000))
        {
            max=100;
        }
        else if (pv <= 100)
        {
            max=80;
        }
        if (finaux > max)
        {
            finaux=max;
        };
        //inserer la valeur "finaux" dans le champ concerné dans résultat
        vie_restante(finaux);
    }
    
    function degat_normaux()
    {
        var atq, defe, pv, shield, bonus, d, endu_de, endu_val, finaux, max;
        bonus = choix_bonus();
        pv = elem_inputs.pv_max.value //champ pv du programme
        atq = elem_inputs.des_atk.value //champ attaque dans dé
        defe = elem_inputs.des_def.value //champ défense dans dé
        bonus = (bonus/100);
        endu_val = elem_inputs.endurance.value //valeur de l'endurance dans les stats
        shield = elem_inputs.bouclier.value //valeur du champ "bouclier"
        shield=shield/1000;
        d=calculate_degat(bonus, atq, defe);
        sel_def=button_check()//insérer le nom qui correspond
        if (sel_def) //est 1 ; checké ?
        {
            endu_de=defe;
        }
        else
        {
            endu_val=0;
            endu_de=10;
        }
        if (atq==0)
        {
            d=(0.5+bonus);
            endu_val=0
        }
        else if (defe==0)
        {
            d=0;
        }
        else if (atq==1)
        {
            endu_val=0;
        }
        finaux=reussite_endurance(endu_de, endu_val, pv, d, shield);
        finaux=finaux/1.4;
        max=finaux;
        if (pv >=1000){
            max=200;
        }
        else if ((pv >100) && (pv <1000))
        {
            max=100;
        }
        else if (pv <100)
        {
            max=80;
        }
        if (finaux > max)
        {
            finaux=max;
        }
        //insérer la valeur final
        vie_restante(finaux);
    }
    
    function log_ecriture()
    {} //A faire plus tard quand le cadre aura été fait, partie 2 du programme
    //s'efface quand on actualise !
    
    function clearAll(){} //Ajouter un bouton d'effacer tous les champs mais NE DOIT PAS EFFACER LES LOGS
    
    function checkError(){} //truc en rouge qui indique quand y'a des erreurs
    
    
    function calculate()
    {
        //test check des erreurs
        selection = elem_inputs.atk_type.value //valeur si on choisit une attaque normale ou une Capacité
        if (selection) //est checké ? egale à 1 ?  égale à "Attaque normale" ?)
        {
            degat_normaux();
        }
        else {
            degat_type();
        }
        log_ecriture();
    }
    
    function grisage_capacité (){
        // En gros, quand le radiobutton "attaque normale" est sélectionné, le spinbox "capacité" est grisé et non utilisable !!
    }
    

    