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
  // console.log('View Button Clicked')
  console.log($(movieID).attr('id'));
}
