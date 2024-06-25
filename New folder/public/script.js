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

window.addEventListener('scroll',() =>{
    let value = window.scrollY;
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

// Define function to start automatic image slider
const autoSlide = () => {
  // Start the slideshow by calling slideImage() every 2 seconds
  intervalId = setInterval(() => slideImage(imageIndex++), 2000);
};
// Call autoSlide function on page load
autoSlide();

// A function that updates the carousel display to show the specified image
const slideImage = () => {
  // Calculate the updated image index
  imageIndex = imageIndex === images.length ? 0 : imageIndex < 0 ? images.length - 1 : imageIndex;
  // Update the carousel display to show the specified image
  carousel.style.transform = `translate(-${imageIndex * 100}%)`;
};

// A function that updates the carousel display to show the next or previous image
const updateClick = (e) => {
  // Stop the automatic slideshow
  clearInterval(intervalId);
  // Calculate the updated image index based on the button clicked
  imageIndex += e.target.id === "next" ? 1 : -1;
  slideImage(imageIndex);
  // Restart the automatic slideshow
  autoSlide();
};

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
 // Function to handle scroll event
function handleScroll() {
  // Get all elements with the class "animated-text"
  const animatedElements = document.querySelectorAll('.aboutme-p');
  
  // Loop through each element
  animatedElements.forEach(element => {
      // Calculate the distance of the element from the top of the viewport
      const elementTop = element.getBoundingClientRect().top;
      
      // Calculate when the element should start sliding in (adjust this value as needed)
      const triggerPoint = window.innerHeight - 100;
      
      // If the element is in the viewport, add the "slide-in" class
      if (elementTop < triggerPoint) {
          element.classList.add('slide-in');
      } else {
          // If the element is not in the viewport, remove the "slide-in" class
          element.classList.remove('slide-in');
      }
  });
}

// Add scroll event listener
window.addEventListener('scroll', handleScroll);

// Initial check on page load
handleScroll();
