function update_function(value, id){

    let url = "http://127.0.0.1:5000/update/"+id+"/"+value;
    let responseText = HttpRequest(url);
    console.log(id)
    document.getElementById(id+"-box").innerHTML = responseText;
}

function HttpRequest(url){
    request = new XMLHttpRequest();
    request.open("GET",url,false)
    request.send(null)
    return request.responseText
}