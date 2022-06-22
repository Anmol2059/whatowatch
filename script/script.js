function getMovie() {
    let movieNumber = Math.floor(Math.random()*(996-11 + 1)) + 1;
    let response = $.getJSON("https://api.themoviedb.org/3/movie/"+movieNumber+"?api_key=3ceb6abdc82b592c94dffa62d6add9dd", (movie)=>{
        let genres = movie.genres;
        let title = movie.title;
        let releaseDate = movie.release_date;
        let rating = movie.vote_average;
        let overview = movie.overview;
        let imgSrc = "https://image.tmdb.org/t/p/w185" + movie.poster_path;

        let runtime = movie.runtime;
        let popularity = movie.popularity;

        console.log(movie);

        $('#genres').html('Genre: ');
        console.log(genres);
        genres.map((genre, index)=>{
            $('#genres').append(genre.name);
            if (index != genres.length -1)
            $('#genres').append(', ')
        })
       
        
        $('#title').html(title);
        $('#releaseDate').html("Release: " + releaseDate);
        $('#rating').html("Rating: " + rating);


        $('#overview').html(overview);
        $('#poster').html('<img src =' + imgSrc + ' alt="poster">');
    })
}

$("#refresh").click(function (){
    getMovie();
});

document.body.onkeyup = function(e){
    if(e.keyCode == 32){
       getMovie();
}
}

