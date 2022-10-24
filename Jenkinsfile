pipeline {
  agent any
  stages {
    stage('Checkout Scm') {
      steps {
        git 'https://github.com/GeorgeBeasley/my-project'
      }
    }

    stage('Shell script 0') {
      steps {
        sh '''sudo docker rm -f $(sudo docker ps -a -q)
sudo docker build /home/jenkins/workspace/job-node-02 -t jenkins-build
sudo docker run -p 8000:5000 jenkins-build'''
      }
    }

  }
}
