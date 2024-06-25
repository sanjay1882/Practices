




function mailto() {
    var mail = 'mailto:sanjayraju264@gmail.com';

    window.open(mail);
}

function skills() {
    var section = document.getElementById("skills");
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });}};

function aboutme() {
            var section = document.getElementById("aboutme");
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });}}

function contactme() {
    var section = document.getElementById("msg");
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });}}

      

function msgsent(){
    const t=document.getElementById("msgsent-bar").style.display="inline-flex";


    
}

function msgsentcls(){
    const x_ele =document.getElementById("msgsent-bar").style.display="none";


}





function frontend(){
const ssdrag=document.getElementById("ssdrag").style.display="none";
const techchange=document.getElementById("Techhead");
const onea=document.getElementById("onea");
const twoa=document.getElementById("twoa");
const threea=document.getElementById("threea");
   const foura=document.getElementById("foura");
   const techtable=document.getElementById("techtable");
   techtable.classList.add("techtable");
   
   techchange.classList.add("Techhead");
onea.classList.add("onea");
twoa.classList.add("twoa");
threea.classList.add("threea");
foura.classList.add("foura");
techchange.innerHTML='Frontend';
onea.innerHTML='HTML5';


twoa.innerHTML='CSS';
;

threea.innerHTML='Javascript';

threea.style.width="60%";
foura.innerHTML='Bootstrap';

foura.style.width="70%";

        }
        
function backend(){
  
    const techchange=document.getElementById("Techhead");
    const techtable=document.getElementById("techtable");
    const twoa=document.getElementById("twoa");
    const ssdrag=document.getElementById("ssdrag").style.display="none";
    const threea=document.getElementById("threea");
       const foura=document.getElementById("foura");
    techtable.classList.add("techtable");
    techchange.classList.add("Techhead");


       onea.classList.add("onea");
       twoa.classList.add("twoa");
       threea.classList.add("threea");
       foura.classList.add("foura");
    
    techchange.innerHTML='Backend';

    onea.innerHTML='PHP';
    onea.style.width="50%";
    twoa.innerHTML='Flask';
   twoa.style.width="20%";

    threea.innerHTML='Firebase';
    threea.style.width="80%";
    foura.innerHTML='Django';
    foura.style.width="60%";
            }
            
function softskills(){
    const techchange=document.getElementById("Techhead");
    const onea=document.getElementById("onea");
    const twoa=document.getElementById("twoa");
const threea=document.getElementById("threea");
const foura=document.getElementById("foura");
const techtable=document.getElementById("techtable");
const ssdrag=document.getElementById("ssdrag").style.display="none";
techtable.classList.add("techtable");
techchange.classList.add("Techhead");
onea.classList.add("onea");
twoa.classList.add("twoa");
threea.classList.add("threea");
foura.classList.add("foura");
    techchange.innerHTML='Soft Skills';
    onea.innerHTML='Python'
     onea.style.width="80%";
    twoa.innerHTML='C-Basics';
  twoa.style.width="60%";
    threea.innerHTML='java';
    threea.style.width="50%";
    foura.innerHTML='C++';
    foura.style.width="70%";

            }
            
function tools(){
    const techchange=document.getElementById("Techhead");
    const onea=document.getElementById("onea");
    const twoa=document.getElementById("twoa");
const threea=document.getElementById("threea");
const foura=document.getElementById("foura");
const ssdrag=document.getElementById("ssdrag").style.display="none";
const techtable=document.getElementById("techtable");
techtable.classList.add("techtable");
techchange.classList.add("Techhead");
onea.classList.add("onea");
twoa.classList.add("twoa");
threea.classList.add("threea");
foura.classList.add("foura");
    techchange.innerHTML='Tools';
    onea.innerHTML='GPT-4';
    onea.style.width="85%";
    twoa.innerHTML='Palm-2';
    twoa.style.width="80%";
    threea.innerHTML='Copilot';
    threea.style.width="40%";
    foura.innerHTML='Excel';
    foura.style.width="50%";
}
