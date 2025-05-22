from groq import Groq
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.platypus import SimpleDocTemplate
from datetime import datetime
from .ai_service import AiService
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

        self.pdf_generator(response.choices[0].message.content)

    def pdf_generator(self, content):
        print("Init report PDF generation...")

        ai_utils = AiService()

        dir = "./templates/"
        os.makedirs(dir, exist_ok=True)

        now = datetime.now()
        date_time_string = now.strftime("%Y-%m-%d_%H-%M-%S")

        pdf_file = os.path.join(dir, f"technical_resume_{date_time_string}.pdf")

        doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=60)

        flowables = ai_utils.parse_to_flowables(content) 

        doc.build(flowables)

        print(f"PDF generated at {pdf_file}")