function connect() {
    ws = new WebSocket("ws://localhost:5000/echo")

    ws.onopen = function (event) {

        document.getElementById('input').onchange = function (ev) {
            var timestamp = new Date().valueOf();
            var message = { text: ev.target.value, timestamp }
            ws.send(JSON.stringify(message))
            ev.target.value = ""
        }

        document.getElementById('input').removeAttribute('disabled')
        document.getElementById('output').removeAttribute('disabled')
        document.getElementById('status').innerText = 'Connected'
    }

    ws.onmessage = function (event) {
        var timestamp = new Date().valueOf()
        console.log(event.data)
        var data = JSON.parse(event.data)
        document.getElementById('output').textContent += `from server: ${data.text} (${timestamp - data.timestamp}ms) \n`
    }

    ws.onclose = function (ev) {
        document.getElementById('input').setAttribute('disabled', '')
        document.getElementById('output').setAttribute('disabled', '')
        document.getElementById('status').innerText = 'Not Connected'
    }
}

document.getElementById('input').focus()