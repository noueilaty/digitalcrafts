
// ES5 class syntax
function Customer() {
  this.firstName = ''
  this.lastName = ''

  this.greet = function() {
    console.log("hello greetings")
  }
}

// ES6 class syntax
class Car {

  constructor(make,model) {
    this.make = make
    this.model = model
  }

  drive() {
    console.log("car is driving")
  }

}

let car = new Car('Honda','Accord')
car.drive()
console.log(car.make)


// create a collection of cars
// running a for loop and then creating a list of cars

let cars = []

for(let index = 1; index<=10; index++) {

    let car = new Car("make" + index, "model" + index)
    console.log(car)

    cars.push(car)
}

console.log(cars)

// get the car list ul
let carList = document.getElementById('carList')

// populating the carListr (ul) with items of the cars array
for(let index = 0; index<cars.length;index++) {

    // get the car at current index
    let car = cars[index]
    let liItem = `<li>${car.make}, ${cars.model}</li>`
    carList.innerHTML += liItem
}

// Python
// customer = Customer()

// create an object of Customer class
let customer = new Customer()
customer.greet()



let titleTextBox = document.getElementById('titleTextBox')
let taskList = document.getElementById('taskList')
let addTaskButton = document.getElementById('addTaskButton')

// arrow syntax in ES6 which is equal to anonymous function
addTaskButton.addEventListener('click',() => {

})


addTaskButton.addEventListener('click',function() {

  // get the title out of the textbox
  let title = titleTextBox.value // wash the car

  // ES6 Syntax
  let item = `<div class="divTaskItem"><li>${title}</li><button onclick="deleteItem(this)">Delete</button></div>`
  taskList.innerHTML += item

})

function deleteItem(btn) {
  taskList.removeChild(btn.parentElement)
}
