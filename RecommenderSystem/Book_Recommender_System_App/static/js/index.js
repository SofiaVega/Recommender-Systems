var data = JSON.parse(document.getElementById('Recommendation').textContent);
console.log(data);

for (i in data){

    var img = document.createElement('img');
    src = data[i];
    img.src = src;
    img.setAttribute("height", "250");
    img.setAttribute("width", "200");
    img.class = "img-thumbnail";

    document.getElementById("images").appendChild(img);
}