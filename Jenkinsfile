pipeline {
    agent any

    stages {
        stage ('Build Image - APP DJANGO') {
            steps {
                script {
                    dockerapp = docker.build("registry.gitlab.com/zackcmariano/django-devops:devops.${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }

        stage ('Push Image - Docker') {
            steps {
                docker.withRegistry('https://gitlab.com/zackcmariano/django-devops/container_registry/2478017', 'gitlab') {
                    dockerapp.push('latest')
                    dockerapp.push('${env.BUILD_ID}')          
                }

            }
        }
    } 
}