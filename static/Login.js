const input = document.querySelectorAll(".js--input");
const submit = document.querySelector(".js--submit");
var state = [false, false];

//When the page reloads, set the fields as invalid
window.onload = function(){
    input[0].style.borderBottom = "solid tomato 1.5px";
    input[1].style.borderBottom = "solid tomato 1.5px";
}

//Verifies if the email field is valid
input[0].onkeyup = function(){
    if(input[0].value.length == 0 || input[0].value.trim().length == 0){
        submit.style.backgroundImage = "linear-gradient(135deg, #000000, #E3E3E3)"
        input[0].style.borderBottom = "solid tomato 1.5px";
        submit.disabled = true;
        state[0] = false
    } else {
        input[0].style.borderBottom = "solid #2D3047 1.5px";
        state[0] = true
    }
}

//Verifies if the password field is valid
input[1].onkeyup = function(){
    if(input[1].value.length == 0 || input[1].value.trim().length == 0){
        submit.style.backgroundImage = "linear-gradient(135deg, #000000, #E3E3E3)"
        input[1].style.borderBottom = "solid tomato 1.5px";
        submit.disabled = true;
        state[1] = false
    } else if(input[1].value.length < 6 || input[1].value.trim().length < 3){
        submit.style.backgroundImage = "linear-gradient(135deg, #000000, #E3E3E3)"
        input[1].style.borderBottom = "solid goldenrod 1.5px";
        submit.disabled = true;
        state[1] = false
    } else {
        input[1].style.borderBottom = "solid #2D3047 1.5px";
        state[1] = true
    }
}

//Verifies if all fields are valid to enable the submit button
setInterval(function() {
    if(state[0] == true && state[1] == true){
        submit.style.backgroundImage = "linear-gradient(135deg, #2D3047, #93B7BE)"
        submit.disabled = false;
    }
});