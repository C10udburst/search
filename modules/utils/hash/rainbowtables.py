import asyncio
import json
from typing import List
from aiohttp_requests import requests
import aiohttp
from user_agent import generate_user_agent
import re

from classes import KeywordModule, Result
from classes.widgets import Field


async def alpha(hash_value, hash_type):
    params = {u"hash": hash_value}
    r = requests.get(u"https://hashtoolkit.com/reverse-hash/",
                     headers={'User-Agent': generate_user_agent()},
                     params=params)
    r = await r.text()
    if r.find("No hashes found for") > 0:
        return None
    else:
        return re.findall(r'<a href="/generate-hash/\?text=(.*?)"', r, re.S)[0]


async def beta(hash_value, hash_type):
    r = await requests.get(f"https://hashtoolkit.com/reverse-hash/?hash={hash_value}")
    r = await r.text()
    match = re.search(r'/generate-hash/\?text=(.*?)"', r)
    if match:
        return match.group(1)
    else:
        return None


async def gamma(hash_value, hash_type):
    r = await requests.get(f"https://www.nitrxgen.net/md5db/{hash_value}")
    r = await r.text()
    if r:
        return r
    else:
        return None


async def delta(hash_value, hash_type):
    data = {u"md5": hash_value}
    r = await requests.post("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php",
                            headers={'User-Agent': generate_user_agent()}, data=data)
    r = await r.text()
    result = re.findall(r"Hashed string</span>:\s(.+?)</div>", r)
    if result:
        return result[0]
    else:
        return None


async def theta(hash_value, hash_type):
    r = await requests.get(
        f"https://md5decrypt.net/Api/api.php?hash={hash_value}&hash_type=%{hash_type}&email=deanna_abshire@proxymail.eu&code=1152464b80a61728")
    r = await r.text()
    if len(r) > 0:
        return r
    else:
        return False


async def epsilon(hash_value, hash_type):
    headers = {
        "User-Agent": generate_user_agent(),
        u"Content-Type": u"application/json", u"Referer": "https://www.chamd5.org/",
        u"X-Requested-With": u"XMLHttpRequest"
    }
    data = {u"email": u"jxtepz93152@chacuo.net", u"pass": u"!Z3jFqDKy8r6v4", u"type": u"login"}
    s = aiohttp.ClientSession()
    await s.post(u"https://www.chamd5.org/HttpProxyAccess.aspx/ajax_login", headers=headers, data=json.dumps(data))
    data = {u"hash": hash_value, u"type": hash_type}
    r = await s.post(u"https://www.chamd5.org/HttpProxyAccess.aspx/ajax_me1ody", headers=headers, data=json.dumps(data))
    r = await r.json()
    await s.close()
    msg = re.sub(r"<.+?>", u"", json.loads(r["d"])["msg"])
    if msg.find(u"\u7834\u89e3\u6210\u529f") > 0:
        plain = re.findall(r"\u660e\u6587:(.+?)\u6570\u636e\u6765\u6e90", msg)[0].strip()
        return plain
    elif msg.find(u"\u91d1\u5e01\u4e0d\u8db3") >= 0:
        return msg
    else:
        return False


class RainbowtablesModule(KeywordModule):
    def __init__(self):
        super().__init__("Rainbowtables", "Uses online APIs to *try* cracking a password hash.", [
            "rainbow",
            "rainbowtable",
            "rainbowtables",
            "dehash"
        ])
        self.tests = {
            "md5": [gamma, beta, theta, delta, epsilon],
            "sha1": [alpha, beta, theta, epsilon],
            "sha256": [alpha, beta, theta, epsilon],
            "sha384": [alpha, beta, theta, epsilon],
            "sha512": [alpha, beta, theta, epsilon]
        }

    def find_hash(self, query):
        match = re.findall("[a-f0-9]{128}", query)
        if len(match) > 0:
            return match[0], "sha512"
        match = re.findall("[a-f0-9]{96}", query)
        if len(match) > 0:
            return match[0], "sha384"
        match = re.findall("[a-f0-9]{64}", query)
        if len(match) > 0:
            return match[0], "sha256"
        match = re.findall("[a-f0-9]{40}", query)
        if len(match) > 0:
            return match[0], "sha1"
        match = re.findall("[a-f0-9]{32}", query)
        if len(match) > 0:
            return match[0], "md5"
        return None, None

    async def whitelisted_search(self, query: str) -> List[Result]:
        hash, hash_type = self.find_hash(query.lower())
        if not hash:
            return []
        results = await asyncio.gather(*[
            func(hash, hash_type)
            for func in self.tests[hash_type]
        ], return_exceptions=True)
        results = list(filter(lambda x: isinstance(x, str), results))
        if len(results) < 1:
            return []
        return [Result(
            title="Rainbowtables results",
            summary=f"Hash: `{hash}`, hash type: `{hash_type}`",
            widgets=[Field(
                key="Result",
                value=x
            ) for x in results],
            color=0x00FFFF,
            weight=7
        )]
