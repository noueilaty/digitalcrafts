// let postURL = "http://dc-coffeerun.herokuapp.com/api/coffeeorders/"


$.get(postURL, function(data) {
  for (const prop in data) {
    $("<ul>")
    .append($("<li>").html(data[prop].emailAddress))
    .append($("<li>").html(data[prop].coffee))
    .append($("<br>").html("<br>"))
    // .append($(`<button id="${data[prop]._id}">Delete</button>`)
    //   .click(function(){}))
    .appendTo($("#existingOrders"))
  }
})


$("#POSTorder").click(function(){
  let emailAddress = $("#emailAddressBox").val()
  let coffee = $("#coffeeBox").val()
  let data = {
    emailAddress: emailAddress,
    coffee: coffee
  }

  $.post(postURL, data, function(response){
  })
})

$("#DELETEorder").click(function(){
  let emailToDelete = $("#deleteEmailAddressBox").val()

  $.ajax({
    url: postURL + emailToDelete,
    type: 'DELETE',
    success: function(result) {
      console.log('Successfully deleted')
    }
  })
})
