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
	- Keywords: ` apk `, ` mobile `, ` android `, ` apps `
- **Base64 Decode**:
	- Decode ASCII string using the standard Base64 alphabet.
- **Base64 Encode**:
	- Encode ASCII string using the standard Base64 alphabet.
	- Keywords: ` b64encode `, ` base64 `, ` b64 `
- **Bins**:
	- Return gists.
	- Keywords: ` bin `, ` gist `, ` txt `, ` texts `, ` paste `, ` bins `, ` pastebin `, ` pastes `, ` text `
- **Duck answers**:
	- Retrieve instant answers from duck duck go.
- **Ebooks**:
	- Search for ebooks using `r/Piracy` cse.
	- Keywords: ` books `, ` book `, ` ebook `, ` reading `, ` ebooks `, ` pdf `
- **Email**:
	- Display info about an email.
- **Ethereum**:
	- Display info about an ethereum address.
- **Files**:
	- Search for files
	- Keywords: ` file `, ` dl `, ` download `, ` files `
- **Games**:
	- Search for game cracks.
	- Keywords: ` steam `, ` cracks `, ` games `, ` game `, ` videogames `, ` crack `
- **Google**:
	- Searches using Google.
- **Google Drive**:
	- Search for files in google drive
	- Keywords: ` drive `, ` file `, ` download `, ` files `
- **Hash BLAKE2B**:
	- Hashes given string using `blake2b`.
	- Keywords: ` hashing `, ` blake2b `, ` hash `
- **Hash BLAKE2S**:
	- Hashes given string using `blake2s`.
	- Keywords: ` hashing `, ` hash `, ` blake2s `
- **Hash MD4**:
	- Hashes given string using `md4`.
	- Keywords: ` hashing `, ` hash `, ` md4 `
- **Hash MD5**:
	- Hashes given string using `md5`.
	- Keywords: ` hashing `, ` hash `, ` md5 `
- **Hash MD5-SHA1**:
	- Hashes given string using `md5-sha1`.
	- Keywords: ` hashing `, ` hash `, ` md5-sha1 `
- **Hash MDC2**:
	- Hashes given string using `mdc2`.
	- Keywords: ` hashing `, ` hash `, ` mdc2 `
- **Hash RIPEMD160**:
	- Hashes given string using `ripemd160`.
	- Keywords: ` hashing `, ` ripemd160 `, ` hash `
- **Hash SHA1**:
	- Hashes given string using `sha1`.
	- Keywords: ` hashing `, ` hash `, ` sha1 `
- **Hash SHA224**:
	- Hashes given string using `sha224`.
	- Keywords: ` hashing `, ` sha224 `, ` hash `
- **Hash SHA256**:
	- Hashes given string using `sha256`.
	- Keywords: ` hashing `, ` hash `, ` sha256 `
- **Hash SHA384**:
	- Hashes given string using `sha384`.
	- Keywords: ` sha384 `, ` hashing `, ` hash `
- **Hash SHA3_224**:
	- Hashes given string using `sha3_224`.
	- Keywords: ` hashing `, ` sha3224 `, ` hash `, ` sha3_224 `
- **Hash SHA3_256**:
	- Hashes given string using `sha3_256`.
	- Keywords: ` hashing `, ` sha3_256 `, ` hash `, ` sha3256 `
- **Hash SHA3_384**:
	- Hashes given string using `sha3_384`.
	- Keywords: ` hashing `, ` sha3_384 `, ` sha3384 `, ` hash `
- **Hash SHA3_512**:
	- Hashes given string using `sha3_512`.
	- Keywords: ` hashing `, ` hash `, ` sha3_512 `, ` sha3512 `
- **Hash SHA512**:
	- Hashes given string using `sha512`.
	- Keywords: ` hashing `, ` sha512 `, ` hash `
- **Hash SHA512_224**:
	- Hashes given string using `sha512_224`.
	- Keywords: ` hashing `, ` hash `, ` sha512_224 `, ` sha512224 `
- **Hash SHA512_256**:
	- Hashes given string using `sha512_256`.
	- Keywords: ` hashing `, ` hash `, ` sha512_256 `, ` sha512256 `
- **Hash SHAKE_128**:
	- Hashes given string using `shake_128`.
	- Keywords: ` hashing `, ` hash `, ` shake_128 `, ` shake128 `
- **Hash SHAKE_256**:
	- Hashes given string using `shake_256`.
	- Keywords: ` hashing `, ` shake256 `, ` shake_256 `, ` hash `
- **Hash SM3**:
	- Hashes given string using `sm3`.
	- Keywords: ` sm3 `, ` hashing `, ` hash `
- **Hash WHIRLPOOL**:
	- Hashes given string using `whirlpool`.
	- Keywords: ` whirlpool `, ` hash `, ` hashing `
- **Help**:
	- Search through modules.
	- Keywords: ` modules `, ` help `, ` module `, ` features `
- **IP**:
	- Gets ip addresses.
	- Keywords: ` ip `, ` ipv4 `, ` ipv6 `
- **Length**:
	- Get length of a string.
	- Keywords: ` len `, ` length `
- **Rainbowtables**:
	- Uses online APIs to *try* cracking a password hash.
	- Keywords: ` dehash `, ` rainbowtables `, ` rainbow `, ` rainbowtable `
- **Regex**:
	- Displays regex visualization.
- **Roms**:
	- Search for console roms.
	- Keywords: ` nintendo `, ` roms `, ` consoles `, ` games `, ` emulation `
- **Service**:
	- Display info about services running.
- **UserAgent**:
	- Returns your and random useragent.
	- Keywords: ` ua `, ` user agent `, ` brand `, ` useragent `
- **Wolfram Alpha**:
	- Query Wolfram|Alpha.

<!--modules-->