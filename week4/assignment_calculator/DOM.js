
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
  document.getElementById('result').innerHTML = 0;
}

// function plusMinus() {
//   console.log('Change +/- sign');
//   document.getElementById('result').innerHTML = unshift('-');
// }

// function percentage() {
//   console.log('Change number to percentage');
// }


// Operator Functions:
function divide() {
  console.log('Divide');
  let result = Number(document.getElementById('num1').value) / Number(document.getElementById('num2').value);

  document.getElementById('result').innerHTML = result;

}

function multiply() {
  console.log('Multiply');
  let result = Number(document.getElementById('num1').value) * Number(document.getElementById('num2').value);

  document.getElementById('result').innerHTML = result;
}

function subtract() {
  console.log('Subtract');
  let result = Number(document.getElementById('num1').value) - Number(document.getElementById('num2').value);

  document.getElementById('result').innerHTML = result;
}

function add() {
  console.log('Add');
  let result = Number(document.getElementById('num1').value) + Number(document.getElementById('num2').value);

  document.getElementById('result').innerHTML = result;
}

// function equals() {
//   console.log('Equal');
// }
