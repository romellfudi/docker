pipeline {
    agent {
        label "main"
    }

    tools {nodejs "nodejs"}
    
    stages {
        stage('clean workspace') {
            steps {
                sh 'rm -rf webdriveio/'
            }
        }
        stage('Clone repository') {
            steps {
                sh 'git clone https://github.com/romellfudi/webdriveio'
                }
        }
        stage('Install npm dependencies') {
            steps {
                dir('webdriveio') {
                    sh 'npm install'
                }
            }
        }
        stage('Run testing cases') {
            steps {
                dir('webdriveio') {
                    sh 'npm run wdio'
                }
            }
        }
    }
}
