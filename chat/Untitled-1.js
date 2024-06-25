



const { GoogleGenerativeAI } = require("@google/generative-ai");

// Access your API key as an environment variable (see "Set up your API key" above)
 const API_KEY="AIzaSyAVw-WzTnb5eQRgsrgUdQwFWVXTgs9u9yc";
const genAI = new GoogleGenerativeAI(API_KEY);

async function run() {
 
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});

  const prompt = "Write a story about a magic backpack."

  const result =  model.generateContent(prompt);
  const response =  result.response;
  const text = response.text();
  console.log(text);
}