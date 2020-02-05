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
                sh 'ansible-playbook ./playbooks/build-and-push-docker-image.yml'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "exit 1"
                }
            }
        }
        stage('Run Unit Tests Within Container'){
            steps {
                sh 'ansible-playbook ./playbooks/run-tests.yml'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "exit 1"
                }
            }
        }
        stage('Configure and Build Kubernetes Cluster'){
            steps {
                sh 'ansible-playbook ./playbooks/configure-k8s-cluster.yml'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "exit 1"
                }
            }
        }
        stage('Deploy updated image to cluster'){
            steps {
                sh 'sudo kubectl apply -f ./k8s-commands' // Bad idea but this is a demo and I'm lazy right :)
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "exit 1"
                }
            }
        }
    }
}