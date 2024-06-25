let text = document.getElementById('texta');
const textchange= document.querySelector(".sec-text");



let leaf = document.getElementById('ballon');
    
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});


let textload=() =>{
    setTimeout(()=>
    {
        textchange.textContent="Student"
    },0);
    setTimeout(()=>
    {
        textchange.textContent="WebDeveloper"
    },4000);
    setTimeout(()=>
    {
        textchange.textContent="Creater"
    },8000);
   
}
textload();
setInterval(textload,12000)
const menu_side= document.querySelector(".menuside");
const menu_open= document.querySelector(".bx-menu");
const menu_cls=document.querySelector(".bx-x");

window.addEventListener('scroll',() =>{
    let value = window.scrollY;
    menu_side.style.display="none";
    menu_open.style.display="block";
    menu_cls.style.display="none";

    leaf.style.bottom = value * 1.5 +'px';


   let out =text.style.marginTop = value * 1.5 +'px';
   

});
function contactme() {
  var section = document.getElementById("c-me");
  if (section) {
      section.scrollIntoView({ behavior: 'smooth' });}}

      function aboutme() {
        var section = document.getElementById("aboutme");
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });}}

// Get the DOM elements for the image carousel
const wrapper = document.querySelector(".wrapper"),
  carousel = document.querySelector(".carousel"),
  images = document.querySelectorAll("img"),
  buttons = document.querySelectorAll(".button");

let imageIndex = 1,
  intervalId;


// Add event listeners to the navigation buttons
buttons.forEach((button) => button.addEventListener("click", updateClick));

// Add mouseover event listener to wrapper element to stop auto sliding
wrapper.addEventListener("mouseover", () => clearInterval(intervalId));
// Add mouseleave event listener to wrapper element to start auto sliding again
wrapper.addEventListener("mouseleave", autoSlide);



 function menuopen(){
  const menu_open= document.querySelector(".bx-menu");
  const menu_cls=document.querySelector(".bx-x");
  const menu_side= document.querySelector(".menuside");
  menu_side.style.display="block";
  menu_side.style.marginLeft="0px";
  menu_open.style.display="none";
  menu_cls.style.display="block";
 
 }
;



 function menucls(){

  const menu_open= document.querySelector(".bx-menu");
  const menu_cls=document.querySelector(".bx-x");
  const menu_side= document.querySelector(".menuside");
 
  menu_side.style.marginLeft="405px";
  menu_side.style.display="none";
  menu_open.style.display="block";
  menu_cls.style.display="none";
  
 };





 