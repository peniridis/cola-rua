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

import unittest

from cola.core.opener import PuppeteerOpener


class Test(unittest.TestCase):

    def testPuppeteerOpener(self):
        test_url = 'http://www.baidu.com'
        opener = PuppeteerOpener()

        # assert 'baidu' in opener.open(test_url)

        br = opener.browse_open(test_url)
        # assert '百度' in br.title()
        # assert 'baidu' in br.response().read()



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
