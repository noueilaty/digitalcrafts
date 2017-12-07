


let titleTextBox = document.getElementById("title")
let addTaskButton = document.getElementById("addTaskButton")

let taskList = document.getElementById("taskList") // ul element

addTaskButton.addEventListener('click',function(){

  // value of the textbox
  let title = titleTextBox.value

  // create the task Item div container
  let taskItemDiv = document.createElement('div')
  taskItemDiv.className = "task-item-div"

  // create li items
  let taskItem = document.createElement('li')
  // set the innerHTML to the value in the textbox
  taskItem.innerHTML = title

  // create a delete button
  let deleteButton = document.createElement('button')
  deleteButton.innerHTML = "Delete"
  // add click event listener to the delete button
  deleteButton.addEventListener('click',function(){

    // this inside the current scope of the button click
    // refers to the button itself
    console.log(this.parentElement)

    // this.parentElement refers to the parent of button which is div
    taskList.removeChild(this.parentElement)

  })

  taskItemDiv.appendChild(taskItem)
  taskItemDiv.appendChild(deleteButton)

  taskList.appendChild(taskItemDiv)

  // add the li to the ul element
  //taskList.appendChild(taskItem)
  // add the button to the list
  //taskList.appendChild(deleteButton)

  console.log(title)

})
