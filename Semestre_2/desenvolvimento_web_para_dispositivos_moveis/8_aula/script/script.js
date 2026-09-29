const abrir = document.querySelector("#abrir");
const bt = document.querySelector(".menu-responsive");
const fechar =document.querySelector(".mask"); 

// atribuir evento de click
bt.addEventListener("click", () => {
    abrir.classList.add("open")
});
// Atribuir evento de fechar ao clicar na class mask
fechar.addEventListener*("click", () => {
    abrir.classList.remove("open");
});

