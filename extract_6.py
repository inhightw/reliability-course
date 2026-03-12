from pypdf import PdfReader

def extract_pages(pdf_path, start_page, end_page, output_name):
    start_index = start_page - 1
    end_index = end_page - 1
    
    text = ""
    try:
        reader = PdfReader(pdf_path)
        max_pages = len(reader.pages)
        if end_index >= max_pages:
            end_index = max_pages - 1
            
        for i in range(start_index, end_index + 1):
            page = reader.pages[i]
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
                
        with open(output_name, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Successfully extracted {start_page}-{end_page} to {output_name}")
    except Exception as e:
        print(f"Error processing {output_name}: {e}")

pdf_file = "lecture_notes.pdf"
extract_pages(pdf_file, 199, 230, "lesson_6_notes.txt")
