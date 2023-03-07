var slider = document.getElementById("myRange");
var output = document.getElementById("demo");

function cat (this){
  if (this.value == 1){
  	output.innerHTML = "Samaa mieltä";
    }
  if (this.value == 2){
    output.innerHTML = "Jokseenkin samaa mieltä";
  }
  if (this.value == 3){
    output.innerHTML = "Ei samaa eikä eri mieltä";
  }
  if (this.value == 4){
    output.innerHTML = "Jokseenkin eri mieltä"
  }
  if (this.value == 5){
    output.innerHTML = "Eri mieltä"
  }
}