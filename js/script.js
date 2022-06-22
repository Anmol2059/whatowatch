function pad(number, length) {
  var str = '' + number;
  while(str.length < length) {
    str = '0' + str;
  }
  return str;
}

function getMovie() {
            var movie = pad(Math.floor((Math.random() * 1155529) + 1), 7);
            $("#refresh").text("Generating...").prop("disabled", true);
            $.getJSON("http://www.omdbapi.com/?apikey=75892e41&i=tt"+movie, function(data) {
            var title = data.Title;
            var year = data.Year;
            var rating = data.imdbRating;
            var actors = data.Actors;
            var plot = data.Plot;
            var type = data.Type;
            var genre = data.Genre;
      
            if(genre == "N/A"){
                genre = "";
            }
          
      
            if(type == "episode"){
                getMovie();
            }else if(type == "movie"){
                if(genre == ""){
                    type = "Movie";
                }else{
                    type = "Movie, " + genre ;
                }
            $("#type").text(type);
                
            }else if(type == "series"){
                if(genre == ""){
                    type = "TV Show";
                }else{
                    type = "TV Show, " + genre;
                }
            $("#type").text(type);
                
            }
      
            if(typeof(title) == "undefined"){
                getMovie();
            }else if(title == "#DUPE#"){
                getMovie();
            }else if(title.search("Episode") >= 0){
                getMovie();
            }else{
                $("#title").text(title);
            }
                
            if(rating != "N/A" || typeof(rating) == "undefined"){
                $("#rating").text("Rating: " + rating);
            }else{
                $("#rating").text("Rating not available on IMDB");
            }
                
            if(actors == "N/A" || typeof(actors) == "undefined"){
                $("#actors").text("Actors not available on IMDB");
            }else{
                $("#actors").text("Actors: " + actors);
            }
      
      
            $("#year").text("Year: " + year);
    
    }).always(function() {
        $("#refresh").text("Next").prop("disabled", false);
    });
}

$("#refresh").click(function (){
    getMovie();
});

document.body.onkeyup = function(e){
    if(e.keyCode == 32){
        var movie = pad(Math.floor((Math.random() * 1155529) + 1), 7);
            $("#refresh").text("Generating...").prop("disabled", true);
            $.getJSON("http://www.omdbapi.com/?apikey=75892e41&i=tt"+movie, function(data) {
            var title = data.Title;
            var year = data.Year;
            var rating = data.imdbRating;
            var actors = data.Actors;
            var plot = data.Plot;
            var type = data.Type;
            var genre = data.Genre;
      
            if(genre == "N/A"){
                genre = "";
            }
          
      
            if(type == "episode"){
                getMovie();
            }else if(type == "movie"){
                if(genre == ""){
                    type = "Movie";
                }else{
                    type = "Movie, " + genre ;
                }
            $("#type").text(type);
                
            }else if(type == "series"){
                if(genre == ""){
                    type = "TV Show";
                }else{
                    type = "TV Show, " + genre;
                }
            $("#type").text(type);
                
            }
      
            if(title == "undefined"){
                getMovie();
            }else if(title == "#DUPE#"){
                getMovie();
            }else if(title.search("Episode") >= 0){
                getMovie();
            }else{
                $("#title").text(title);
            }
                
            if(rating != "N/A" || rating == "undefined"){
                $("#rating").text("Rating: " + rating);
            }else{
                $("#rating").text("Rating not available on IMDB");
            }
                
            if(actors == "N/A" || actors == "undefined"){
                $("#actors").text("Actors not available on IMDB");
            }else{
                $("#actors").text("Actors: " + actors);
            }
      
      
            $("#year").text("Year: " + year);
    
    }).always(function() {
        $("#refresh").text("Next").prop("disabled", false);
    });
}
}

