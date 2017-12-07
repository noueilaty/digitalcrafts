
// get ul element
let dishesList = document.getElementById('dishesList')

// add the button click listener
btnStarters = document.getElementById('btnStarters')

btnStarters.addEventListener('click',function(){
  console.log('btn fired')

  let search = 'Starters'
  filterDishesByCourseName(search)
})

btnEntrees.addEventListener('click',function(){

  filterDishesByCourseName('Entrees')
})

// filter dishes by course name
function filterDishesByCourseName(search) {

  // create a new empty array
  let filteredDishes = []

  for(let index=0; index<dishes.length;index++) {

      if(dishes[index].course == search) {
          filteredDishes.push(dishes[index])
      }
  }

  // display dishes
  displayDishes(filteredDishes)

}

function displayDishes(filteredDishes) {

  // clear the old list
  dishesList.innerHTML = ""

  for(let index = 0; index < filteredDishes.length; index++) {

    let dishListItem = `
    <div>
    <img src="${filteredDishes[index].imageURL}"></img>
    <li>
    ${filteredDishes[index].title}
    </li>
    <p>
    ${filteredDishes[index].description}
    </p>
    </div>`

    dishesList.innerHTML += dishListItem
  }

}

// display all dishes
displayDishes(dishes)
