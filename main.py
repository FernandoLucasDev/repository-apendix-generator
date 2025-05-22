from src.services.github_service import GitHubService

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

print(prompt)