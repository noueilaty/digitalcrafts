
// Functions:
document.getElementById("ac").addEventListener("click", ac);
// document.getElementById("plusMinus").onclick =
// document.getElementById("percentage").onclick =


// Operators:
document.getElementById("divide").addEventListener("click", divide);
document.getElementById("multiply").addEventListener("click", multiply);
document.getElementById("subtract").addEventListener("click", subtract);
document.getElementById("add").addEventListener("click", add);
document.getElementById("equals").addEventListener("click", equals);


// Functional Buttons:
function ac() {
  console.log('Clear');
  document.getElementById('inputFields').reset();
}

function plusMinus() {
  console.log('Change +/- sign');
}

function percentage() {
  console.log('Change number to percentage');
}


// Operator Functions:
function divide() {
  console.log('Divide');
  let result = Math.floor(document.getElementById('num1').value) / Math.floor(document.getElementById('num2').value);

  Math.floor(document.getElementById('result').innerHTML) = result;

}

function multiply() {
  console.log('Multiply');
  let result = Math.floor(document.getElementById('num1').value) * Math.floor(document.getElementById('num2').value);

  document.getElementById('result').innerHTML = result;
}

function subtract() {
  console.log('Subtract');
  let result = Math.floor(document.getElementById('num1').value) - Math.floor(document.getElementById('num2').value);

  Math.floor(document.getElementById('result').innerHTML) = result;
}

function add() {
  console.log('Add');
  let result = Math.floor(document.getElementById('num1').value) + Math.floor(document.getElementById('num2').value);

  document.getElementById('result').innerHTML = result;
}

function equals() {
  console.log('Equal');
}
