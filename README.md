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

<!--modules-->