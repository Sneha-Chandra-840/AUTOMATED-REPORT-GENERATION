from fpdf import FPDF

def read_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    return header, data

def analyze_data(data):
    marks = [int(row[1]) for row in data]
    total_students = len(marks)
    average = sum(marks) / total_students
    highest = max(marks)
    lowest = min(marks)
    return total_students, average, highest, lowest

def generate_pdf(header, data, total, avg, high, low):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(100, 10, header[0], border=1)
    pdf.cell(40, 10, header[1], border=1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for row in data:
        pdf.cell(100, 10, row[0], border=1)
        pdf.cell(40, 10, row[1], border=1)
        pdf.ln()

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Students: {total}", ln=True)
    pdf.cell(200, 10, txt=f"Average Marks: {avg:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Highest Marks: {high}", ln=True)
    pdf.cell(200, 10, txt=f"Lowest Marks: {low}", ln=True)

    pdf.output("report.pdf")

header, data = read_data("input.txt")
total, avg, high, low = analyze_data(data)
generate_pdf(header, data, total, avg, high, low)

print("PDF report 'report.pdf' successfully created!")
