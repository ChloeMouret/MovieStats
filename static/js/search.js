
$(main)

function main(){
    var btn = $("#searchButton");
	btn.click(recupTitle);
}


function recupTitle(){
    var movieName = $("#inputMovie").val();
    sendRequest(movieName);
}


function sendRequest(movie){
    /*var data = $.ajax('/getStats/Inception', function () {
        console.log("Hello world")
    });
    console.log(data);*/
    $.get('/getStats/Inception', function(){console.log("Hello")});
}
