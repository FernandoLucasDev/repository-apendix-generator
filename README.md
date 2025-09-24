# Tech Health Appendix Generator - MVP

## Overview
This is a project of appendix generator based on GitHub data and analysis with AI.


## How the Solution Addresses the Core Problem
This MVP has the ability to analyze essential parameters of a repository/project and provide a concise analysis on the state and quality of the application/system.

## Development Time Tracking


**Total estimated time:** Approximately 3 hours and 14 minutes. between creation of GitHub integration, generation of PDF file, creation of flow to format PDF style, prompt implementation with real data and end-to-end tests.

### Instructions to run:

- Rename the file .envexample to .env
- For the GitHub key, click [here](https://github.com/settings/tokens) to generate your GitHub token, to read, and than past the key for the GITHUB_TOKEN on .env
- For the Groq API key just access the [Groq Cloud](https://console.groq.com/keys), create an account and generate the api key. It is simple and free. When you have your key, add to the GROQ_KEY on .env
- When it is ready, in terminal, access the root of the project and run `pip install -r requirements.txt`. Than, if everything is ok, run: `python main.py`. It will get paramiters of a repository and generate a PDF report on templates folder.



