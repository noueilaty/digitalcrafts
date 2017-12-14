// http://www.omdbapi.com/?i=tt2975590&apikey=46e308e5
// http://www.omdbapi.com/?s=batman&apikey=46e308e5

let url = "http://www.omdbapi.com/?s=batman&apikey=46e308e5";


$.get(url, function(data) {
  $(data.Search).each(function(index, movie) {
    console.log(movie.Title);

    $("<div>")
    .append($("<li>").html(movie.Title + ', ' + movie.Year))
    .append($(`<button id="${movie.imdbID}" onclick="currentTitle(${movie.imdbID})">View</button>`))
    .appendTo($("#movieList"))
  })
})


let currentTitle = function(movieID) {
  let id = $(movieID).attr('id');
  let movieUrl = `http://www.omdbapi.com/?i=${id}&apikey=46e308e5`

  document.getElementById("currentTitle").innerHTML = "";

  $.get(movieUrl, function(data) {
    console.log(data.Title);
    $("<div>")
    .append($("<li>").html(data.Title))
    .append($("<li>").html('Image'))
    .append($("<li>").html(data.Year))
    .append($("<li>").html(data.Rated))
    .append($("<li>").html(data.Released))
    .append($("<li>").html(data.Director))
    .appendTo($("#currentTitle"))
  })
}
