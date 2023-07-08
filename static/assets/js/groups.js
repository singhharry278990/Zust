const socket = new WebSocket('ws://localhost:8000/ws/livec/');
socket.onmessage = (e) => {
    result = JSON.parse(e.data).result;
    document.getElementById("results").value += "Server: " + result + "\n";
}

socket.onclose = (e) => {
    console.log("Socket closed!");
}

document.querySelector('#exp').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#submit ').click();
    }
};

document.querySelector("#submit").onclick = (e) => {
    inputfield = document.querySelector("#exp")
    exp = inputfield.value
    socket.send(JSON.stringify(
        {
            expression: exp
        }
    ))
    document.querySelector("#results").value += "You: " + exp + "\n";
    inputfield.value = "";
}
