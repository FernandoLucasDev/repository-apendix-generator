from groq import Groq
import os

class ReportService:
    def __init__(self, prompt):
        self.prompt = prompt

    def get_report(self):
        groq_client = Groq(api_key=os.environ["GROQ_KEY"])

        groq_message_prompt = [
            {"role": "system", "content": "You are a wizard who generates technical appendices for investors."},
            {"role": "user", "content": "Generate a technical appendix based on metrics: Commits: 100, Tags: 30, Languages: Python 70%, Shell 30%, Medium complexity: low"}
        ]

        print("Getting report summary with AI...")

        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_message_prompt,
            temperature=0.7,
            max_tokens=1024
        )

        print(response)

    