const headerEl = document.querySelector("header");
const myBtn = document.querySelector("#toggle_header");


myBtn.addEventListener("click", () => {
    if (headerEl.classList.contains("green")) {
        headerEl.classList.replace("green", "red");
    } else {
        headerEl.classList.replace("red", "green");
    }
});
