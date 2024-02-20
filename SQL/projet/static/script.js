/* Fonctions pour le tri en descandant et ascendant */
let chg_desc = document.getElementById('desc');
chg_desc.addEventListener('click', inversement1); /* Quand il y a un clic sur le bouton "tri décroissant", mettre l'id dans une variable chg_desc */
let chg_asc = document.getElementById('asc');
chg_asc.addEventListener('click', inversement2); /* Quand il y a un clic sur le bouton "tri croissant", mettre l'id dans une variable chg_asc */

function inversement1(){ /* Fonction qui ajoute un _D a la fin d'un name pour la recherche en desc */
	boutons = document.getElementsByClassName('bouton_tri');
	for (var i =0; i<boutons.length; i=i+1) { /* Quand le bouton i est séléctionné */
		if (boutons[i].name.includes("_D")==false){ /* Si le name du bouton i  n'a pas déjà un _D en mettre un */
		boutons[i].name += "_D";}
	}
}

function inversement2(){ /* Fonction qui enlève un _D a la fin d'un name pour la recherche en asc */
	boutons = document.getElementsByClassName('bouton_tri');
	for (var i =0; i<boutons.length; i=i+1) { /* Quand le bouton i est séléctionné */
		if (boutons[i].name.includes("_D")==true){ /* Si le name du bouton i a déjà un _D: passer à l'étape suivante */
		boutons[i].name = boutons[i].name.replace("_D", "");} /* remplace le _D par une chaîne de caractère vide  */
	}
}

/* Fonction pour l'écran de chargement: */
window.addEventListener("load", function(){ 
	document.querySelector('.preloader').style.display = "none"	 /* Tant que la page n'est pas chargée laisser afficher le loader */
});


