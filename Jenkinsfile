pipeline {
    agent any

    stages {
        stage ('Build Image - APP DJANGO') {
            steps {
                script {
                    dockerapp = docker.build("registry.gitlab.com/zackcmariano/django-devops:devops", '-f ./Dockerfile ./')
                }
            }
        }
    } 
}