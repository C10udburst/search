let redirects = [
    [/^\!g([o]{0,4}gle?)?\s/g, "https://google.com/search?q=%s"],
    [/^\!((dd?g{0,2}\s)|((duck){1,2}(go)?))/g, "https://duckduckgo.com/?q=%s"],
    [/^r\//, "http://reddit.com/r/%s"]
]

function tryRedirect(query) {
    for (let redirect of redirects) {
        let regex = redirect[0]
        let uri = redirect[1]
        if (regex.test(query)) {
            q = query.replace(regex, "")
            q = encodeURIComponent(q)
            q = uri.replace(/%s/g, q)
            window.location = q
            return true
        }
    }
    if (query.startsWith("//")) {
        window.location = query.substring(1)
        return true
    }
    return false
}
