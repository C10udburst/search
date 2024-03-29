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
	- Keywords: ` android `, ` apk `, ` apps `, ` mobile `
- **Base64 Decode**:
	- Decode ASCII string using the standard Base64 alphabet.
- **Base64 Encode**:
	- Encode ASCII string using the standard Base64 alphabet.
	- Keywords: ` b64 `, ` b64encode `, ` base64 `
- **Bins**:
	- Return gists.
	- Keywords: ` bin `, ` bins `, ` gist `, ` paste `, ` pastebin `, ` pastes `, ` text `, ` texts `, ` txt `
- **Duck answers**:
	- Retrieve instant answers from duck duck go.
- **Ebooks**:
	- Search for ebooks using `r/Piracy` cse.
	- Keywords: ` book `, ` books `, ` ebook `, ` ebooks `, ` pdf `, ` reading `
- **Email**:
	- Display info about an email.
- **Ethereum**:
	- Display info about an ethereum address.
- **Files**:
	- Search for files
	- Keywords: ` dl `, ` download `, ` file `, ` files `
- **Games**:
	- Search for game cracks.
	- Keywords: ` crack `, ` cracks `, ` game `, ` games `, ` steam `, ` videogames `
- **Google**:
	- Searches using Google.
- **Google Drive**:
	- Search for files in google drive
	- Keywords: ` download `, ` drive `, ` file `, ` files `
- **Hash BLAKE2B**:
	- Hashes given string using `blake2b`.
	- Keywords: ` blake2b `, ` hash `, ` hashing `
- **Hash BLAKE2S**:
	- Hashes given string using `blake2s`.
	- Keywords: ` blake2s `, ` hash `, ` hashing `
- **Hash MD4**:
	- Hashes given string using `md4`.
	- Keywords: ` hash `, ` hashing `, ` md4 `
- **Hash MD5**:
	- Hashes given string using `md5`.
	- Keywords: ` hash `, ` hashing `, ` md5 `
- **Hash MD5-SHA1**:
	- Hashes given string using `md5-sha1`.
	- Keywords: ` hash `, ` hashing `, ` md5-sha1 `
- **Hash MDC2**:
	- Hashes given string using `mdc2`.
	- Keywords: ` hash `, ` hashing `, ` mdc2 `
- **Hash RIPEMD160**:
	- Hashes given string using `ripemd160`.
	- Keywords: ` hash `, ` hashing `, ` ripemd160 `
- **Hash SHA1**:
	- Hashes given string using `sha1`.
	- Keywords: ` hash `, ` hashing `, ` sha1 `
- **Hash SHA224**:
	- Hashes given string using `sha224`.
	- Keywords: ` hash `, ` hashing `, ` sha224 `
- **Hash SHA256**:
	- Hashes given string using `sha256`.
	- Keywords: ` hash `, ` hashing `, ` sha256 `
- **Hash SHA384**:
	- Hashes given string using `sha384`.
	- Keywords: ` hash `, ` hashing `, ` sha384 `
- **Hash SHA3_224**:
	- Hashes given string using `sha3_224`.
	- Keywords: ` hash `, ` hashing `, ` sha3224 `, ` sha3_224 `
- **Hash SHA3_256**:
	- Hashes given string using `sha3_256`.
	- Keywords: ` hash `, ` hashing `, ` sha3256 `, ` sha3_256 `
- **Hash SHA3_384**:
	- Hashes given string using `sha3_384`.
	- Keywords: ` hash `, ` hashing `, ` sha3384 `, ` sha3_384 `
- **Hash SHA3_512**:
	- Hashes given string using `sha3_512`.
	- Keywords: ` hash `, ` hashing `, ` sha3512 `, ` sha3_512 `
- **Hash SHA512**:
	- Hashes given string using `sha512`.
	- Keywords: ` hash `, ` hashing `, ` sha512 `
- **Hash SHA512_224**:
	- Hashes given string using `sha512_224`.
	- Keywords: ` hash `, ` hashing `, ` sha512224 `, ` sha512_224 `
- **Hash SHA512_256**:
	- Hashes given string using `sha512_256`.
	- Keywords: ` hash `, ` hashing `, ` sha512256 `, ` sha512_256 `
- **Hash SHAKE_128**:
	- Hashes given string using `shake_128`.
	- Keywords: ` hash `, ` hashing `, ` shake128 `, ` shake_128 `
- **Hash SHAKE_256**:
	- Hashes given string using `shake_256`.
	- Keywords: ` hash `, ` hashing `, ` shake256 `, ` shake_256 `
- **Hash SM3**:
	- Hashes given string using `sm3`.
	- Keywords: ` hash `, ` hashing `, ` sm3 `
- **Hash WHIRLPOOL**:
	- Hashes given string using `whirlpool`.
	- Keywords: ` hash `, ` hashing `, ` whirlpool `
- **Help**:
	- Search through modules.
	- Keywords: ` features `, ` help `, ` module `, ` modules `
- **IP**:
	- Gets ip addresses.
	- Keywords: ` ip `, ` ipv4 `, ` ipv6 `
- **Length**:
	- Get length of a string.
	- Keywords: ` len `, ` length `
- **Rainbowtables**:
	- Uses online APIs to *try* cracking a password hash.
	- Keywords: ` dehash `, ` rainbow `, ` rainbowtable `, ` rainbowtables `
- **Regex**:
	- Displays regex visualization.
- **Roms**:
	- Search for console roms.
	- Keywords: ` consoles `, ` emulation `, ` games `, ` nintendo `, ` roms `
- **Service**:
	- Display info about services running.
- **Streaming**:
	- Search for movie or tv series streaming
	- Keywords: ` movies `, ` series `, ` streaming `, ` tv `
- **UserAgent**:
	- Returns your and random useragent.
	- Keywords: ` brand `, ` ua `, ` user agent `, ` useragent `
- **Wolfram Alpha**:
	- Query Wolfram|Alpha.

<!--modules-->