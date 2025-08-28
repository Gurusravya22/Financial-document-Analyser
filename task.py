from crewai import Task
from agents import financial_analyst

# Define a task for analyzing the financial document
analyze_financial_task = Task(
    description=(
        "1. Read the provided financial document at {file_path}. "
        "2. Analyze the document thoroughly using the available tools to extract key financial metrics, identify risks, and uncover opportunities. "
        "3. Based on your analysis, answer the user's query: '{query}'. "
        "4. Synthesize your findings into a comprehensive report. Provide structured results including: "
        "- A concise summary of the company's financial health. "
        "- Key financial ratios or figures (e.g., revenue, net income, debt-to-equity ratio). "
        "- A detailed list of identified risks and opportunities. "
        "- Two to three clear, actionable investment recommendations based on the data. "
    ),
    expected_output=(
        "A structured, professional report in Markdown format. The report should have the following sections: "
        "## Summary of Financial Health "
        "(A 1-2 paragraph summary) "
        "## Key Financial Metrics "
        "(A bulleted or table-based list of key figures) "
        "## Risks and Opportunities "
        "(Bulleted lists for each category with brief explanations) "
        "## Investment Recommendations "
        "(A numbered list of 2-3 specific recommendations with justifications) "
    ),
    agent=financial_analyst
)