var ticks = 0;

function changeEgg() {
  ticks ++;

  if (ticks == 3){
    document.getElementById("fullEgg").src = "/static/img/egg1.jpg";
  }
  if (ticks == 7){
    document.getElementById("fullEgg").src = "/static/img/egg2.jpg";
  }
  if (ticks == 8){
    document.getElementById("fullEgg").src = "/static/img/lexa.jpg";
  }
  if (ticks == 9){
    document.getElementById("fullEgg").src = "/static/img/egg.jpg";
    ticks = 0;
  }
  document.getElementById('ticksField').innerHTML = 'Постучал по яйцу ' + ticks + ' раз'
}

function changeText() {
	document.getElementById('Header').innerHTML = "IDK";
}

function showEgg() {
  if (document.getElementById('fullEgg').style.display == 'none'){
    document.getElementById('fullEgg').style.display = 'block'
  }
  else{
    document.getElementById('fullEgg').style.display = 'none'

  }
}
function showDate() {
  document.getElementById('demo').innerHTML = Date()
}
