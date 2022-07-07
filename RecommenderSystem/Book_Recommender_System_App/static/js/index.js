var data = JSON.parse(document.getElementById('Recommendation').textContent);
var first = JSON.parse(document.getElementById('First').textContent);
console.log(data);

if (data.length == 0 && first == "false"){
    const errorMessage = document.createTextNode("El libro no existe en la base de datos");
    document.getElementById("images").appendChild(errorMessage);
}else{
    for (i in data){

        var img = document.createElement('img');
        src = data[i];
        img.src = src;
        img.setAttribute("height", "250");
        img.setAttribute("width", "200");
        img.class = "img-thumbnail";
    
        document.getElementById("images").appendChild(img);
    }

}