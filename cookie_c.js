let body = document.querySelector("body");
let para1 = body.querySelector("p");
let bouton_c = body.querySelector("button");
let bouton_am = document.getElementById("button2");
let para2 = body.querySelector("p0");

bouton_c.addEventListener("click", compter)
let compteur = 0
let compteur_tot = 0
let bonus = 0
function compter() {
    compteur = Math.round((compteur+ 1 +bonus) *100) /100 ;
    compteur_tot = Math.round((compteur_tot +1 +bonus)*100)/100;
    if (compteur_tot > 500 ) {
        compteur =  Math.round((compteur+1 + bonus)*100)/100;
        compteur_tot =  Math.round((compteur_tot +1 +bonus)*100)/100;
    }
    if (compteur_tot > 2000 ) {
        compteur =  Math.round((compteur+2 + 2 * bonus)*100)/100;
        compteur_tot =  Math.round((compteur_tot +2 +2 * bonus)*100)/100;
    }
    afficher(compteur);
}

bouton_am.addEventListener("click", ameliorer)
let cout = 15
let num_am = 0
function ameliorer() {
    num_am = num_am + 1
    if (compteur >= cout) {
        compteur = Math.round((compteur - cout)*100)/100 ;
        cout = cout * 2;
        bonus = bonus+0.010;
    }
    para2.innerHTML = "Dépensez " + cout + " cookies pour améliorer :";
    afficher(compteur);
}
/* Fonction d'affichage dans la page web */
function afficher(valeur) {
    para1.innerHTML = valeur;
}
