import os
import requests
from fpdf import FPDF
from pdfid import pdfid


# 下载示例PDF文件
def download_sample_pdfs(directory):
    urls = [
        'http://www.africau.edu/images/default/sample.pdf',
        'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
    ]
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i, url in enumerate(urls):
        response = requests.get(url)
        file_path = os.path.join(directory, f'sample_{i + 1}.pdf')
        with open(file_path, 'wb') as file:
            file.write(response.content)
    print("Sample PDFs downloaded.")


# 分析PDF文件
def analyze_pdf(file_path):
    result = pdfid.PDFiDMain(file_path)
    return result


# 创建PDF报告
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'PDF Vulnerability Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_analysis(self, file_name, analysis):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Analysis for: {file_name}', 0, 1)
        self.set_font('Arial', '', 12)
        for line in analysis.split('\n'):
            self.multi_cell(0, 10, line)
            self.ln()


# 生成报告
def generate_report(analysis_results, output_file):
    pdf = PDFReport()
    pdf.add_page()
    for file_name, analysis in analysis_results.items():
        pdf.add_analysis(file_name, analysis)
    pdf.output(output_file)


# 主函数
def main(directory):
    download_sample_pdfs(directory)
    analysis_results = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(directory, file_name)
            analysis_results[file_name] = analyze_pdf(file_path)

    generate_report(analysis_results, 'pdf_vulnerability_report.pdf')


if __name__ == '__main__':
    main('pdf_samples')
