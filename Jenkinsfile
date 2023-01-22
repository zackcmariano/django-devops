pipeline {
    agent any

    stages {
        stage ('Build Image - APP DJANGO') {
            steps {
                script {
                    dockerapp = docker.build("django-devops:v.${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }

        stage ('Push Image - Docker') {
            steps {
                docker.withRegistry('https://registry.hub.docker.com', 'hubdocker') {
                    dockerapp.push('latest')
                    dockerapp.push('${env.BUILD_ID}')          
                }

            }
        }
    } 
}