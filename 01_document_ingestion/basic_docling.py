
from pathlib import Path

from docling.document_converter import DocumentConverter


def convert_document(input_path: str) -> str:
    """
    Convert a supported document into Markdown using Docling.
    """

    source = Path(input_path)

    # Step 1: Validate the input file.
    if not source.exists():
        raise FileNotFoundError(f"File not found: {source}")

    if not source.is_file():
        raise ValueError(f"Expected a file: {source}")

    # Step 2: Create the converter.
    converter = DocumentConverter()

    # Step 3: Convert the document.
    result = converter.convert(str(source))

    # Step 4: Check conversion status.
    print(f"Conversion status: {result.status}")

    # Step 5: Access the structured document.
    document = result.document

    # Step 6: Export the document as Markdown.
    markdown_content = document.export_to_markdown()

    return markdown_content


def main():
    input_file = Path("sample_documents/pdf/sample.pdf")
    output_file = Path("sample_documents/pdf/extracted.md")

    try:
        markdown_content = convert_document(str(input_file))

        output_file.write_text(
            markdown_content,
            encoding="utf-8"
        )

        print("Document conversion successful!")
        print(f"Output saved to: {output_file}")
        print(f"Extracted characters: {len(markdown_content)}")

    except Exception as error:
        print(f"Document conversion failed: {error}")


if __name__ == "__main__":
    main()
