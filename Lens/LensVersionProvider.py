#!/usr/local/autopkg/python
#
# Copyright 2021 Anver Housseini
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
"""See docstring for LensVersionProvider class"""

import json

from autopkglib import URLGetter

__all__ = ["LensVersionProvider"]


class LensVersionProvider(URLGetter):
    """Provides the version for the latest Lens release."""

    description = __doc__
    input_variables = {
        "appcast_url": {"required": False, "description": "URL to Lens appcast"}
    }

    output_variables = {
        "version": {"description": ("Version of the latest Lens release.")}
    }

    def main(self):
        """Grab version from appcast"""

        appcast_url = "https://api.k8slens.dev/binaries/latest.json"

        manifest = self.download(appcast_url)

        data = json.loads(manifest.decode("utf-8"))
        parsed = data["version"]

        self.env["version"] = parsed
        self.output("Version number %s" % self.env["version"])


if __name__ == "__main__":
    processor = LensVersionProvider()
    processor.execute_shell()
