import fitz  # PyMuPDF

try:
    doc = fitz.open('ML_Assignment_2.pdf')
    print(f"Total pages: {len(doc)}\n")
    
    # Extract text from first 3 pages
    full_text = ""
    for i, page in enumerate(doc[:3]):
        text = page.get_text()
        full_text += f"\n--- PAGE {i} ---\n{text}\n"
    
    print(full_text)
    
    # Look for Section 3
    if "Section 3" in full_text or "SECTION 3" in full_text:
        print("\n\n=== FOUND SECTION 3 ===")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
