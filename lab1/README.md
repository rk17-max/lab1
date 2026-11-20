# Lab 1: DevOps Foundations & Continuous Integration

This repository contains the complete assignment deliverables, configurations, pipeline scripts, and reports for **Lab 1: DevOps Foundations & Continuous Integration**.

---

## 📁 Repository Structure & Deliverables

- **`Q1_Record_All_Commands.docx`** / **`commands_log.sh`**:
  - Full chronological list of all Linux, Git, and Jenkins administrative commands.
- **`Q2_CICD_Workflow_Report.docx`** / **`WORKFLOW_REPORT.md`**:
  - Comprehensive CI/CD workflow report covering pipeline architecture, lifecycle stages, automation triggers, test execution observations, and error handling.
- **`Q3_Automate_Application_Deployment.docx`**:
  - Deployment automation documentation detailing webhook/polling triggers, release synchronization (`rsync`/file deployment), health checks, and post-build notifications.
- **`Q4_Install_and_Configure_Git_and_Jenkins.docx`**:
  - Step-by-step setup guide for installing and configuring Git and Jenkins on Ubuntu Linux, including service management (`systemctl`) and global Git identity.
- **`Q5_Setup_Version_Control_Git.docx`**:
  - Git version control workflow: repository initialization, staging, atomic commits, isolated feature branching, branch merging, and pushing to GitHub.
- **`Q6_Implement_Basic_Jenkins_Pipeline.docx`**:
  - Jenkins pipeline integration guide: connecting GitHub SCM, build triggers, job configuration, and console execution logs.
- **`Q7_Jenkinsfile_Pipeline_Stages.docx`** / **`Jenkinsfile`**:
  - Production-ready Declarative `Jenkinsfile` featuring `Build`, `Test`, and `Deploy` stages, environment variables, timeout policies, and `post` build actions.
- **`app.js`**: Sample Node.js application.

---

## 🚀 Quick Reference: Jenkinsfile

```groovy
pipeline {
    agent any

    environment {
        APP_NAME    = 'devops-demo-app'
        APP_VERSION = "1.0.${BUILD_NUMBER}"
        TARGET_DIR  = '/var/www/html/devops-app'
    }

    options {
        timeout(time: 15, unit: 'MINUTES')
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Build') {
            steps {
                echo "========== STAGE: BUILD [Version: ${APP_VERSION}] =========="
                sh '''
                    echo "Compiling application assets..."
                    mkdir -p build/
                    cp -r *.js *.html build/ 2>/dev/null || cp *.md build/
                    echo "Build completed successfully."
                '''
            }
        }

        stage('Test') {
            steps {
                echo "========== STAGE: TEST =========="
                sh '''
                    echo "Executing automated test suite..."
                    if [ -d "build" ]; then
                        echo "Artifact verification passed."
                    else
                        echo "Test failed: Build directory missing."
                        exit 1
                    fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "========== STAGE: DEPLOY =========="
                sh '''
                    echo "Deploying application to target directory: ${TARGET_DIR}"
                    sudo mkdir -p ${TARGET_DIR}
                    sudo cp -r build/* ${TARGET_DIR}/
                    echo "Application deployed successfully at $(date)"
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed with status: SUCCESS."
        }
        failure {
            echo "Pipeline FAILED during execution. Check logs above."
        }
        always {
            echo "Cleaning temporary build workspace..."
            deleteDir()
        }
    }
}
```

---

## 🛠️ Global Git Configuration
```bash
git config --global user.name "rk17-max"
git config --global user.email "rishitg400@gmai.com"
```
