"""
    Copyright (c) 2021 Fedora Websites and Apps

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

from json import loads
from time import time


class ErraticReturns(object):
    def parameter_error_return_data(self):
        return_data = {
            "status": "FAIL",
            "salute": "Could not fetch requested information",
            "reason": "Command string could not be interpreted",
            "collection_fetched_at": time()
        }
        return return_data

    def file_read_error_return_data(self):
        return_data = {
            "status": "FAIL",
            "salute": "Could not fetch requested information",
            "reason": "Index file could not be accessed",
            "collection_fetched_at": time()
        }
        return return_data


class TicketDataRetrieval(object):
    def __init__(self):
        self.filename = "tickdata.json"
        with open(self.filename, "r") as self.fileobjc:
            self.dictcont = loads(self.fileobjc.read())

    def preliminary_information(self):
        try:
            return_data = {
                "status": "PASS",
                "forges": {},
                "collection_fetched_at": 0.0
            }
            for forge in self.dictcont["forges"].keys():
                forge_info = {
                    "name": forge,
                    "repository_list": {}
                }
                for repository in self.dictcont["forges"][forge].keys():
                    repository_info = {
                        "name": repository,
                        "description": self.dictcont["forges"][forge][repository]["description"],
                        "contact": self.dictcont["forges"][forge][repository]["contact"],
                        "issue_list": {}
                    }
                    for issue in self.dictcont["forges"][forge][repository]["ticket_list"].keys():
                        issue_info = {
                            "title": self.dictcont["forges"][forge][repository]["ticket_list"][issue]["title"],
                            "labels": self.dictcont["forges"][forge][repository]["ticket_list"][issue]["labels"]
                        }
                        repository_info["issue_list"][issue] = issue_info
                    forge_info[repository] = repository_info
                return_data["forges"][forge] = forge_info
            return_data["collection_fetched_at"] = time()
        except Exception as expt:
            return_data = {
                "status": "FAIL",
                "salute": "Could not fetch preliminary information",
                "reason": str(expt),
                "collection_fetched_at": time()
            }
        return return_data

    def repository_information(self, forge, repository):
        try:
            return_data = {
                "status": "PASS",
                "information": {
                    "name": repository,
                    "forge": forge,
                    "ticket_count": self.dictcont["forges"][forge][repository]["ticket_count"],
                    "contact": self.dictcont["forges"][forge][repository]["contact"],
                    "url": self.dictcont["forges"][forge][repository]["url"],
                    "description": self.dictcont["forges"][forge][repository]["description"],
                    "id": self.dictcont["forges"][forge][repository]["id"],
                    "target_label": self.dictcont["forges"][forge][repository]["target_label"],
                    "maintainer": self.dictcont["forges"][forge][repository]["maintainer"],
                    "date_created": self.dictcont["forges"][forge][repository]["date_created"]
                },
                "collection_fetched_at": time()
            }
        except Exception as expt:
            return_data = {
                "status": "FAIL",
                "salute": "Could not fetch repository information",
                "reason": str(expt),
                "collection_fetched_at": time()
            }
        return return_data

    def issue_information(self, forge, repository, number):
        try:
            return_data = {
                "status": "PASS",
                "information": {
                    "name": repository,
                    "forge": forge,
                    "number": number,
                    "title": self.dictcont["forges"][forge][repository]["ticket_list"][number]["title"],
                    "date_created": self.dictcont["forges"][forge][repository]["ticket_list"][number]["date_created"],
                    "last_updated": self.dictcont["forges"][forge][repository]["ticket_list"][number]["last_updated"],
                    "creator": self.dictcont["forges"][forge][repository]["ticket_list"][number]["creator"],
                    "url": self.dictcont["forges"][forge][repository]["ticket_list"][number]["url"],
                    "labels": self.dictcont["forges"][forge][repository]["ticket_list"][number]["labels"]
                },
                "collection_fetched_at": time()
            }
        except Exception as expt:
            return_data = {
                "status": "FAIL",
                "salute": "Could not fetch issue information",
                "reason": str(expt),
                "collection_fetched_at": time()
            }
        return return_data
