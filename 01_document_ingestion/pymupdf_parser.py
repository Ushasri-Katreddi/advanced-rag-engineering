
from pathlib import Path

import pymupdf


def extract_pdf_text(input_path: str) -> list[dict]:
    """
    Extract text from a PDF using PyMuPDF.

    Returns one dictionary per page.
    """

    source = Path(input_path)

    # 1. Validate the file.
    if not source.exists():
        raise FileNotFoundError(f"PDF not found: {source}")

    if not source.is_file():
        raise ValueError(f"Expected a file: {source}")

    if source.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    extracted_pages = []

    # 2. Open the PDF.
    with pymupdf.open(source) as pdf:

        # 3. Read document metadata.
        print(f"Total pages: {len(pdf)}")
        print(f"Document metadata: {pdf.metadata}")

        # 4. Process each page individually.
        for page_number, page in enumerate(pdf, start=1):

            # 5. Extract text from the current page.
            page_text = page.get_text("text")

            extracted_pages.append({
                "page_number": page_number,
                "content": page_text
            })

    return extracted_pages


def main():
    input_file = "sample_documents/pdf/sample.pdf"

    try:
        pages = extract_pdf_text(input_file)

        for page in pages:
            print(f"\n--- Page {page['page_number']} ---")
            print(page["content"][:500])

        print(f"\nSuccessfully extracted {len(pages)} pages.")

    except Exception as error:
        print(f"PDF extraction failed: {error}")


if __name__ == "__main__":
    main()
