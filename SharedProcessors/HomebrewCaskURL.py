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
"""See docstring for HomebrewCaskURL class"""

import os, ssl, json
import urllib.request
import urllib.error
import urllib.parse

from autopkglib import Processor, ProcessorError  # pylint: disable=import-error

__all__ = ["HomebrewCaskURL"]

class HomebrewCaskURL(Processor):
	"""An AutoPkg processor which reads the download url from the Homebrew Cask API."""

	input_variables = {
        "cask_name": {
            "required": True,
            "description": (
                "Name of cask to fetch, as would be given to the 'brew' command. Example: 'firefox'"
            ),
        }
    }
	output_variables = {
        "url": {
        	"description": (
        		"URL for the Cask's download."
        	)
        }
    }
    
	description = __doc__
    
	def main(self):
		ssl._create_default_https_context = ssl._create_unverified_context
		
		homebrew_api_baseurl = (
            "https://formulae.brew.sh/api/cask"
        )
    
		cask_url = f"{homebrew_api_baseurl}/{self.env['cask_name']}.json"
		try:
			urlobj = urllib.request.urlopen(cask_url)
		except urllib.error.HTTPError as err:
			raise ProcessorError(f"Error opening URL {cask_url}: {err}")

		formula_data = urlobj.read()

		with urllib.request.urlopen(cask_url) as url:
			data = json.loads(url.read().decode())
		parsed = (data['url'])

		self.env["url"] = parsed

		self.output(
			f"Got URL {self.env['url']} for cask '{self.env['cask_name']}':"
		)

if __name__ == "__main__":
    PROCESSOR = HomebrewCaskURL()
    PROCESSOR.execute_shell()