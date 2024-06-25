let text = document.getElementById('texta');
const textchange= document.querySelector(".sec-text");



let leaf = document.getElementById('pizzaimg');
    
let textload=() =>{
    setTimeout(()=>
    {
        textchange.textContent="Free delevering"
    },0);
    setTimeout(()=>
    {
        textchange.textContent="20%off"
    },4000);
    setTimeout(()=>
    {
        textchange.textContent="20min"
    },8000);
   
}
textload()
setInterval(textload,12000)

window.addEventListener('scroll',() =>{
    let value = window.scrollY;
    leaf.style.bottom = value * 1.5 +'px';


   let out =text.style.marginTop = value * 1.5 +'px';

})


function orderFood(foodItem) {
    document.getElementById('food').value = foodItem;
    document.getElementById('menu').style.display = 'none';
    document.getElementById('order-form').style.display = 'block';
}

function submitOrder(event) {
    event.preventDefault();
    
    const food = document.getElementById('food').value;
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;

    alert(`Thank you, ${name}! Your order for ${food} will be delivered to ${address}.`);

    // You can add code here to submit the order to a backend server

    // Reset form and show the menu again
    document.getElementById('order-form').reset();
    document.getElementById('order-form').style.display = 'none';
    document.getElementById('menu').style.display = 'block';
}




function exploreList(){
    const buutoncontainer = document.getElementById('explorelist');
    const list = document.getElementById('listmore');
    const exploreless = document.getElementById('exploreless');
    list.style.display="inline-flex";
  exploreless.style.display="block";
    buutoncontainer.style.display="none";
}
function exploreless(){
    const buutoncontainer = document.getElementById('explorelist');
    const list = document.getElementById('listmore');
    const exploreless = document.getElementById('exploreless');
    list.style.display="none";
  exploreless.style.display="none";
    buutoncontainer.style.display="block";
}