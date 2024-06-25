


const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span ");
const chatbox = document.querySelector(".chatbox ");
const chatbtn = document.querySelector(".bx-send");
let userMessage;






function handleKeyPress(event) {
  if (event.keyCode === 13) {
    // 13 is the key code for Enter
    var chatInput = document.getElementById("inputa").value.trim();
    if (chatInput !== "") {
      handlechat();
    }
  }
}





const createChatli = (message, className) => {
  const chatLi = document.createElement("li");
  chatLi.classList.add("chat", className);
  const messageID =Math.random()*100;
  let chatContent = className === "outgoing" ? `<p>${message}</p>` : `<span class="material-symbols-outlined">T</span><p id="${messageID}">${message}</p><i class="bx bx-copy" id="${messageID}" title="Copy" onclick="copyText(${messageID})"></i><i class="bx bx-dots-vertical-rounded"></i>`;
  
  chatLi.innerHTML = chatContent;
  return chatLi;
}

const generateResponse =() =>{
   /*
 * Install the Generative AI SDK
 *
 * $ npm install @google/generative-ai
 *
 * See the getting started guide for more information
 * https://ai.google.dev/gemini-api/docs/get-started/node
 */

const {
  GoogleGenerativeAI,
  HarmCategory,
  HarmBlockThreshold,
} = require("@google/generative-ai");
const GEMINI_API_KEY ="AIzaSyCrbbKwCxr-I3EPIEDiegoaXokpbCFDBh4";

const apiKey = process.env.GEMINI_API_KEY;
const genAI = new GoogleGenerativeAI(apiKey);

const model = genAI.getGenerativeModel({
  model: "gemini-1.5-flash",
});

const generationConfig = {
  temperature: 1,
  topP: 0.95,
  topK: 64,
  maxOutputTokens: 8192,
  responseMimeType: "text/plain",
};

async function run() {
  const chatSession = model.startChat({
    generationConfig,
 // safetySettings: Adjust safety settings
 // See https://ai.google.dev/gemini-api/docs/safety-settings
    history: [
      {
        role: "user",
        parts: [
          {text: "hello"},
        ],
      },
      {
        role: "model",
        parts: [
          {text: "Hello! How can I help you today? \n"},
        ],
      },
    ],
  });

  const result = await chatSession.sendMessage(userMessage);
  console.log(result.response.text());
}

run();
}

const handlechat = () => {


  userMessage = chatInput.value.trim();

  createChatli(userMessage, "outgoing");
  chatbox.appendChild(createChatli(userMessage, "outgoing"));
  userMessage = chatInput.value.trim();

  chatbox.scrollTo(0, chatbox.scrollHeight);
setTimeout(() =>{
  chatbox.appendChild(createChatli("Hey there I am chatbot . I can assist you. I will notify once i can make conversation with you. stay tuned ._.", "incoming"));
},300);

  
  }
  if (userMessage == "who is sanjay") {

    let out = " Sanjay is creater.His journey into the world of programming and technology began at VSB Engineering College in Karur, where I pursued his education.During his college years, I discovered his love for coding and delved into various aspects of software development.I found joy in creating mobile games, exploring the intersection of creativity and technology. his hobby of creating and playing mobile games not only provided entertainment but also sparked his curiosity about the underlying software that powers these experiences. With a solid foundation in computer science from College, I am driven by the ambition to become a proficient software developer.";

    chatbox.appendChild(createChatli(out, "incoming"));

  }



  else if (userMessage == "whats up") {

    let out = "This is Teego , I can assist you!. Would you like to ask some questions ? ";
    chatbox.appendChild(createChatli(out, "incoming"));

  }
  else {
    let out = "Hey there I am chatbot . I can assist you. I will notify once i can make conversation with you. stay tuned ._.";
    chatbox.appendChild(createChatli(out, "incoming"));

  }




function copyText(paraId) {
  // Get the text from the paragraph with the given id

  var text = document.getElementById(paraId).innerText;

  // Create a temporary textarea element to hold the text
  var tempTextArea = document.createElement("textarea");
  tempTextArea.value = text;
  document.body.appendChild(tempTextArea);

  // Select the text in the textarea
  tempTextArea.select();
  tempTextArea.setSelectionRange(0, 99999); // For mobile devices

  // Copy the text to the clipboard
  document.execCommand("copy");

  // Remove the temporary textarea element
  document.body.removeChild(tempTextArea);
  
 

}




if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
  const startSound = document.getElementById('startSound');
  const stopSound = document.getElementById('stopSound');
  // Create speech recognition object
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();

  // Define what should happen when speech is recognized
  recognition.onresult = function(event) {
      const transcript = event.results[0][0].transcript;
      document.getElementById('inputa').value = transcript;;
  }

  // Define what should happen when speech recognition is started
  recognition.onstart = function() {
      console.log('Speech recognition started');

      startSound.play(); 
  }

  // Define what should happen when speech recognition is ended
  recognition.onend = function() {
      console.log('Speech recognition ended');

        stopSound.play();
  }

  // Define what should happen when there is an error with speech recognition
  recognition.onerror = function(event) {
      console.error('Speech recognition error occurred:', event.error);
  }

  // Add event listener to start button
  document.getElementById('start-btn').addEventListener('click', function() {
      recognition.start();
  });

} else {
  // Browser doesn't support Web Speech API
  console.error('Browser does not support speech recognition');
  alert(" This Browser does not support speech recognition ");
}
sendChatBtn.addEventListener("click", handlechat);



















