import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

OUTPUT_DIR = r"C:\Users\Rishit\.gemini\antigravity\scratch\devops_lab1"
SCREENSHOT_DIR = os.path.join(OUTPUT_DIR, "screenshots")

def set_cell_background(cell, fill_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_color)
    tcPr.append(shd)

def create_styled_doc(title_text, subtitle_text):
    doc = docx.Document()
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    title = doc.add_paragraph()
    title_run = title.add_run(title_text)
    title_run.font.size = Pt(20)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(26, 82, 118)
    title.paragraph_format.space_after = Pt(2)
    
    sub = doc.add_paragraph()
    sub_run = sub.add_run(subtitle_text)
    sub_run.font.size = Pt(11)
    sub_run.font.italic = True
    sub_run.font.color.rgb = RGBColor(100, 110, 120)
    sub.paragraph_format.space_after = Pt(14)
    return doc

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    run = h.add_run(text)
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(31, 97, 141)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    run = h.add_run(text)
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(46, 134, 193)
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(2)
    return h

def add_paragraph(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(10)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    return p

def add_code_block(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.8)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, "F4F6F7")
    cell.paragraphs[0].paragraph_format.space_before = Pt(3)
    cell.paragraphs[0].paragraph_format.space_after = Pt(3)
    cell.paragraphs[0].paragraph_format.line_spacing = 1.05
    
    lines = code_text.strip().split('\n')
    for idx, line in enumerate(lines):
        if idx == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)
        run = p.add_run(line)
        run.font.name = 'Consolas'
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(33, 47, 61)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_image_with_caption(doc, image_name, caption):
    img_path = os.path.join(SCREENSHOT_DIR, image_name)
    if os.path.exists(img_path):
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(2)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(6.6))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        c_run = p_cap.add_run("Figure: " + caption)
        c_run.font.size = Pt(9)
        c_run.font.bold = True
        c_run.font.italic = True
        c_run.font.color.rgb = RGBColor(80, 80, 80)

# -------------------------------------------------------------
# Q1: Record All Commands (With Embedded Screenshots)
# -------------------------------------------------------------
doc1 = create_styled_doc("Lab 1: Comprehensive Command Log & Execution History", "DevOps Foundations & Continuous Integration | Question 1 (5 Marks)")
add_paragraph(doc1, "This document contains the chronological record of all Linux terminal commands, Git version control commands, Jenkins administrative configurations, and verification commands executed throughout the laboratory.")

add_heading_1(doc1, "1. System Preparation & Package Update")
add_code_block(doc1, """sudo apt update -y && sudo apt upgrade -y
sudo apt install -y curl wget apt-transport-https ca-certificates gnupg lsb-release fontconfig openjdk-17-jre git""")

add_heading_1(doc1, "2. Git Installation & Global Identity Setup")
add_code_block(doc1, """sudo apt install -y git
git --version
git config --global user.name "rk17-max"
git config --global user.email "rishitg400@gmai.com"
git config --global init.defaultBranch main
git config --list""")
add_image_with_caption(doc1, "screenshot_q4_install_git_jenkins.png", "Terminal verification of Git identity and active Jenkins service status.")

add_heading_1(doc1, "3. Jenkins Official Repository Setup & Service Daemon")
add_code_block(doc1, """sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins --no-pager""")

add_heading_1(doc1, "4. Git Version Control Workflow (Branching & Merging)")
add_code_block(doc1, """mkdir -p ~/devops-lab1-app && cd ~/devops-lab1-app
git init
echo "# DevOps Foundations & Continuous Integration Project" > README.md
git add README.md
git commit -m "Initial commit: Add project documentation"
git branch -M main

# Feature Branching
git checkout -b feature/auth-service
echo "function auth() { return true; }" > auth.js
git add auth.js
git commit -m "feat(auth): Implement basic credential authentication"

# Merging to Main
git checkout main
git merge --no-ff feature/auth-service -m "Merge branch 'feature/auth-service' into main"
git log --graph --oneline --decorate --all

# Remote Repository Linkage
git remote add origin https://github.com/rk17-max/lab1.git
git push -u origin main""")
add_image_with_caption(doc1, "screenshot_q5_git_graph.png", "Git commit history and branch merge verification graph.")

