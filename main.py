import os
from utils.file_reader import read_file
from utils.classifier import categorize
from utils.report_generator import generate_pdf_report, generate_summary
from utils.logger import setup_logger, log_success, log_error

INPUT_FOLDER = "input_documents"
OUTPUT_SUMMARY = "output/summaries"
OUTPUT_CATEGORY = "output/categories"
OUTPUT_REPORT = "output/reports"

def create_folders():
    os.makedirs(OUTPUT_SUMMARY, exist_ok=True)
    os.makedirs(OUTPUT_CATEGORY, exist_ok=True)
    os.makedirs(OUTPUT_REPORT, exist_ok=True)

def process_documents():
    for file in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, file)

        try:
            text = read_file(file_path)
            if not text.strip():
                continue

            category = categorize(text)

        
            summary = generate_summary(text)
            with open(os.path.join(OUTPUT_SUMMARY, file + "_summary.txt"), "w", encoding="utf-8") as f:
                f.write(summary)

            
            with open(os.path.join(OUTPUT_CATEGORY, file + "_category.txt"), "w") as f:
                f.write(category)

            
            report_path = os.path.join(OUTPUT_REPORT, file + "_report.pdf")
            generate_pdf_report(file, text, category, report_path)

            log_success(file, category)

        except Exception as e:
            log_error(file, str(e))

if __name__ == "__main__":
    setup_logger()
    create_folders()
    process_documents()
    print("Processing Completed Successfully!")