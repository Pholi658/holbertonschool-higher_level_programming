const headerEl = document.querySelector("header");
const myBtn = document.querySelector("#red_header");

myBtn.addEventListener("click",function(){
    headerEl.classList.add("red");
});
