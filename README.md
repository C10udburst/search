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
- **Apps**: Search for Android apps.
- **Base64 Decode**: Decode ASCII string using the standard Base64 alphabet.
- **Base64 Encode**: Encode ASCII string using the standard Base64 alphabet.
- **Bins**: Return gists.
- **Duck answers**: Retrieve instant answers from duck duck go.
- **Ebooks**: Search for ebooks using `r/Piracy` cse.
- **Email**: Display info about an email.
- **Files**: Search for files
- **Games**: Search for game cracks.
- **Google**: Searches using Google.
- **Google Drive**: Search for files in google drive
- **Hash BLAKE2B**: Hashes given string using `blake2b`.
- **Hash BLAKE2S**: Hashes given string using `blake2s`.
- **Hash MD4**: Hashes given string using `md4`.
- **Hash MD5**: Hashes given string using `md5`.
- **Hash MD5-SHA1**: Hashes given string using `md5-sha1`.
- **Hash MDC2**: Hashes given string using `mdc2`.
- **Hash RIPEMD160**: Hashes given string using `ripemd160`.
- **Hash SHA1**: Hashes given string using `sha1`.
- **Hash SHA224**: Hashes given string using `sha224`.
- **Hash SHA256**: Hashes given string using `sha256`.
- **Hash SHA384**: Hashes given string using `sha384`.
- **Hash SHA3_224**: Hashes given string using `sha3_224`.
- **Hash SHA3_256**: Hashes given string using `sha3_256`.
- **Hash SHA3_384**: Hashes given string using `sha3_384`.
- **Hash SHA3_512**: Hashes given string using `sha3_512`.
- **Hash SHA512**: Hashes given string using `sha512`.
- **Hash SHA512_224**: Hashes given string using `sha512_224`.
- **Hash SHA512_256**: Hashes given string using `sha512_256`.
- **Hash SHAKE_128**: Hashes given string using `shake_128`.
- **Hash SHAKE_256**: Hashes given string using `shake_256`.
- **Hash SM3**: Hashes given string using `sm3`.
- **Hash WHIRLPOOL**: Hashes given string using `whirlpool`.
- **Help**: Search through modules.
- **IP**: Gets ip addresses.
- **Length**: Get length of a string.
- **Rainbowtables**: Uses online APIs to *try* cracking a password hash.
- **Regex**: Displays regex visualization.
- **Service**: Display info about services running.
- **UserAgent**: Returns your and random useragent.
- **Wolfram Alpha**: Query Wolfram|Alpha.

<!--modules-->