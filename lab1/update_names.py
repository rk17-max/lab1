import os

with open(r"C:\Users\Rishit\.gemini\antigravity\scratch\devops_lab1\generate_docs.py", "r") as f:
    code = f.read()

# Replace file names with _with_screenshots.docx
old_names = [
    "Q1_Record_All_Commands.docx",
    "Q2_CICD_Workflow_Report.docx",
    "Q3_Automate_Application_Deployment.docx",
    "Q4_Install_and_Configure_Git_and_Jenkins.docx",
    "Q5_Setup_Version_Control_Git.docx",
    "Q6_Implement_Basic_Jenkins_Pipeline.docx",
    "Q7_Jenkinsfile_Pipeline_Stages.docx"
]

for name in old_names:
    new_name = name.replace(".docx", "_Submission.docx")
    code = code.replace(f'"{name}"', f'"{new_name}"')

with open(r"C:\Users\Rishit\.gemini\antigravity\scratch\devops_lab1\generate_docs.py", "w") as f:
    f.write(code)

print("Updated script to generate _Submission.docx files")
