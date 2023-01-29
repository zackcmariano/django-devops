pipeline {
    agent any

    environment {

        PROJECT_ID = 'terra-analytics-374723'
        CLUSTER_NAME = 'jenk-gke'
        LOCATION = 'us-central1-a'
        CREDENTIALS_ID = 'gcp-kube'
    }

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
            }
            steps {
                withKubeConfig ([credentialsId: 'kubeconfig']) {
                    sh 'kubectl apply -f ./k8s/deployment.yaml'
                }
            } */

            steps {
                environment {
                tag_version = "version.${env.BUILD_ID}"
                }

                echo "Deployment started ..."
                sh 'ls -ltr'
                sh 'pwd'
                sh "sed -i 's/{{tag}}/$tag_version/g' ./k8s/deployment.yaml"
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: './k8s/deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
                echo "Deployment Finished"
            }
        }

    } 
}