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
        sudo docker build /home/jenkins/workspace/job-node-02 -t George-Build
        sudo docker run -p 8000:5000 George-build'''
      }
    }
      
    }
    post {
		always {
			sh 'sudo docker logout'
		}
	}
}
