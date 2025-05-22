from src.services.github_service import GitHubService
from src.services.report_service import ReportService

service = GitHubService("flutter", "flutter")

default_branch = service.get_default_branch()
commits = service.get_commits(branch=default_branch)
tags = service.get_tags()
langs = service.get_languages()

prompt = {
    "commits": commits,
    "tags": tags,
    "langs": langs
}

#print(prompt)
report = ReportService(prompt=prompt)
report.get_report()