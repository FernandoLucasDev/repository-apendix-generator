import os
import requests
from dotenv import load_dotenv

load_dotenv()


class GitHubService:
    def __init__(self, owner, repo):
        self.base_url = "https://api.github.com"
        self.owner = owner
        self.repo = repo
        self.token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"token {self.token}"}

    def get_default_branch(self):
        info = self.get_repo_info()
        return info.get("default_branch", "main")

    def get_commits(self, branch="main"):
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/commits"
        params = {"sha": branch, "per_page": 100}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_languages(self):
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/languages"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_tags(self):
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/tags"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repo_info(self):
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()