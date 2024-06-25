
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
  import { getDatabase,ref,set,get,child } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";




  const firebaseConfig = {
    apiKey: "AIzaSyB0DgfNT3C1lWlYmS3j_mLWxCkd95F7phs",
    authDomain: "resume-e6312.firebaseapp.com",
    projectId: "resume-e6312",
    storageBucket: "resume-e6312.appspot.com",
    messagingSenderId: "838668514093",
    appId: "1:838668514093:web:7f0129d226ce0ad77e59a4",
    measurementId: "G-CH9VXZQ61X"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);


  const db = getDatabase(app);


  document.getElementById("submit").addEventListener("click",function(e){

    e.preventDefualt();
set(ref(db,'user/'+ document.getElementById('fname').value),
{
    fname: document.getElementById('fname').value,
    lname: document.getElementById('lname').value,
    mobile: document.getElementById('mobile').value,
   email: document.getElementById('mail').value,
    message: document.getElementById('message').value
}
);
alert("Thankyou");


  });






  const analytics = getAnalytics(app);
