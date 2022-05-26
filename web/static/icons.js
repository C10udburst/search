function getIcon(icon, promise) {
    fetch(`static/icons/${icon}.svg`)
    .then(r => r.text())
    .then(r => {
        var node = document.createElement("div")
        node.innerHTML = r
        node = node.firstChild
        promise(node)
    })
}