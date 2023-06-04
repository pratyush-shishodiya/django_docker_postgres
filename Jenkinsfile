pipeline {
    agent any
    environment{
        GITHUB_CRED = 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
    }
    stages {
        stage('checkout'){
            steps{
                git([url: 'https://github.com/pratyush-shishodiya/django_docker_postgres.git', branch: 'master', credentialsId: 'GITHUB_CRED'])
            }
        }
        stage('Build') {
            steps {
                echo 'docker compose running'
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                // Your test steps here
                echo 'Testing done'
            }
        }
        stage('Deploy') {
            steps {
                // Your deployment steps here
                echo 'Deployed'
            }
        }
    }
}

