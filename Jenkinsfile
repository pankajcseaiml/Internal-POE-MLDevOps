pipeline {
    agent any

    environment {
        PYTHON_EXEC = 'python'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling code from GitHub repository: https://github.com/pankajcseaiml/Internal-POE-MLDevOps'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing required Python dependencies...'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Running Pytest test case for hello.py...'
                bat 'python -m pytest -v -s tests/test_hello.py'
            }
        }

        stage('Evidently AI Monitoring') {
            steps {
                echo 'Running Evidently monitoring for Data Drift and Quality...'
                bat 'python evidently_monitor.py evidently_report.html'
            }
        }

        stage('Docker Build and Run (Optional)') {
            steps {
                script {
                    echo 'Building and running lightweight Python Docker image...'
                    catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                        bat 'docker build -t hello-mlops:latest .'
                        bat 'docker run --rm hello-mlops:latest'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Archiving test results and Evidently monitoring report...'
            archiveArtifacts artifacts: 'evidently_report.html', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline encountered failures.'
        }
    }
}