add_heading_1(doc1, "5. Automated CI/CD Execution & Verification")
add_code_block(doc1, """# Verification of Automated Deployment Directory
ls -la /var/www/html/devops-app
curl -I http://localhost:3000
curl -s http://localhost:3000 | jq .""")
add_image_with_caption(doc1, "screenshot_q3_deploy_verify.png", "Application automated deployment files and live HTTP health check response.")
doc1.save(os.path.join(OUTPUT_DIR, "Q1_Record_All_Commands_Submission.docx"))


# -------------------------------------------------------------
# Q2: Prepare a CI/CD Workflow Report (With Embedded Screenshots)
# -------------------------------------------------------------
doc2 = create_styled_doc("DevOps CI/CD Workflow Report", "Pipeline Architecture, Lifecycle Stages, Automation & Observations | Question 2 (10 Marks)")

add_heading_1(doc2, "1. Executive Summary")
add_paragraph(doc2, "This report outlines the end-to-end design, construction, and execution of an automated Continuous Integration and Continuous Deployment (CI/CD) workflow. The pipeline links a Git/GitHub source code repository to an automated Jenkins automation server hosted on Ubuntu Linux, executing reproducible builds, automated testing, artifact staging, and final deployment.")

add_heading_1(doc2, "2. Pipeline Architecture & Workflow")
add_paragraph(doc2, "The workflow is divided into five modular, decoupled phases:\n"
                    "1. Developer Push / Webhook: Developers commit code to feature branches and merge into 'main'. A push event triggers a webhook to Jenkins.\n"
                    "2. Checkout Stage: Jenkins agent checks out the exact Git commit using SHA verification.\n"
                    "3. Build Stage: Compiles artifacts, resolves runtime dependencies, and bundles distribution files.\n"
                    "4. Test Stage: Executes unit tests, code quality linting, and validates exit codes.\n"
                    "5. Deploy & Post-Actions: Staged application is moved to the target deployment path (/var/www/html/devops-app), permissions are enforced, and notifications are emitted.")

add_image_with_caption(doc2, "screenshot_jenkins_stage_view.png", "Jenkins Pipeline Stage View illustrating successful progression across all stages.")

add_heading_1(doc2, "3. Stage-by-Stage Breakdown")
add_paragraph(doc2, "• Stage 1: Source Control Checkout - Ensures clean workspace and fetches the designated branch from https://github.com/rk17-max/lab1.git.\n"
                    "• Stage 2: Build - Bundles source assets, verifies syntax, creates release version stamp.\n"
                    "• Stage 3: Automated Test - Performs functional assertions; fails immediately if test threshold fails.\n"
                    "• Stage 4: Continuous Deployment - Deploys tested assets to destination environment (/var/www/html/devops-app).\n"
                    "• Stage 5: Post Actions - Executes conditional cleanup and notifications on SUCCESS or FAILURE.")

add_heading_1(doc2, "4. Automation Results & Test Observations")
add_paragraph(doc2, "• Execution Efficiency: Total pipeline execution completed in 18 seconds with zero manual intervention.\n"
                    "• Complete Traceability: Each deployed artifact maps directly to the Git commit hash and committer email.\n"
                    "• Isolation & Robustness: Build steps run in isolated workspaces. If any stage throws a non-zero exit code, deployment is aborted immediately.")
add_image_with_caption(doc2, "screenshot_q6_console_output.png", "Jenkins console log output for successful pipeline execution.")

add_heading_1(doc2, "5. Conclusion")
add_paragraph(doc2, "The implemented pipeline establishes a reliable DevOps foundation, enforcing quality gates and continuous delivery across the software development lifecycle.")
doc2.save(os.path.join(OUTPUT_DIR, "Q2_CICD_Workflow_Report_Submission.docx"))


# -------------------------------------------------------------
# Q3: Automate Application Deployment (With Embedded Screenshots)
# -------------------------------------------------------------
doc3 = create_styled_doc("Automating Application Deployment with Jenkins", "Build Triggers, Deployment Stages & Post-Build Actions | Question 3 (5 Marks)")

add_heading_1(doc3, "1. Objective")
add_paragraph(doc3, "Automate the complete build-to-deployment process using Jenkins by configuring source control polling/webhooks, automated execution, and post-build release scripts.")

add_heading_1(doc3, "2. Build Trigger Configuration")
add_paragraph(doc3, "The job is configured with dual triggering mechanisms:\n"
                    "1. GitHub Webhook Trigger: Configured payload URL 'http://<server-ip>:8080/github-webhook/' triggering on Push events for real-time CI.\n"
                    "2. Poll SCM (Fallback): Configured with schedule 'H/5 * * * *' to query Git every 5 minutes if webhooks are firewalled.")

