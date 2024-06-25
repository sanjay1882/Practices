const firebaseConfig = {
    apiKey: "AIzaSyBDoFWeOuajcinwG9YDKkVnFTU6voDMXvA",
    authDomain: "innovativegoals-1ddf3.firebaseapp.com",
    databaseURL: "https://innovativegoals-1ddf3-default-rtdb.firebaseio.com",
    projectId: "innovativegoals-1ddf3",
    storageBucket: "innovativegoals-1ddf3.appspot.com",
    messagingSenderId: "544150628076",
    appId: "1:544150628076:web:3fb7d73ccb2dc30045e7c9",
    measurementId: "G-N02CNFJX9Y"
  };
  firebase.initializeApp(firebaseConfig);
  const contactFormdb=firebase.database().ref("contactForm");
  document.getElementById('contactForm').addEventListener("submit",submitForm);
  function submitForm(e){
    e.preventDefault();
    var fname =getElementvalue('fname');
    var lname =getElementvalue('lname');
    var mobile =getElementvalue('mobile');
    var mail =getElementvalue('mail');
    var message =getElementvalue('message');
SaveDatabase(fname,lname,mobile,mail,message);
  }
  const getElementvalue =(id) =>{
    return document.getElementById(id).value;
  }
  const SaveDatabase=(fname,lname,mobile,mail,message) =>{
   var newcontactform =contactFormdb.push();
   newcontactform.set({
    firstName:fname,
lastName:lname,
Mobile:mobile,
Mail:mail,
Message:message,
   });
  };
