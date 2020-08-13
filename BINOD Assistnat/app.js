alert("Upvote If You Like")
confirm("Check out Tutorial Video of How I did it. Link is in the HTML File")

//answers
const greetings = ['Hello Mate', 'How are you doing today?', "What's Up homeboi"]
const health = ["I'm Fine, How are you?", "I'm good, you can ask me BINOD related questions", "I'm good"]
const binod = ["Everyone is Binod, You're Binod, I'm Binod, the whole world is Binod", "Binod is someone who comments his name everywhere."]
const greetings2 = ["Nice Binod", "Okay Binod", "I'll convert your name into Binod"]

//dom
const btn = document.querySelector('.talk')
const content = document.querySelector('.content')
const answer = document.querySelector('.answer')
const defaultBtn = document.querySelector('.default')
const femaleBtn = document.querySelector('.female')

const speech = new SpeechSynthesisUtterance
const speechRecog = window.SpeechRecognition || window.webkitSpeechRecognition
const recognition = new speechRecog


defaultBtn.addEventListener('click', function(e){
    const currentBtn = e.target
    const nextBtn = e.target.nextElementSibling
    nextBtn.classList.remove('active')
    nextBtn.classList.add('inactive')
    currentBtn.classList.remove('inactive')
    currentBtn.classList.add('active')

    speech.voice = speechSynthesis.getVoices().filter(function(voice){
        return voice.name == "Microsoft David Desktop - English (United States)"
    })[0];
})

femaleBtn.addEventListener('click', function(e){
    const currentBtn = e.target
    const prevBtn = e.target.previousElementSibling
    prevBtn.classList.remove('active')
    prevBtn.classList.add('inactive')
    currentBtn.classList.remove('inactive')
    currentBtn.classList.add('active')

    speech.voice = speechSynthesis.getVoices().filter(function(voice){
        return voice.name == "Microsoft Zira Desktop - English (United States)"
    })[0];

})

recognition.onstart = function(){
    console.log("Listening")
}

recognition.onresult = function(e){
    const transcript = e.results[0][0].transcript
    content.textContent = transcript
    readSentences(transcript)
}

btn.addEventListener('mouseenter', function(e){
    e.target.textContent = 'Press to Talk'
    e.target.style.width = '200px'
    e.target.style.boxShadow ='5px 5px 4px 6px #ccc'
})

btn.addEventListener('mouseleave', function (e){
    e.target.textContent = 'Talk'
    e.target.style.width = '150px'
    e.target.style.boxShadow ='3px 3px 4px 6px #ccc'
})

btn.addEventListener('click', function(e){
    recognition.start()
})


function readSentences(message){
    if(!('speechSynthesis' in window)){
        alert("Change your Browser")
    }else{
        const fallback = speech.text = "I don't know what you said?"


        //condition whether the user inpur includes some keyword or not
        if(message.toLowerCase().includes('good') || message.toLowerCase().includes("nice") || message.toLowerCase().includes("great") || message.toLowerCase().includes("fine")){
            const finalText = greetings2[Math.floor(Math.random() * greetings2.length)];
            speech.text = finalText
            answer.textContent = speech.text
        }else if(message.toLowerCase().includes('good morning') || message.toLowerCase().includes('hi') || message.toLowerCase().includes('hello') || message.toLowerCase().includes('good afternoon') || message.toLowerCase().includes('good night') || message.toLowerCase().includes('hai')){
            const finalText = greetings[Math.floor(Math.random() * greetings.length)];
            speech.text = finalText;
            answer.textContent = speech.text
        }else if(message.toLowerCase().includes('how are you') || message.toLowerCase().includes("what's up") || message.toLowerCase().includes("what is up") || message.toLowerCase().includes("are you good")){
            const finalText = health[Math.floor(Math.random() * health.length)];
            speech.text = finalText
            answer.textContent = speech.text
        }else if(message.toLowerCase().includes('binod') || message.toLowerCase().includes("tell me about binod") || message.toLowerCase().includes("vinod")){
            const finalText = binod[Math.floor(Math.random() * binod.length)];
            speech.text = finalText
            answer.textContent = speech.text
        }else if(message.toLowerCase().includes('name') || message.toLowerCase().includes("yourself")){
            const finalText = "My name is Binod, you're also Binod. I'll make whole world into Binod";
            speech.text = finalText
            answer.textContent = speech.text
        }else{
            answer.textContent = fallback
        }

        speech.volume =1
        speech.pitch = 1
        speech.rate = 1
        window.speechSynthesis.speak(speech)
    }
}