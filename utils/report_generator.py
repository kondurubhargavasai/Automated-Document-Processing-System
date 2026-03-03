import os
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem
from datetime import datetime

def generate_summary(text):
    sentences = text.split(".")
    summary = ".".join(sentences[:5])
    return summary

def extract_keywords(text):
    words = text.split()
    return list(set(words[:10]))

def extract_dates(text):
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

def extract_amounts(text):
    return re.findall(r"\₹?\$?\d+(?:,\d+)*(?:\.\d{2})?", text)

def generate_pdf_report(file_name, text, category, output_path):
    summary = generate_summary(text)
    keywords = extract_keywords(text)
    dates = extract_dates(text)
    amounts = extract_amounts(text)

    word_count = len(text.split())
    char_count = len(text)

    doc = SimpleDocTemplate(output_path)
    elements = []

    styles = getSampleStyleSheet()
    
    elements.append(Paragraph(f"<b>Report for:</b> {file_name}", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Category:</b> {category}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Generated On:</b> {datetime.now()}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Summary:</b>", styles["Heading3"]))
    elements.append(Paragraph(summary, styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Word Count:</b> {word_count}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Character Count:</b> {char_count}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Dates Found:</b> {', '.join(dates)}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Amounts Found:</b> {', '.join(amounts)}", styles["Normal"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Keywords:</b> {', '.join(keywords)}", styles["Normal"]))

    doc.build(elements)