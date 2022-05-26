var results = []
let container = document.querySelector("#main-container")
let cardTemplate = document.querySelector("#card-template").content
let md = new markdownit({
    breaks: true,
    linkify: true,
    typographer: true,
    html: true
})
function search(query) {
    if (tryRedirect(query)) {
        return
    }
    let ssl = window.location.protocol==="https:"
    let addr = `ws${ssl?'s':''}://${window.location.hostname}${window.location.pathname}ws/`
    var sock = new WebSocket(addr)
    sock.onmessage = (event) => {
        let data = JSON.parse(event.data)
        fastAdd(data)
        results.push(data)
    }
    sock.onopen = (event) => {
        results = []
        container.innerHTML = ""
        sock.send(query)
    }
    sock.onclose = () => {
        setTimeout(finalAdd, 100)
    }
}

function createCardNode(data,) {
    let node = cardTemplate.cloneNode(true)
    node.querySelector(".title > a").innerText = data.title
    node.querySelector(".summary").innerHTML = md.render(data.summary)
	let card = node.querySelector(".card")
    card.style=`--color: ${data.color};`
    let anchor = node.querySelector(".main-url")
    if (data.uri !== undefined) {
        anchor.href = data.uri
    } else {
        node.querySelector(".title .icon").remove()
        anchor.outerHTML = anchor.outerHTML.replace(/^\<a /gi,"<span ")
    }
    if (data.image !== undefined) {
        node.querySelector(".img-container img").src = data.image
        node.querySelector(".img-container a").href = data.image
    }
    if (data.footer !== undefined) {
        node.querySelector(".footer").innerHTML = md.render(data.footer)
    } else {
        node.querySelector(".footer").remove()
    }
    let widgetsContainer = node.querySelector(".widgets")
    data.widgets.forEach((widget) => {
        let widgetNode = createWidget(widget.widget)
        if (widgetNode !== undefined) {
            widgetsContainer.appendChild(widgetNode)
        }
    })
    return node
}

function fastAdd(data) {
    container.appendChild(createCardNode(data,))
}

function compare(a, b) {
    return b.weight - a.weight
}

function finalAdd() {
    results = results.sort(compare)
    container.innerHTML = ""
    results.forEach((result) => {
        container.appendChild(createCardNode(result))
    })
}

document.querySelector(".search form").addEventListener("submit", (evt) => {
    evt.preventDefault()
    let query = document.querySelector("#query").value
    search(query)
})
