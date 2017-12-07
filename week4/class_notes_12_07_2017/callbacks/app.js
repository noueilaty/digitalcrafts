
let listULItem = document.getElementById('list')


window.setTimeout(function(){


  console.log("contents of the function")




},6000)

// setTimeout is called only ONCE
window.setTimeout(doSomething,5000)

function doSomething() {
  console.log('I am called!')
}

window.setTimeout(function() {

  console.log("set timeout called using anonymous function")

},5000)


let counter = 0

// call a function repeatedly after x seconds
let intervalId = window.setInterval(function(){

  let listItem = `<li>Hey!</li>`

  listULItem.innerHTML += listItem
  counter += 1
  console.log(counter)
  if(counter == 5) {
   window.clearInterval(intervalId)
 }
},1000)

// stop the timer
window.clearInterval(intervalId)
