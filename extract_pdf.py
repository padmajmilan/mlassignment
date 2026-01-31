import PyPDF2

try:
    with open('ML_Assignment_2.pdf', 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        print(f"Total pages: {len(pdf.pages)}\n")
        
        # Extract text from first few pages
        for i, page in enumerate(pdf.pages[:6]):
            text = page.extract_text()
            print(f"\n--- PAGE {i+1} ---\n{text}\n")
            
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
