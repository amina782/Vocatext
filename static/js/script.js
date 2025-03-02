// Create Floating Bubbles
for (let i = 0; i < 30; i++) {
    let bubble = document.createElement('div');
    bubble.className = 'bubble';
    document.body.appendChild(bubble);
    
    let size = Math.random() * 15 + 10; 
    let position = Math.random() * 100; 
    let duration = Math.random() * 5 + 7; 
    let delay = Math.random() * 5; 

    bubble.style.width = size + 'px';
    bubble.style.height = size + 'px';
    bubble.style.left = position + 'vw';
    bubble.style.animationDuration = duration + 's';
    bubble.style.animationDelay = delay + 's';
}

// Speech Function
function speakAndNavigate() {
    let text = "Welcome to our futuristic text-to-speech engine! Let's begin.";
    let speech = new SpeechSynthesisUtterance(text);
    let synth = window.speechSynthesis;

    let voices = synth.getVoices();
    speech.voice = voices.find(voice => voice.lang.includes("en")) || voices[0];

    synth.speak(speech);
    startAudioVisualizer();

    speech.onend = () => {
        stopAudioVisualizer();
        setTimeout(() => {
            window.location.href = "/home"; 
        }, 500);
    };
}

// Start Audio Visualizer
function startAudioVisualizer() {
    document.querySelectorAll('.bar').forEach(bar => {
        bar.style.animation = "soundWave 1.5s infinite ease-in-out alternate";
    });
}

// Stop Audio Visualizer
function stopAudioVisualizer() {
    document.querySelectorAll('.bar').forEach(bar => {
        bar.style.animation = "none";
    });
}
