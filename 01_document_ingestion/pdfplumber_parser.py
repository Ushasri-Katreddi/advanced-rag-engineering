
from pathlib import Path

import pdfplumber


def extract_pdf_text(input_path: str) -> list[dict]:
    """Extract text from a PDF using pdfplumber."""

    source = Path(input_path)

    if not source.exists():
        raise FileNotFoundError(f"PDF not found: {source}")

    if not source.is_file():
        raise ValueError(f"Expected a file: {source}")

    if source.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    extracted_pages = []

    with pdfplumber.open(source) as pdf:
        print(f"Total pages: {len(pdf.pages)}")

        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""

            extracted_pages.append({
                "page_number": page_number,
                "content": page_text,
                "character_count": len(page_text),
            })

    return extracted_pages


def main():
    input_file = "sample_documents/pdf/sample.pdf"

    try:
        pages = extract_pdf_text(input_file)

        for page in pages:
            print(f"\n--- Page {page['page_number']} ---")
            print(page["content"][:500])
            print(f"Characters: {page['character_count']}")

        print(f"\nSuccessfully extracted {len(pages)} pages.")

    except Exception as error:
        print(f"PDF extraction failed: {error}")


if __name__ == "__main__":
    main()
