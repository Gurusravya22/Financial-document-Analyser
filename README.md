# Financial Document Analyzer

## Project Overview

This project is a comprehensive AI-powered financial document analysis system. It processes corporate reports, financial statements, and other investment documents using a multi-agent framework to provide structured, actionable insights. The system is designed to analyze documents, identify key financial metrics, assess risks, and generate strategic investment recommendations.

***

## Getting Started

### 1. Install Required Libraries

First, install all necessary libraries from the `requirements.txt` file.

```sh
pip install -r requirements.txt

README.md
This is the README.md file you can use for your project submission. It is formatted to meet all your requirements, including an overview of the project, setup instructions, and a detailed explanation of the bugs you found and fixed.

Markdown

# Financial Document Analyzer



## Getting Started


2. Setup API Keys
This project requires an OpenAI API key for the AI models and a Serper API key for search functionality.

Create a .env file in the root directory of your project.

Add your API keys to the file in the following format:
OPENAI_API_KEY=your_openai_key_here
SERPER_API_KEY=your_serper_key_here
3. Run the Application
Start the FastAPI server from your terminal using the following command:
uvicorn main:app --reload
The server will start at http://localhost:8000.
4. Use the API
Open your web browser and go to http://localhost:8000/docs to access the interactive API documentation. You can use the /analyze endpoint to:

Upload a financial document (PDF).

Provide a query for the AI to analyze.

The API will return a structured JSON response with a detailed analysis.
Bugs Found and How They Were Fixed
The initial project had several critical bugs that prevented it from running. Here is a summary of the issues and the implemented solutions
Bug Description	Fix Implemented

ImportError: cannot import name...	The tools.py file had incorrect import paths for crewai_tools. The file was updated to use the correct from crewai_tools import PDFSearchTool, SerperDevTool syntax.

ValidationError	The agents.py file was attempting to pass Python function definitions directly to the Agent's tools list. The tools.py file was corrected to instantiate the tools as objects (PDFSearchTool() and SerperDevTool()), and these instances were then correctly imported and passed to the agent.

KeyError : 'OPENAI_API_KEY'	The PDFSearchTool was unable to find the OpenAI API key, as it was not set in the environment. The fix involved creating a .env file and adding OPENAI_API_KEY=your_key to allow python-dotenv to load the key correctly.
500 Internal Server Error:	The PDFSearchTool was being initialized without a file path, causing a server crash when the agent tried to use it. The main.py file was refactored to dynamically create the PDFSearchTool with the temporary file path of the uploaded document, ensuring the tool always has a file to analyze.

Outdated Dependency Versions:	The original requirements.txt file had outdated and conflicting dependencies, particularly with onnxruntime. The requirements.txt was updated with compatible versions of all necessary libraries to ensure a stable working environment.

Asynchronous Function Mismatch:	The run_crew function in main.py was not properly awaited. The function call was updated to await run_crew to handle asynchronous operations correctly, a requirement for working with fastapi.
### **API Documentation**

The project's API is documented to help users understand its functionality and how to interact with it.

***

### **Endpoint: `/analyze`**

* **URL:** `http://localhost:8000/analyze`
* **Method:** `POST`
* **Description:** This endpoint processes an uploaded financial document, performs a comprehensive AI analysis, and returns a structured report with key financial insights.
* **Parameters:**
    * `file` (required): An uploaded PDF file (`multipart/form-data`).
    * `query` (optional): A string to specify the user's specific analysis request. The default query is "Analyze this financial document for investment insights".
* **Response:**
    * **Success (200 OK):** Returns a JSON object containing the status, the query, the name of the processed file, and the full analysis report in a structured Markdown format.
        * `status`: "success"
        * `query`: The query used for the analysis.
        * `analysis`: A multi-section report with a summary of financial health, key metrics, risks/opportunities, and investment recommendations.
        * `file_processed`: The filename of the uploaded document.
    * **Error (500 Internal Server Error):** Returns a JSON object with an error message.
        * `detail`: A description of the error that occurred during processing.

