## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai_tools import PDFSearchTool, SerperDevTool

load_dotenv()

# The correct import paths for the tools
search_tool = SerperDevTool()
financial_document_reader_tool = PDFSearchTool()