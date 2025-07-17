"""
Document Q&A Generation

Note: Use `myenv` virtual environment to run ydata, Python 3.10 is installed there
"""
import pandas as pd
import os
import pyarrow as pa
from ydata.synthesizers.text.model.qa import DocumentQAGeneration

if __name__ == "__main__":
    # Authenticate to ydata-sdk
    os.environ['YDATA_LICENSE_KEY'] = 'b179edcd-6f7f-4fc0-b437-ebfb35e1b101'
    print("Initializing Q&A Generator...")
    qa_generator = DocumentQAGeneration()

    # Generate Q&A pairs from multiple documents in a folder
    print("\n=== Processing Multiple Documents ===")
    folder_result = qa_generator.generate(
        input_source="/Users/ramalakshmi/Documents/ydata/data-generation-legalqa-ydata/documents",  # Replace with your folder path
        docs_extension="txt",  # Process all documents with this extension
        num_qa_pairs=30,  # Number of Q&A pairs per document
    )
    print("Multiple documents Q&A pairs:")
    print(folder_result)

    # The below run failed due to exhausion of credits
    folder_result.to_csv("output.csv", index=False)
