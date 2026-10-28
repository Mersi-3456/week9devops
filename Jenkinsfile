pipeline {
agent any

environment {
    IMAGE_NAME = 'mersineelakantam/week8-registration'
    IMAGE_TAG = 'latest'
}

stages {
    stage('Checkout') {
        steps {
            checkout scm
            echo 'Source code checked out.'
        }
    }

    stage('Build Docker Image') {
        steps {
            bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
        }
    }

    stage('Docker Login') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASSWORD'
            )]) {
                powershell '''
                    $env:DOCKER_PASSWORD | docker login -u $env:DOCKER_USER --password-stdin
                    if ($LASTEXITCODE -ne 0) {
                        exit $LASTEXITCODE
                    }
                '''
            }
        }
    }

    stage('Push Docker Image') {
        steps {
            bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
        }
    }

    stage('Deploy to Kubernetes') {
        steps {
            bat 'kubectl apply -f deployment.yaml'
            bat 'kubectl apply -f service.yaml'
        }
    }

    stage('Verify Deployment') {
        steps {
            bat 'kubectl get deployments'
            bat 'kubectl get pods'
            bat 'kubectl get services'
        }
    }
}

post {
    success {
        echo 'Week 8 pipeline completed successfully!'
    }
    failure {
        echo 'Pipeline failed. Check the Jenkins console output.'
    }
}

}
