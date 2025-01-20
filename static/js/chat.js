
function SendChatbotMessage(message) { //a method used for rendering a new message sent by the AI in the HTML 
    const chatElement = document.getElementById('chat');
    if (chatElement) {
      const htmlCode = `
      <div class="question">
        <div class="img">
            <img src="../static/assets/icon.png" alt="">
        </div>

        <div class="gpt-title">
            ${message}
        </div>
      </div>
      `;
      chatElement.innerHTML += htmlCode.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');
    } else {
      console.error("Chat element with ID 'chat' not found!");
    }
  }
function SendUserMessage(message){ //a method used for rendering a new message sent by the user in the HTML 
    const chatElement = document.getElementById('chat');
    if (chatElement) {
      const htmlCode = `
      <div class="response">
        <div class="gpt-title">
            ${message}
        </div>
        <div class="img">
          <img src="../static/assets/avatar.png" alt=""/>
        </div>
      </div>
      `;
      chatElement.innerHTML += htmlCode.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');;
    } else {
      console.error("Chat element with ID 'chat' not found!");
    }
}


let JSONmessage = 'empty';


function UpdateMessage() { //a method used to send an AJAX request that checks the last message sent by main.py to app.py
  $.ajax({
      type: 'POST',
      data: {},
      url: '/GetLatestMessage',  // Pass data to Python function
      success: function(response) {
          JSONmessage = response;
      },
      error: function(error) {
          console.error('Error 909 calling Python function:', error);
      }
  });
}


let oldJSONValue = '';

setInterval(() => { //executes UpdateMessage() every 500 ms and checks for changes, if the latest message change that means that there's a new message and therefore should by rendered
  UpdateMessage()
  if (JSON.stringify(JSONmessage) != JSON.stringify(oldJSONValue)) {
    if (JSONmessage.role == "user") { //checks the role of sender of the new message, and fires the corresponding method
      SendUserMessage(JSONmessage.message)
    }
    else if(JSONmessage.role == "Chatbot") {
      SendChatbotMessage(JSONmessage.message)
    }
  }
  oldJSONValue = JSONmessage;
}, 500);


setInterval(() => { //sends an AJAX request checking the the person currently speaking, and updates the ui responsively
  const Speaker_ImageObj = document.getElementById("Speaker_Image")
  const mic_backgroundObj = document.getElementById("mic-background")
  $.ajax({
      type: 'POST',
      data: {},
      url: '/GetSpeaker',  // Pass data to Python function
      success: function(response) {
          if (response.speaker == "Athar") {
            console.log("ath")
            Speaker_ImageObj.src = "../static/assets/mic_black.png";
            Speaker_ImageObj.style.backgroundColor = '#3B3B3B';
            mic_backgroundObj.style.backgroundColor = '#3B3B3B';
            mic_backgroundObj.style.scale = 1.0;
          }
          else if(response.speaker == "user") {
            Speaker_ImageObj.src = "../static/assets/mic_white.png";
            Speaker_ImageObj.style.backgroundColor = '#EB5E28';
            mic_backgroundObj.style.backgroundColor = '#EB5E28';
            mic_backgroundObj.style.scale = 1.2;
          }
      },
      error: function(error) {
          console.error('Error 909 calling Python function:', error);
      }
  });
}, 200);
