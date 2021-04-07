#!/usr/local/autopkg/python
#
# Copyright 2020 Anver Housseini
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for AircallURLProvider class"""

import json

from autopkglib import URLGetter

__all__ = ["AircallURLProvider"]


class AircallURLProvider(URLGetter):
    """Provides the URL for the latest Aircall release."""

    description = __doc__
    input_variables = {
        "appcast_url": {"required": False, "description": "URL to Aircall appcast"}
    }

    output_variables = {"url": {"description": ("URL of the latest Aircall release.")}}

    def main(self):
        """Grab version from appcast"""

        appcast_url = "https://electron.aircall.io/update/osx/0.0.0"

        appcast = self.download(appcast_url)

        data = json.loads(appcast.decode("utf-8"))
        parsed = data["url"]

        self.env["url"] = parsed
        self.output("Found url %s" % self.env["url"])


if __name__ == "__main__":
    processor = AircallURLProvider()
    processor.execute_shell()
