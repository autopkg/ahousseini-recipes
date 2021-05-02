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
"""See docstring for ArchiLatestGitHubTagProvider class"""

import json

from autopkglib import URLGetter

__all__ = ["ArchiLatestGitHubTagProvider"]


class ArchiLatestGitHubTagProvider(URLGetter):
    """Provides the version for the latest Archi release."""

    description = __doc__
    input_variables = {
        "appcast_url": {"required": False, "description": "URL to Archi appcast"}
    }

    output_variables = {
        "tag": {"description": ("GitHub tag of the latest Archi release.")}
    }

    def main(self):
        """Grab GitHub tag from appcast"""

        appcast_url = "https://api.github.com/repos/archimatetool/archi/tags"

        appcast = self.download(appcast_url)

        data = json.loads(appcast.decode("utf-8"))
        parsed = data[0]["name"]

        self.env["tag"] = parsed
        self.output("Found tag %s" % self.env["tag"])


if __name__ == "__main__":
    processor = ArchiLatestGitHubTagProvider()
    processor.execute_shell()
