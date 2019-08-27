# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 Zhang peng <roocpeng@foxmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2019-8-26

@author: peniridis
"""
# Standard library imports
import asyncio

# Related third party imports
try:
    import pyppeteer
except ImportError:
    from cola.core.errors import DependencyNotInstalledError

    raise DependencyNotInstalledError('pyppeteer')

from pyppeteer.network_manager import Request, Response


# Local application/library specific imports


class Opener(object):
    def open(self, url):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError


class PuppeteerOpener(Opener):
    def __init__(self, cookie_filename=None, user_agent=None, timeout=None, **kwargs):
        self.browser = None

    def open(self, url):
        pass

    def read(self):
        pass

    def browse_open(self, url, data=None, timeout=None):
        asyncio.get_event_loop().run_until_complete(self._browse_open(url, data, timeout))

    async def _browse_open(self, url, data=None, timeout=None):
        self.browser = await pyppeteer.launch({
            'headless': False,  # 关闭无头模式
            'devtools': True,  # 打开 chromium 的 devtools
            'executablePath': '/Users/melkor/Melkor/06-Tools/webdriver/Chromium.app/Contents/MacOS/Chromium',
            'args': [
                '--disable-extensions',
                '--hide-scrollbars',
                '--disable-bundled-ppapi-flash',
                '--mute-audio',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
            ],
            'dumpio': True,
        })
        page = await self.browser.newPage()
        await page.evaluate("""
            () =>{
                Object.defineProperties(navigator,{
                    webdriver:{
                    get: () => false
                    }
                })
            }
        """)
        page.on('request', self.req_intercept)
        page.on('response', self.resp_intercept)
        resp = await page.goto('http://example.com')
        # await page.screenshot({'path': 'example.png'})
        print(resp.headers)
        print(resp.text())
        # await self.browser.close()

    async def req_intercept(self, req: Request):
        print(f'Original header: {req.headers}')
        req.headers.update({'Accept-Encoding': 'gzip'})
        await req.continue_(overrides={'headers': req.headers})

    async def resp_intercept(self, resp: Response):
        print(f"New header: {resp.request.headers}")
