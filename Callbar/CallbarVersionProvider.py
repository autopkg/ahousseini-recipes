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

import os, ssl, json
import urllib.request
import urllib.error
import urllib.parse

from autopkglib import Processor  # pylint: disable=import-error

APPCAST_URL = "https://downloadcallbar.talkdesk.com/release_metadata.json"

__all__ = ["CallbarVersionProvider"]

class CallbarVersionProvider(Processor):
	"""Provides the version for the latest Callbar release."""

	input_variables = {
        "appcast_url": {"required": False, "description": "Default is %s" % APPCAST_URL,},
    }

	output_variables = {
        "url": {
        	"description": (
        		"URL to the latest Callbar release."
			)
		}
	}

	description = __doc__

	def main(self):
		ssl._create_default_https_context = ssl._create_unverified_context

		try:
			urlobj = urllib.request.urlopen(APPCAST_URL)
		except urllib.error.HTTPError as err:
			raise ProcessorError(f"Error opening URL {APPCAST_URL}: {err}")

		formula_data = urlobj.read()

		with urllib.request.urlopen(APPCAST_URL) as url:
			data = json.loads(url.read().decode())
		parsed = (data['version'])

		self.env["version"] = parsed

		self.output(
			f"Got version {self.env['version']}:"
		)

if __name__ == "__main__":
	PROCESSOR = CallbarVersionProvider()
	PROCESSOR.execute_shell()