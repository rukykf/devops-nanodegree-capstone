pipeline {
    agent any
    stages {
       stage('Lint Html'){
           steps {
               sh 'tidy -q -e ./src/html-for-linting.html'
           }
       }
       stage('Build and Push Docker Image') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                   sh 'ansible-playbook ./playbooks/build-and-push-docker-image.yml'
                }
            }
        }
        stage('Run Unit Tests Within Container'){
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'ansible-playbook ./playbooks/run-tests.yml'
                }
            }
        }
        stage('Configure and Build Kubernetes Cluster'){
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'ansible-playbook ./playbooks/configure-k8s-cluster.yml'
                }
            }
        }
        stage('Deploy updated image to cluster'){
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                   sh 'sudo kubectl apply -f ./k8s-commands' // Bad idea but this is a demo and I'm lazy right :)
                }
            }
        }
    }
}