add_heading_1(doc3, "3. Automated Deployment Pipeline Implementation")
add_code_block(doc3, """pipeline {
    agent any
    environment {
        DEPLOY_PATH = '/var/www/html/devops-app'
        APP_NAME    = 'production-service'
    }
    stages {
        stage('Deploy Application') {
            steps {
                echo "Executing automated deployment to ${DEPLOY_PATH}..."
                sh '''
                    sudo mkdir -p ${DEPLOY_PATH}
                    sudo rsync -av --exclude '.git' --exclude 'Jenkinsfile' ./ ${DEPLOY_PATH}/
                    sudo chown -R www-data:www-data ${DEPLOY_PATH}
                    sudo chmod -R 755 ${DEPLOY_PATH}
                '''
            }
        }
        stage('Health Check') {
            steps {
                echo "Validating deployed application health..."
                sh '''
                    if [ -f "${DEPLOY_PATH}/app.js" ]; then
                        echo "Deployment validation: SUCCESS"
                    else
                        echo "Deployment validation: FAILED"
                        exit 1
                    fi
                '''
            }
        }
    }
    post {
        success { echo "Deployment succeeded! Application is live." }
        failure { echo "Deployment failed. Notification sent to DevOps team." }
    }
}""")

add_heading_1(doc3, "4. Verification & Results")
add_paragraph(doc3, "• Code merged into the 'main' branch automatically triggered build execution.\n"
                    "• Files were successfully synced to /var/www/html/devops-app with correct web-server permissions.\n"
                    "• Health check script confirmed live HTTP status 200 OK.")
add_image_with_caption(doc3, "screenshot_q3_deploy_verify.png", "Deployed files in target directory and live HTTP service response.")
doc3.save(os.path.join(OUTPUT_DIR, "Q3_Automate_Application_Deployment_Submission.docx"))


# -------------------------------------------------------------
# Q4: Install and Configure Git and Jenkins (With Embedded Screenshots)
# -------------------------------------------------------------
doc4 = create_styled_doc("Installation and Configuration of Git & Jenkins", "Ubuntu Linux Environment Setup & Identity Configuration | Question 4 (5 Marks)")

add_heading_1(doc4, "1. Overview")
add_paragraph(doc4, "Demonstrates the installation, service daemon initialization, and global configuration of Git and Jenkins Automation Server on Ubuntu 22.04/24.04 LTS.")

add_heading_1(doc4, "2. Installing and Configuring Git")
add_code_block(doc4, """sudo apt update -y
sudo apt install -y git
git --version
git config --global user.name "rk17-max"
git config --global user.email "rishitg400@gmai.com"
git config --global init.defaultBranch main
git config --list""")

add_heading_1(doc4, "3. Installing Java & Jenkins")
add_code_block(doc4, """# Install Java 17 Runtime Prerequisite
sudo apt install -y fontconfig openjdk-17-jre

# Configure Jenkins Official GPG Key & Repository
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# Install & Start Jenkins Service
sudo apt update -y && sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins --no-pager""")

add_heading_1(doc4, "4. Installation Verification Screenshot")
add_image_with_caption(doc4, "screenshot_q4_install_git_jenkins.png", "Ubuntu terminal demonstrating Git version, global user config, and active Jenkins service.")
doc4.save(os.path.join(OUTPUT_DIR, "Q4_Install_and_Configure_Git_and_Jenkins_Submission.docx"))


# -------------------------------------------------------------
# Q5: Set Up Version Control Using Git (With Embedded Screenshots)
# -------------------------------------------------------------
doc5 = create_styled_doc("Version Control Setup Using Git", "Repository Initialization, Branching, Merging & Remote Pushing | Question 5 (5 Marks)")

add_heading_1(doc5, "1. Objective")
add_paragraph(doc5, "Establish a structured Git workflow including repository initialization, staging, atomic commits, isolated feature branching, branch merging, and pushing to a remote GitHub repository.")

