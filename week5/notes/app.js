let url = "https://jsonplaceholder.typicode.com/users"
let userList = document.getElementById("")

$.get(url, function(data) {
  $(data).each(function(index, item) {
    $("<li>").html(item.username).appendTo($("#userList"))
  })

})
