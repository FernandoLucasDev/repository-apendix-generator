from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
import re

class AiService:
    def __init__(self):
        ...

    def parse_to_flowables(self, raw_text):
        styles = getSampleStyleSheet()
        style_normal = styles["Normal"]
        style_bold = ParagraphStyle('Bold', parent=style_normal, fontName='Helvetica-Bold', fontSize=12, spaceAfter=6)
        style_justify = ParagraphStyle('Justify', parent=style_normal, alignment=TA_JUSTIFY)
        style_subtitle = ParagraphStyle('Subtitle', parent=style_normal, fontName='Helvetica-Bold', fontSize=14, spaceAfter=10)
        
        flowables = []
        lines = raw_text.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('**') and line.endswith('**'):
                title_text = line.strip('*').strip()
                title_text = self.format_inline_bold_gray(title_text)
                flowables.append(Paragraph(title_text, style_bold))
                flowables.append(Spacer(1, 12))

            elif line.startswith('###'):
                subtitle_text = line.lstrip('#').strip()
                subtitle_text = self.format_inline_bold_gray(subtitle_text)
                flowables.append(Paragraph(subtitle_text, style_subtitle))
                flowables.append(Spacer(1, 10))

            elif line.startswith('*') or line.startswith('+'):
                items = []
                while i < len(lines) and (lines[i].strip().startswith('*') or lines[i].strip().startswith('+')):
                    item_text = lines[i].strip().lstrip('*+').strip()
                    item_text = self.format_inline_bold_gray(item_text)
                    items.append(Paragraph(item_text, style_justify))
                    i += 1
                i -= 1

                flowables.append(ListFlowable(
                    [ListItem(i) for i in items],
                    bulletType='bullet',
                    bulletColor=colors.black,
                    leftIndent=20
                ))
                flowables.append(Spacer(1, 10))

            elif line:
                line = self.format_inline_bold_gray(line)
                flowables.append(Paragraph(line, style_justify))
                flowables.append(Spacer(1, 8))
            
            i += 1
        
        return flowables

    def format_inline_bold_gray(self, text):
        return re.sub(r'\*\*(.*?)\*\*', r'<font color="#666666"><b>\1</b></font>', text)