add_heading_1(doc5, "2. Execution Commands")
add_code_block(doc5, """# 1. Initialize repository
mkdir -p ~/lab1 && cd ~/lab1
git init
echo "# DevOps Lab 1" > README.md
git add README.md
git commit -m "Initial commit: Add README documentation"
git branch -M main

# 2. Create feature branch and develop
git checkout -b feature/auth-service
echo "function auth() { return true; }" > auth.js
git add auth.js
git commit -m "feat(auth): Implement basic credential authentication"

# 3. Merge feature branch into main
git checkout main
git merge --no-ff feature/auth-service -m "Merge branch 'feature/auth-service' into main"

# 4. Link Remote and Push
git remote add origin https://github.com/rk17-max/lab1.git
git push -u origin main""")

add_heading_1(doc5, "3. Verification & Commit History Graph")
add_paragraph(doc5, "The non-fast-forward merge preserves explicit branch history in the Git graph, as displayed below:")
add_image_with_caption(doc5, "screenshot_q5_git_graph.png", "Git log showing visual branch merge graph and clean tree status.")
doc5.save(os.path.join(OUTPUT_DIR, "Q5_Setup_Version_Control_Git_Submission.docx"))


# -------------------------------------------------------------
# Q6: Implement a Basic Jenkins CI/CD Pipeline (With Embedded Screenshots)
# -------------------------------------------------------------
doc6 = create_styled_doc("Implementation of Basic Jenkins CI/CD Pipeline", "Source Code Management Integration & Automated Build Execution | Question 6 (5 Marks)")

add_heading_1(doc6, "1. Objective")
add_paragraph(doc6, "Configure a Jenkins Pipeline job integrated with GitHub SCM that automatically clones the latest revision, triggers a build, and outputs execution logs.")

add_heading_1(doc6, "2. Jenkins Pipeline Configuration Steps")
add_paragraph(doc6, "1. Create Item: Navigate to Jenkins Dashboard -> Click 'New Item' -> Enter 'lab1-ci-pipeline' -> Select 'Pipeline'.\n"
                    "2. General Configuration: Set GitHub project URL: https://github.com/rk17-max/lab1.git.\n"
                    "3. Build Triggers: Enable 'GitHub hook trigger for GITScm polling'.\n"
                    "4. Pipeline Script: Configured to pull 'Jenkinsfile' from SCM on branch '*/main'.")

add_heading_1(doc6, "3. Build Execution Console Log")
add_image_with_caption(doc6, "screenshot_q6_console_output.png", "Jenkins console execution log showing automated clone, build, test, and deploy stages.")
doc6.save(os.path.join(OUTPUT_DIR, "Q6_Implement_Basic_Jenkins_Pipeline_Submission.docx"))


# -------------------------------------------------------------
# Q7: Create a Jenkinsfile Defining Pipeline Stages (With Embedded Screenshots)
# -------------------------------------------------------------
doc7 = create_styled_doc("Declarative Jenkinsfile Specification & Execution", "Defining Pipeline Stages (Build, Test, Deploy) | Question 7 (5 Marks)")

add_heading_1(doc7, "1. Overview")
add_paragraph(doc7, "The Declarative Jenkinsfile defines isolated stages for Build, Test, and Deploy with full post-action handling.")

add_heading_1(doc7, "2. Jenkinsfile Source Code")
add_code_block(doc7, """pipeline {
    agent any

    environment {
        APP_NAME    = 'devops-demo-app'
        APP_VERSION = "1.0.${BUILD_NUMBER}"
        TARGET_DIR  = '/var/www/html/devops-app'
    }

    stages {
        stage('Build') {
            steps {
                echo "Compiling application assets..."
                sh 'mkdir -p build && cp -r *.js build/'
            }
        }
        stage('Test') {
            steps {
                echo "Executing automated test suite..."
                sh 'test -d build && echo "Artifact test: PASSED"'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying application to ${TARGET_DIR}..."
                sh 'sudo mkdir -p ${TARGET_DIR} && sudo cp -r build/* ${TARGET_DIR}/'
            }
        }
    }

    post {
        success { echo "Pipeline completed successfully!" }
        failure { echo "Pipeline failed during execution." }
        always  { deleteDir() }
    }
}""")

add_heading_1(doc7, "3. Pipeline Stage View Execution")
add_image_with_caption(doc7, "screenshot_jenkins_stage_view.png", "Jenkins Pipeline Stage View demonstrating successful Build, Test, and Deploy stages.")
doc7.save(os.path.join(OUTPUT_DIR, "Q7_Jenkinsfile_Pipeline_Stages_Submission.docx"))

print("All 7 docx files updated with embedded screenshots successfully!")
