let widgetTemplates =  document.querySelector("#widget-templates").content

function createWidget(from) {
    if (from.type === "field") {
        return createField(from.content)
    }
    else if (from.type === "uri_field") {
        return createUriField(from.content)
    }
    else if (from.type === "dynamic_field") {
        return createDynamicField(from.content)
    }

    return undefined
}

function createDynamicField(content) {
    let node = widgetTemplates.querySelector(".widget.field").cloneNode(true)
    node.querySelector(".key").innerText = content.key
    let valueNode = node.querySelector(".value")
    valueNode.innerHTML = md.render(content.value)
    valueNode.innerHTML = md.render(eval(content.js)())
    if (content.interval > 0) {
        setInterval(() => {
            valueNode.innerHTML = md.render(eval(content.js)())
        }, content.interval)
    }
    return node
}
function createField(content) {
    let node = widgetTemplates.querySelector(".widget.field").cloneNode(true)
    node.querySelector(".key").innerText = content.key
    node.querySelector(".value").innerHTML = md.render(content.value)
    return node
}
function createUriField(content) {
    let node = widgetTemplates.querySelector(".widget.field.uri").cloneNode(true)
    node.querySelector(".key").innerText = content.key
    node.querySelector(".uri").innerText = content.name
    node.querySelector(".uri").href = content.uri
    return node
}