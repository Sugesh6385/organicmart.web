let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function showNextSlide(){

    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlidePosition();
}

function updateSlidePosition() {
    const slidesContainer = document.querySelector('.slides');
    const offset = -currentIndex * 100;
    slidesContainer.style.transform = `translateX(${offset}%)`;
}

setInterval(showNextSlide, 3000); // Change slide every 3 seconds



//selecting popup box popup overlay button
var popupoverlay=document.querySelector(".popup-overlay")
var popupbox  = document.querySelector(".popup-box")
var addpopupbutton= document.getElementById("add-popup-button")

addpopupbutton.addEventListener("click",function(){
    popupoverlay.style.display="block"
    popupbox.style.display="block"
})

 
    
    
    
    
