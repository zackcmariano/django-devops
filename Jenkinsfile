pipeline {
    agent any

    stages {
        stage ('Build Image - APP DJANGO') {
            steps {
                script {
                    dockerapp = docker.build("zackcmariano/django-devops:version.${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }

        stage ('Push Image - Docker') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        dockerapp.push('latest')
                        dockerapp.push("version.${env.BUILD_ID}")          
                    }
                }
            }
        }

        stage ('Deploy Kubernetes') {
            /*environment {
                tag_version = "version.${env.BUILD_ID}"            
            }
            steps {
                sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                sh 'kubectl apply -f ./k8s/deployment.yaml'
                withKubeConfig([credentialsId: 'kubeconfig']) {
                    sh 'sed -i "s/{{tag}}/$tag_version/g" ./k8s/deployment.yaml'
                    sh 'kubectl apply -f ./k8s/deployment.yaml'
                }
            }*/
            steps {
                withKubeConfig ([credentialsId: 'kubeconfig']) {
                    sh 'sudo -p "Manu101018" kubectl apply -f ./k8s/deployment.yaml'
                }
            }
        }

    } 
}