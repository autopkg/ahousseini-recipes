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
"""See docstring for CallbarVersionProvider class"""

import ssl, certifi, re, json
from urllib.request import urlopen


from autopkglib import Processor, ProcessorError


__all__ = ["CallbarVersionProvider"]


APPCAST_URL = "https://downloadcallbar.talkdesk.com/release_metadata.json"


class CallbarVersionProvider(Processor):

	"""Provides the version for the latest Callbar release."""

	input_variables = {
		"appcast_url": {
			"required": False,
			"description": "Default is %s" % APPCAST_URL
		}
	}

	output_variables = {
		"version": {
			"description": (
				"Version of the latest Callbar release."
			)
		}
	}
	description = __doc__

	def get_version(self, appcast_url):

		try:
			jsonData = json.loads(urlopen(appcast_url, context=ssl.create_default_context(cafile=certifi.where())).read())
			return str(jsonData['version'])
		except BaseException as err:
			raise Exception("Can't read %s: %s" % (appcast_url, err))

	def main(self):
		appcast_url = self.env.get("appcast_url", APPCAST_URL)
		self.env["version"] = self.get_version(appcast_url)
		self.output("Version number %s" % self.env["version"])

if __name__ == "__main__":
	processor = CallbarVersionProvider()
	processor.execute_shell()