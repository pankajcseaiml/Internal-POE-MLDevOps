pipeline {
    agent any

    environment {
        PATH = "C:\\Users\\Pankaj\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;C:\\Users\\Pankaj\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\Pankaj\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;${env.PATH}"
        PYTHONPATH = "C:\\Users\\Pankaj\\AppData\\Roaming\\Python\\Python313\\site-packages"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling code from GitHub repository: https://github.com/pankajcseaiml/Internal-POE-MLDevOps'
                git branch: 'main', url: 'https://github.com/pankajcseaiml/Internal-POE-MLDevOps.git'
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
                bat 'python -m pytest -p no:dash -v -s tests/test_hello.py'
            }
        }

        stage('Evidently AI Monitoring') {
            steps {
                echo 'Running Evidently monitoring for Data Drift and Quality...'
                bat 'python evidently_monitor.py evidently_report.html'
            }
        }

        stage('Docker Build and Run') {
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
    }
}
