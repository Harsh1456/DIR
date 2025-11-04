# Driver Inspection Report Processor

A modular monolithic web application for processing driver inspection reports with AI-powered handwritten remark detection and text extraction.

## Features

- **File Upload**: Support for PDF and image files (JPG, PNG)
- **AI Classification**: YOLOv8 model detects handwritten remarks
- **Text Extraction**: ChatGPT API extracts text from detected remarks
- **Dashboard**: Comprehensive view of all processed files with criticality levels
- **Database**: PostgreSQL storage for all records and processing results
- **CRUD Operations**: View, edit, and delete records

## Prerequisites

- Python 3.11.9
- PostgreSQL
- YOLOv8 model file (`best.pt`)

## Installation

1. **Clone or download the project files**

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate