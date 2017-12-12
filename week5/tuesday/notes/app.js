let url = "https://jsonplaceholder.typicode.com/users"

$.get(url, function(data) {
  $(data).each(function(index, user) {

    $("<div>")
    .append($("<li>").html(user.name))
    .append($("<li>").html(user.email))
    .append($("<li>").html(user.username))
    .append($("<li>").html(user.address.street))
    .appendTo($("#userList"))

  })
})
