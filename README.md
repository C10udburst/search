# Search

Fast, asynchronous and modular search system.

<details>
<summary>Websockets interface preview</summary>

<img src=".github/web_preview.png">

</details>

## Interface options
- `term`: Mainly for debugging
- `websocket`: Search through a web browser, using ui provided in [web](./web/) directory
- `discord`: Search using discord bot slash commands

## Installation (websockets)
1. Install requirements (`discord-py-slash-command` is not needed)
2. Create `config.ini` similar to [this one](/config.example.ini) (you can skip the `[discord]` section)
3. Copy files from [web](./web/) for example to `/var/www/search`
4. Create a nginx config similar to [this one](/nginx.example.conf)
5. Create a service or chron job that executes `python3 main.py websocket`

## Installation (discord)
1. Install requirements (`websockets` is not needed)
2. Create `config.ini` similar to [this one](/config.example.ini) (you can skip the `[websocket]` section)
3. Create a service or chron job that executes `python3 main.py discord`

## Avaliable search modules
<!--modules-->
- **Apps**:
	- Search for Android apps.
	- Keywords: ` mobile `, ` apps `, ` android `, ` apk `
- **Base64 Decode**:
	- Decode ASCII string using the standard Base64 alphabet.
- **Base64 Encode**:
	- Encode ASCII string using the standard Base64 alphabet.
	- Keywords: ` b64encode `, ` base64 `, ` b64 `
- **Bins**:
	- Return gists.
	- Keywords: ` texts `, ` text `, ` bin `, ` pastebin `, ` gist `, ` bins `, ` txt `, ` paste `, ` pastes `
- **Duck answers**:
	- Retrieve instant answers from duck duck go.
- **Ebooks**:
	- Search for ebooks using `r/Piracy` cse.
	- Keywords: ` pdf `, ` ebook `, ` ebooks `, ` book `, ` books `, ` reading `
- **Email**:
	- Display info about an email.
- **Ethereum**:
	- Display info about an ethereum address.
- **Files**:
	- Search for files
	- Keywords: ` file `, ` dl `, ` download `, ` files `
- **Games**:
	- Search for game cracks.
	- Keywords: ` game `, ` videogames `, ` steam `, ` games `, ` cracks `, ` crack `
- **Google**:
	- Searches using Google.
- **Google Drive**:
	- Search for files in google drive
	- Keywords: ` drive `, ` download `, ` file `, ` files `
- **Hash BLAKE2B**:
	- Hashes given string using `blake2b`.
	- Keywords: ` hashing `, ` blake2b `, ` hash `
- **Hash BLAKE2S**:
	- Hashes given string using `blake2s`.
	- Keywords: ` hashing `, ` hash `, ` blake2s `
- **Hash MD4**:
	- Hashes given string using `md4`.
	- Keywords: ` hashing `, ` md4 `, ` hash `
- **Hash MD5**:
	- Hashes given string using `md5`.
	- Keywords: ` hashing `, ` hash `, ` md5 `
- **Hash MD5-SHA1**:
	- Hashes given string using `md5-sha1`.
	- Keywords: ` hashing `, ` md5-sha1 `, ` hash `
- **Hash MDC2**:
	- Hashes given string using `mdc2`.
	- Keywords: ` mdc2 `, ` hashing `, ` hash `
- **Hash RIPEMD160**:
	- Hashes given string using `ripemd160`.
	- Keywords: ` hashing `, ` ripemd160 `, ` hash `
- **Hash SHA1**:
	- Hashes given string using `sha1`.
	- Keywords: ` hashing `, ` sha1 `, ` hash `
- **Hash SHA224**:
	- Hashes given string using `sha224`.
	- Keywords: ` sha224 `, ` hashing `, ` hash `
- **Hash SHA256**:
	- Hashes given string using `sha256`.
	- Keywords: ` hashing `, ` sha256 `, ` hash `
- **Hash SHA384**:
	- Hashes given string using `sha384`.
	- Keywords: ` hashing `, ` sha384 `, ` hash `
- **Hash SHA3_224**:
	- Hashes given string using `sha3_224`.
	- Keywords: ` hashing `, ` sha3_224 `, ` sha3224 `, ` hash `
- **Hash SHA3_256**:
	- Hashes given string using `sha3_256`.
	- Keywords: ` sha3_256 `, ` hashing `, ` sha3256 `, ` hash `
- **Hash SHA3_384**:
	- Hashes given string using `sha3_384`.
	- Keywords: ` sha3_384 `, ` hashing `, ` sha3384 `, ` hash `
- **Hash SHA3_512**:
	- Hashes given string using `sha3_512`.
	- Keywords: ` hashing `, ` sha3512 `, ` sha3_512 `, ` hash `
- **Hash SHA512**:
	- Hashes given string using `sha512`.
	- Keywords: ` hashing `, ` sha512 `, ` hash `
- **Hash SHA512_224**:
	- Hashes given string using `sha512_224`.
	- Keywords: ` hashing `, ` sha512_224 `, ` hash `, ` sha512224 `
- **Hash SHA512_256**:
	- Hashes given string using `sha512_256`.
	- Keywords: ` hashing `, ` hash `, ` sha512_256 `, ` sha512256 `
- **Hash SHAKE_128**:
	- Hashes given string using `shake_128`.
	- Keywords: ` shake128 `, ` hashing `, ` shake_128 `, ` hash `
- **Hash SHAKE_256**:
	- Hashes given string using `shake_256`.
	- Keywords: ` hashing `, ` shake_256 `, ` shake256 `, ` hash `
- **Hash SM3**:
	- Hashes given string using `sm3`.
	- Keywords: ` hashing `, ` hash `, ` sm3 `
- **Hash WHIRLPOOL**:
	- Hashes given string using `whirlpool`.
	- Keywords: ` whirlpool `, ` hashing `, ` hash `
- **Help**:
	- Search through modules.
	- Keywords: ` modules `, ` module `, ` help `, ` features `
- **IP**:
	- Gets ip addresses.
	- Keywords: ` ip `, ` ipv4 `, ` ipv6 `
- **Length**:
	- Get length of a string.
	- Keywords: ` length `, ` len `
- **Rainbowtables**:
	- Uses online APIs to *try* cracking a password hash.
	- Keywords: ` rainbowtable `, ` dehash `, ` rainbowtables `, ` rainbow `
- **Regex**:
	- Displays regex visualization.
- **Roms**:
	- Search for console roms.
	- Keywords: ` nintendo `, ` roms `, ` consoles `, ` games `, ` emulation `
- **Service**:
	- Display info about services running.
- **Streaming**:
	- Search for movie or tv series streaming
	- Keywords: ` series `, ` streaming `, ` tv `, ` movies `
- **UserAgent**:
	- Returns your and random useragent.
	- Keywords: ` ua `, ` user agent `, ` useragent `, ` brand `
- **Wolfram Alpha**:
	- Query Wolfram|Alpha.

<!--modules-->