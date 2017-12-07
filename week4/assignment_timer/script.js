// On click of 'submit' button, call a function that starts a countdown timer at the number input by the user. The number should incriment down one second at a time until it reaches zero. Once it hits zero, a 'Time!' message should appear.


function myFunction() {

}


function startCountdown() {
  let startNum = Number(document.getElementById('startNumField').value + '000');
    console.log('Number in milliseconds: ', startNum);


  setInterval(function(){
    let interval = 0;
    interval ++;
    console.log(interval);
  }, 3000);

  console.log('Done counting')
}
