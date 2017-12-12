// Notes from class:
// <@BKchannel|@channel> Search for $.get jQuery on Google and you will get documentation on how to use $.get function. The code is also attached.

let url = 'https://jsonplaceholder.typicode.com/photos'
let photoList = document.getElementById("photoList")
$.get(url,function(data){
  // using plain vanilla JS with ES6 syntax
  /*
  for(let index =0; index<data.length;index++) {
    let li = `<li>${data[index].title}</li>`
    photoList.innerHTML += li
  }*/
  // jQuery
  $(data).each(function(index ,item){
    $("<li>").html(item.title).appendTo($("#photoList"))
  })
})
