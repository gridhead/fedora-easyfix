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


class ErraticReturns:
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
        with open(self.filename, "r") as fileobjc:
            self.dictcont = loads(fileobjc.read())

    def retrieve_preliminary_information(self):
        try:
            return_data = {
                "status": "PASS",
                "forges": {},
                "collection_fetched_at": 0.0
            }
            for forge_name, forge in self.dictcont["forges"].items():
                forge_info = {
                    "name": forge_name,
                    "repository_list": {}
                }
                for repository_name, repository in forge.items():
                    repository_info = {
                        "name": repository_name,
                        "description": repository["description"],
                        "contact": repository["contact"],
                        "issue_list": {}
                    }
                    for issue_id, issue in repository["ticket_list"].items():
                        issue_info = {
                            "title": issue["title"],
                            "labels": issue["labels"]
                        }
                        repository_info["issue_list"][issue_id] = issue_info
                    forge_info[repository_name] = repository_info
                return_data["forges"][forge_name] = forge_info
            return_data["collection_fetched_at"] = time()
        except Exception as expt:
            return_data = {
                "status": "FAIL",
                "salute": "Could not fetch preliminary information",
                "reason": str(expt),
                "collection_fetched_at": time()
            }
        return return_data

    def retrieve_repository_information(self, forge, repository):
        try:
            repository_info = self.dictcont["forges"][forge][repository]
            return_data = {
                "status": "PASS",
                "information": {
                    "name": repository,
                    "forge": forge,
                    "ticket_count": repository_info["ticket_count"],
                    "contact": repository_info["contact"],
                    "url": repository_info["url"],
                    "description": repository_info["description"],
                    "id": repository_info["id"],
                    "target_label": repository_info["target_label"],
                    "maintainer": repository_info["maintainer"],
                    "date_created": repository_info["date_created"]
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

    def retrieve_issue_information(self, forge, repository, number):
        try:
            issue_info = self.dictcont["forges"][forge][repository]["ticket_list"][number]
            return_data = {
                "status": "PASS",
                "information": {
                    "name": repository,
                    "forge": forge,
                    "number": number,
                    "title": issue_info["title"],
                    "date_created": issue_info["date_created"],
                    "last_updated": issue_info["last_updated"],
                    "creator": issue_info["creator"],
                    "url": issue_info["url"],
                    "labels": issue_info["labels"]
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
