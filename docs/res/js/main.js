window.onload = function() {
    elem_inputs.refresh();
    elem_inputs.pv_max["old_value"] = elem_inputs.pv_max.valueAsNumber;

    elem_inputs.pv_max.onchange = function() {
        
        if(this.old_value > this.valueAsNumber){
            elem_inputs.pv_reste.valueAsNumber -= this.old_value - this.valueAsNumber;
        }else if(this.old_value < this.value){
            elem_inputs.pv_reste.valueAsNumber += this.valueAsNumber - this.old_value;
        }
        this.old_value = this.valueAsNumber;
        elem_inputs.pv_reste.onchange()
    }

    elem_inputs.pv_reste.onchange = function() {
        if(this.valueAsNumber >= elem_inputs.pv_max.valueAsNumber){
            this.valueAsNumber = elem_inputs.pv_max.valueAsNumber
        }
        if(this.valueAsNumber <= 0){
            this.valueAsNumber = 0;
        }
        if(isNaN(this.valueAsNumber)){
            this.valueAsNumber = elem_inputs.pv_max.valueAsNumber
        }
    }
}

function log_ecriture(){

} //A faire plus tard quand le cadre aura été fait, partie 2 du programme
//s'efface quand on actualise !

function clearAll(){} //Ajouter un bouton d'effacer tous les champs mais NE DOIT PAS EFFACER LES LOGS

function test_none(val){
  //parce que j'ai la flemme de marquer un pavé géant
  if (((! t) || (t.trim().length == 0))) {
      return true;
  }
  return false;
}

/* function checkError()
{
  if ((isNaN(pv_max)) || (isNaN(atq)) || (isNaN(shield)) || (isNaN(valeur_dé_endurance)) || (isNaN(pv_restant)) || (isNaN(bonus_entry)) || (isNaN(de_defense)))
  {
    //Les valeurs qui ont un problème deviennent rouges
    //Affichage du message ("Erreur, les variables ne sont pas numériques")
  }
  else if (((test_none(pv_max)) || (test_none(atq)) || (test_none(shield)) || (test_none(val_de_endurance)) || (test_none(pv_restant)) || (test_none(de_defense)))
  { //Même chose
  //affiche le message d'erreur "Erreur, les variables sont vides"
  }
  else if ( (atq > 10) || (defense > 10) || (endurance_dé > 10) || (bonus_entry > 10))
  {
    //Même chose
    //affiche le message ("Erreur, Certaines valeurs sont supérieures à 10.")
  }
  else if ((bonus_entry > 100)||(shield > 100))
  {
    //"Certaines valeurs sont supérieures à 100"
  }
  else if ((pv_max <=0))
  {
    //Les PV sont inférieurs ou égaux à 0.
  }
  else if ((pv_restant > pv_max))
  {
    //Les pv restants sont supérieurs aux PV maximum.
  }
} //truc en rouge qui indique quand y'a des erreurs*/

function grisage_spinbox (){
    // En gros, quand le radiobutton "attaque normale" est sélectionné, le spinbox "capacité" est grisé et non utilisable !!
    // de même, quand le bonus est sur aucun, la spinbox a côté est grisé !
}
