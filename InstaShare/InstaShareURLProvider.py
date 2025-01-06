# Copyright 2023 Anver Housseini
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
"""See docstring for InstaShareURLProvider class"""

import json

from autopkglib import URLGetter

__all__ = ["InstaShareURLProvider"]


class InstaShareURLProvider(URLGetter):
    """Provides the URL for the latest InstaShare release."""

    description = __doc__
    input_variables = {
        "appcast_url": {"required": False, "description": "URL to InstaShare appcast"}
    }

    output_variables = {
        "url": {"description": ("Download URL of the latest InstaShare release.")}
    }

    def main(self):
        """Grab url from appcast"""

        appcast_url = (
            "https://www.benq.com/api/esupport-tm/getFiles/en_gb/InstaShare/en_gb"
        )

        appcast = self.download(appcast_url)

        data = json.loads(appcast.decode("utf-8"))

        detail = data["response"]["list"]["detail"]

        for i in range(len(detail)):
            if "Mac" in detail[i]["OS"]:
                parsed = detail[i]["Download"]
                break

        self.env["url"] = parsed
        self.output("URL is %s" % self.env["url"])


if __name__ == "__main__":
    processor = InstaShareURLProvider()
    processor.execute_shell()
