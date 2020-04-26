/*Valeurs des boutons radio et selections:
*
*  des_esquive -> 0 pour Endurance, 1 pour esquive raté
*
*  arme -> 0 pour aucun, 1 pour pouvoir, 2 fusil, 3 projectile, 4 épée,
*          5 contondant, 6 couteau, 7 pistolet, 8 artillerie, 9 autre
*
*  atq_type -> 0 pour atq normale, 1 pour capacité
*
*  capacite_type -> 0 pour Burst, 1 perforant, 2 autre
*
*  dist_atq -> 0 pour cac, 1 distance
*/

const elemIDs = [
    "pv_max",
    "pv_reste",
    "bouclier",
    "endurance",
    "des_atq",
    "des_def",
    "arme",
    "bonus",
    "capacite_type",
    "des_bonus_def",
    "res_deg",
    "res_pv",
    "log_box"
];

const radioGroupsName = [
    "des_esquive",
    "atq_type",
    "dist_atq"
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

function calculate(){
    //test check des erreurs
    elem_inputs.refresh();
    selection = parseInt(elem_inputs.atq_type.value); //valeur si on choisit une attaque normale ou une Capacité
    if (selection == 0){ //est checké ? egale à 1 ?  égale à "Attaque normale" ?)
        degat_normaux();
    }else {
        degat_type();
    }
    log_ecriture();
}

function degat_normaux(){
    var remise = elem_inputs.des_bonus_def.checked;
    var d, endu_de, finaux, max;
    var bonus = choix_bonus();
    var bonus = (bonus/100);
    var pv = parseInt(elem_inputs.pv_max.value); //champ pv du programme
    var atq = parseInt(elem_inputs.des_atq.value); //champ attaque dans dé
    var defe = parseInt(elem_inputs.des_def.value); //champ défense dans dé
    var endu_val = parseInt(elem_inputs.endurance.value); //valeur de l'endurance dans les stats
    var shield = parseInt(elem_inputs.bouclier.value)/100; //valeur du champ "bouclier"
    d=calculate_degat(bonus, atq, defe);
    sel_def = parseInt(elem_inputs.des_esquive.value); //insérer le nom qui correspond
    if (!sel_def){ //Endurance (valeur = 0)
        endu_de=defe;
    }else{ //Esquive & test (valeur = 1)
        if (remise) {
            if (defe < (atq/2)){ //esquive réussi : Pas de dégât
                defe=0;
                endu_de=0;
            }else { //esquive raté
                endu_val=0;
                endu_de=10;


            }
        }else {
            if (defe <= (atq/2)){ //esquive réussi : pas de dégât
                defe=0;
                endu_de=0;
            }
            else { //esquive raté
                endu_val=0;
                endu_de=10;
            }
        }
    }

    if (atq == 0){
        d = (0.5+bonus);
        endu_val = 0;
    }else if (defe == 0){
        d = 0;
    }else if (atq == 1){
        endu_val=0;
    }

    finaux = reussite_endurance(endu_de, endu_val, pv, d, shield);
    finaux = Math.trunc(finaux/1.4);
    max = finaux;
    if (pv >=1000){
        max=200;
    }else if ((pv >100) && (pv <1000)){
        max=100;
    }else if (pv <100){
        max=80;
    }

    if (finaux > max){
        finaux = max;
    }

    vie_restante(finaux);
}

function degat_type(){
    var remise = elem_inputs.des_bonus_def.checked;
    var bonus_attaque, bonus_type, d, endu_de, finaux, max;
    var bonus = parseInt(elem_inputs.bonus.value); //valeur du champ "bonus"
    var pv = parseInt(elem_inputs.pv_max.value); //valeur du champ PV au départ
    var atq = parseInt(elem_inputs.des_atq.value); //valeur du dés d'Attaque
    var defe = parseInt(elem_inputs.des_def.value); //valeur du dé de défense
    var sel_defe = parseInt(elem_inputs.des_esquive.value); //type de défense - valeur dans dés [Endurance ou Esquive raté]
    var type_capa = parseInt(elem_inputs.capacite_type.value); //Valeur de la spinbox dans capacité ["Burst", "Autre", "Perforante"]
    var shield = parseInt(elem_inputs.bouclier.value)/100; //valeur du champ "Bouclier"
    var endu_val = parseInt(elem_inputs.endurance.value); //valeur champ "endurance" dans stats

    switch (sel_defe) {
        case 0: //Endurance
            endu_de = defe;
            break;
        case 1: //Esquive
        if (remise) {
          if (defe < (atq/2)){
            defe=0;
            endu_de=0;
          }else {
            endu_val=0;
            endu_de=10;
          }
        }
          else {
            if (defe <= (atq/2)){
              defe=0;
              endu_de=0;
            }else {
              endu_val=0;
              endu_de=10;
            }
          }
            break;
    }

    switch (type_capa) {
        case 0: //burst
            if (shield != 0){
                bonus_type = capacite_bonus(15);
                bonus = (bonus_type + bonus) / 100;
                [d, endu_val] = degat_burst_bouclier(bonus, atq, defe, endu_val);
            }else{
                bonus_type = capacite_bonus(25);
                bonus = ((bonus + bonus_type) / 100);
                [d, endu_val] = degat_burst(bonus, atq, defe, endu_val);
            }
            break;

        case 1: //Perforant
            bonus_type = capacite_bonus(15);
            bonus = ((bonus_type + bonus) / 100);
            endu_val = 0;
            shield = 0;
            [d, endu_val] = degat_perforant(bonus, atq, defe, endu_val);
            break;

        case 2: //Autre
            bonus_attaque = choix_bonus();
            bonus = capacite_bonus(bonus);
            bonus = ((bonus_attaque + bonus) / 100);
            endu_val = parseInt(elem_inputs.endurance.value); //récupérer la valeur du champ d'endurance
            shield = parseInt(elem_inputs.shield.value);
            [d, endu_val] = degat_autre(bonus, atq, defe, endu_val);
            break;
    }

    finaux = reussite_endurance(endu_de, endu_val, pv, d, shield);
    finaux = Math.trunc(finaux/1.4);
    max = finaux;
    if (pv >= 1000){
        max = 200;
    }else if ((pv > 100) && (pv < 1000)){
        max = 100;
    }else if (pv <= 100){
        max = 80;
    }
    if (finaux > max){
        finaux = max;
    };
    vie_restante(finaux);
}

function choix_bonus(){
    var b;
    var bonus = parseInt(elem_inputs.arme.value);
    var bonus_val = parseInt(elem_inputs.bonus.value);
    var dist = parseInt(elem_inputs.dist_atq.value); //récupération du bouton distance sur la boite bonus
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
    if (b>=100) {
      b=100;
    }
    return b;
}


function reussite_endurance(endu_de, endu_val, pv, d, shield){
    var finaux;
    var d = Math.abs(Math.trunc(d * pv));
    var bouclier = Math.abs(Math.trunc(d * (1 - shield))); //au besoin, placé des int pour convertir les valeurs
    var remise = elem_inputs.des_bonus_def.checked; //checkbox "bonus"

    if (remise){ //est check
        if ((endu_de > endu_val) || (endu_de == endu_val)){
            finaux = bouclier;
        }else if (endu_val == 0){
            finaux = bouclier;
        }else{
            finaux = bouclier * (1 - (10 * (Math.abs(endu_val - endu_de) + 1 )) /100);
        }
    }else {
        if (endu_de > endu_val){
            finaux = bouclier;
        }else if (endu_val==0){
            finaux = bouclier;
        }else{
            finaux = bouclier * (1 - (10 * (Math.abs(endu_val - endu_de) + 1)) /100);
        }
    }
    if (finaux >= pv){
        finaux = pv;
    }
    return finaux;
}



function capacite_bonus(bonus){
    var atq = parseInt(elem_inputs.des_atq.value) //valeur dé champ Attaque
    if (atq==0){
        bonus = bonus * 1.8;
    }else if (atq == 1){
        bonus = bonus * 1.4;
    }
    return bonus;
}

function calculate_degat(bonus, atq, defe){
    var d;
    d = Math.abs(atq - defe);
    switch(d){
        case 0:
            d = (0 + bonus);
            break;
        case 1:
            d = (0.05 + bonus);
            break;
        case 2:
            d = (0.1 + bonus);
            break;
        case 3: //En cas de 3 ou de 4, faire d = 0.2 + bonus
        case 4:
            d = (0.2 + bonus);
            break;
        case 5:
        case 6:
            d = (0.3 + bonus);
            break;
        case 7:
        case 8:
            d = (0.4 + bonus);
            break;
        default:
            d = (0.5 + bonus);
            break;
    }
    return d;
}

function degat_burst(bonus, atq, defe, endu_val){
    let d;
    if (atq == 0) {
        d = 0.25 + bonus;
        endu_val = 0;
    }else if (defe == 0){
        d = 0;
    }else if(atq == 1){
        d = calculate_degat(bonus, atq, defe);
    }else{
        d = calculate_degat(bonus, atq, defe);
    }
    return [d, endu_val];
}

function degat_burst_bouclier(bonus, atq, defe, endu_val){
    let d;
    if (atq == 0){
        d = (0.38 + bonus);
        endu_val = 0;
    }else if (defe == 0){
        d = 0;
    }else if(atq == 1){
        d = calculate_degat(bonus, atq, defe);
    }else{
        d = calculate_degat(bonus, atq, defe);
    }
    return [d, endu_val];
}

function degat_perforant(bonus, atq, defe, endu_val){
    var d;
    if (atq == 0){
        d = (0.4 + bonus);
        endu_val = 0;
    }else if (defe == 0){
        d = 0;
    }else if(atq == 1){
        d = calculate_degat(bonus, atq, defe);
    }else{
        d = calculate_degat(bonus, atq, defe);
    }
    return [d, endu_val];
}

function degat_autre(bonus, atq, defe, endu_val){
    var d;
    if (atq == 0){
        d = (0.5 + bonus);
        endu_val = 0;
    }else if (defe == 0){
        d = 0;
    } else if (atq == 1){
        d = calculate_degat(bonus, atq, defe);
    }else{
        d = calculate_degat(bonus, atq, defe);
    }
    return [d, endu_val];
}

function phrase_esquive(finaux){
  var remise = elem_inputs.des_bonus_def.checked;
  var atq = parseInt(elem_inputs.des_atq.value); //champ attaque dans dé
  var defe = parseInt(elem_inputs.des_def.value); //champ défense dans dé
  sel_def = parseInt(elem_inputs.des_esquive.value);
  if (sel_def){
    if (remise){
      if (defe < (atq/2)){
        finaux='Esquive réussie';
      }
    }
    else {
      if (defe <= (atq/2)){
        finaux='Esquive réussie';
      }
    }
  }
  return finaux;

}

function vie_restante(finaux){
    var vie = parseInt(elem_inputs.pv_reste.value) - finaux; //champ pv restant
    finaux=phrase_esquive(finaux)
    if (isNaN(finaux)){
      vie=elem_inputs.pv_max.value;
    }
    elem_inputs.res_deg.innerHTML = finaux;
    elem_inputs.pv_reste.value = (vie <= 0 || isNaN(vie)) ? 0 : vie;
    elem_inputs.res_pv.innerHTML = (vie <= 0 || isNaN(vie)) ? "X" : vie;
}
