from .main import GoogleModule
from .cse import GoogleCSEModule

google_modules = {
    GoogleModule(),

    GoogleCSEModule("Bins", ["012b157605b71f278", "0b2238d1d092b0261", "6f5c8e8896c9325dd", "02a9e816e74720d9c", "012b157605b71f278"], [
        "bin",
        "bins",
        "paste",
        "pastes",
        "pastebin",
        "gist",
        "txt",
        "text",
        "texts"
    ], summary="Return gists."),
    GoogleCSEModule("Ebooks", ["003753031376654422446:szjag5vbefo", "006516753008110874046:s9ddesylrm8", "e9657e69c76480cb8", "c46414ccb6a943e39"], [
        "books",
        "ebooks",
        "book",
        "ebook",
        "pdf",
        "reading"
    ], summary="Search for ebooks using `r/Piracy` cse."),
    GoogleCSEModule("Games", ["8057daa3730322939", "b330325055a60da29"], [
        "games",
        "crack",
        "game",
        "cracks",
        "videogames",
        "steam"
    ], summary="Search for game cracks."),
    GoogleCSEModule("Google Drive", "22dda532c1a0e20cf", [
        "drive",
        "files",
        "file",
        "download"
    ], summary="Search for files in google drive"),
    GoogleCSEModule("Roms", "017627112597466747210:d_mvqq9pgve", [
        "roms",
        "emulation",
        "consoles",
        "nintendo",
        "games"
    ], summary="Search for console roms."),
    GoogleCSEModule("Files", ["006516753008110874046:1ugcdt3vo7z", "006516753008110874046:reodoskmj7h"], [
        "files",
        "file",
        "dl",
        "download"
    ], summary="Search for files"),
    GoogleCSEModule("Streaming", ["006516753008110874046:cfdhwy9o57g", "006516753008110874046:o0mf6t-ugea", "98916addbaef8b4b6", "0199ade0b25835f2e"], [
        "streaming",
        "movies",
        "series",
        "tv"
    ], summary="Search for movie or tv series streaming"),
}
