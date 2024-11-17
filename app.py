from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Collect form data
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        education = request.form.get("education")
        skills = request.form.get("skills")
        experience = request.form.get("experience")
        
        # Generate PDF
        pdf_path = generate_pdf(name, email, phone, education, skills, experience)
        return send_file(pdf_path, as_attachment=True)

    return render_template("form.html")

def generate_pdf(name, email, phone, education, skills, experience):
    # Create a PDF file
    pdf_path = "cv.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    text = c.beginText(50, 750)

    # Add content to the PDF
    text.textLine(f"Name: {name}")
    text.textLine(f"Email: {email}")
    text.textLine(f"Phone: {phone}")
    text.textLine(f"Education: {education}")
    text.textLine(f"Skills: {skills}")
    text.textLine(f"Experience: {experience}")

    c.drawText(text)
    c.save()
    return pdf_path

if __name__ == "__main__":
    app.run(debug=True)
