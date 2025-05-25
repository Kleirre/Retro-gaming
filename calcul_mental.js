  let para0 = document.getElementById('0');
  let para1 = document.getElementById('1');
  let para2 = document.getElementById('2');
  let para3 = document.getElementById('3');
  let para4 = document.getElementById('4');
  let add = document.getElementById('add');
  let sou = document.getElementById('sou');
  let mul = document.getElementById('mul');

let score = 0;
let attempt = 0;
let i = 0;

add.addEventListener("click", addition);
function addition() {
  para3.innerHTML ="";
  para0.style.display = 'none' ;
  para1.innerHTML = "Vous avez choisi Addition !";
  let reponseInput = document.createElement('input');
  reponseInput.setAttribute('type', 'text');
  para3.appendChild(reponseInput);
  let submitButton = document.createElement('button');
  submitButton.innerHTML = "Vérifier la réponse";
  para3.appendChild(submitButton);
  let nombre1 = Math.floor(Math.random() * 99) + 1;
  let nombre2 = Math.floor(Math.random() * 99) + 1;
  para2.innerHTML = `Combien font ${nombre1} + ${nombre2}?`;
	
  submitButton.addEventListener("click", function() {
    let reponse = parseInt(reponseInput.value);
    if (reponse === nombre1 + nombre2) {
      score++;
      para3.innerHTML = "Correct!";
    } else {
      para3.innerHTML = `Erreur, la réponse était : ${nombre1 + nombre2}`;
    }
    attempt++;
    para4.innerHTML = `Votre score est ${score} / ${attempt}`;
    i = i+1
    reponseInput.remove();
    submitButton.remove();
    if (i<10) {
      setTimeout(() => {
        addition();
      }, 1250);
    } else {
   setTimeout(() => {
        reinitialiser();
      }, 1250);
    }
	});
} 


sou.addEventListener("click", soustraction);
function soustraction() {
  para3.innerHTML ="";
  para0.style.display = 'none' ;
  para1.innerHTML = "Vous avez choisi Soustraction !";
  let reponseInput = document.createElement('input');
  reponseInput.setAttribute('type', 'text');
  para3.appendChild(reponseInput);
  let submitButton = document.createElement('button');
  submitButton.innerHTML = "Vérifier la réponse";
  para3.appendChild(submitButton);
  let nombre1 = Math.floor(Math.random() * 99) + 1;
  let nombre2 = Math.floor(Math.random() * nombre1) + 1;
  para2.innerHTML = `Combien font ${nombre1} - ${nombre2}?`;

  submitButton.addEventListener("click", function() {
    let reponse = parseInt(reponseInput.value);
    if (reponse === nombre1 - nombre2) {
      score++;
      para3.innerHTML = "Correct!";
    } else {
      para3.innerHTML = `Erreur, la réponse était : ${nombre1 - nombre2}`;
    }
    attempt++;
    para4.innerHTML = `Votre score est ${score} / ${attempt}`;
    i = i+1
    reponseInput.remove();
    submitButton.remove();
    if (i<10) {
      setTimeout(() => {
        soustraction();
      }, 1250);
    } else {
   setTimeout(() => {
        reinitialiser();
      }, 1250);
    }
	});
}

mul.addEventListener("click", multiplication);
function multiplication() {
  para3.innerHTML ="";
  para0.style.display = 'none' ;
  para1.innerHTML = "Vous avez choisi Multiplication !";
  let reponseInput = document.createElement('input');
  reponseInput.setAttribute('type', 'text');
  para3.appendChild(reponseInput);
  let submitButton = document.createElement('button');
  submitButton.innerHTML = "Vérifier la réponse";
  para3.appendChild(submitButton);
  let nombre1 = Math.floor(Math.random() * 9) + 1;
  let nombre2 = Math.floor(Math.random() * 9) + 1;
  para2.innerHTML = `Combien font ${nombre1} x ${nombre2}?`;

  submitButton.addEventListener("click", function() {
    let reponse = parseInt(reponseInput.value);
    if (reponse === nombre1 * nombre2) {
      score++;
      para3.innerHTML = "Correct!";
    } else {
      para3.innerHTML = `Erreur, la réponse était : ${nombre1 * nombre2}`;
    }
    attempt++;
    para4.innerHTML = `Votre score est ${score} / ${attempt}`;
    i = i+1
    reponseInput.remove();
    submitButton.remove();
    if (i<10) {
      setTimeout(() => {
        multiplication();
      }, 1250);
    } else {
   setTimeout(() => {
        reinitialiser();
      }, 1250);
    }
	});
}




function reinitialiser() {
  score = 0;
  attempt = 0;
  i = 0;
  para3.innerHTML ="";
  para2.innerHTML ="";
  para1.innerHTML ="";
  para4.innerHTML ="";
  para0.style.display = 'block' ;

}
