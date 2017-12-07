for (var i = 0; i < news.articles.length; i++) {
  console.log(news.articles[i].title);

  newsList = document.getElementById('newsList');

  let newsListItem = `
  <div>
    <img src="${news.articles[i].urlToImage}" alt="${news.articles[i].title}">
    <h3><a href="${news.articles[i].url}">${news.articles[i].title}</a><h3>
    <h5>Posted ${news.articles[i].publishedAt} by ${news.articles[i].author}
    <p>${news.articles[i].description}</p>

  </div>`

  newsList.innerHTML += newsListItem;
}
