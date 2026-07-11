from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os

def generate_report(analysis: dict, output_path: str):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Setup document with proper margins to prevent text cut-off
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)
    
    styles = getSampleStyleSheet()
    
    # Custom Premium Styles
    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontSize=22, textColor=colors.HexColor("#2563eb"),
        spaceAfter=20, alignment=1 # Center aligned
    )
    
    h2_style = ParagraphStyle(
        'Heading2', parent=styles['Heading2'],
        fontSize=14, textColor=colors.HexColor("#1e293b"),
        spaceBefore=15, spaceAfter=10
    )
    
    normal_style = styles['Normal']
    normal_style.fontSize = 11
    normal_style.leading = 16 # Line height for readability

    elements = []
    
    # Title
    elements.append(Paragraph("Resumind AI - Executive Report", title_style))
    elements.append(Spacer(1, 10))
    
    # Metric Scores Table
    score_data = [
        ["Resume Score", f"{analysis.get('resume_score', 'N/A')}/100"],
        ["ATS Score", f"{analysis.get('ats_score', 'N/A')}/100"],
        ["Health Status", str(analysis.get('resume_health', 'N/A'))]
    ]
    
    score_table = Table(score_data, colWidths=[150, 150])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#0f172a")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#e2e8f0"))
    ]))
    
    elements.append(score_table)
    elements.append(Spacer(1, 20))
    
    # Executive Summary (This will now wrap correctly!)
    elements.append(Paragraph("Executive Summary", h2_style))
    for line in analysis.get('summary', []):
        # Paragraph automatically wraps text based on page margins
        elements.append(Paragraph(f"• {line}", normal_style))
        elements.append(Spacer(1, 5))
        
    # Strengths & Weaknesses
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("Strengths", h2_style))
    for s in analysis.get('strengths', []):
        elements.append(Paragraph(f"✓ {s}", normal_style))
        elements.append(Spacer(1, 3))
        
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("Areas for Improvement", h2_style))
    for w in analysis.get('weaknesses', []):
        elements.append(Paragraph(f"⚠ {w}", normal_style))
        elements.append(Spacer(1, 3))
        
    # Build the PDF
    doc.build(elements)
    
    return output_path