// fetching title from all movies using URL

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('UL#list_movies').append(`<li>film.title</li>`);
  }
});
