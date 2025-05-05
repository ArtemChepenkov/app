node {

     stage('Checkout') {
        checkout scm
    }

    stage('Build Docker Image') {
        docker.build("artemchepenkov/third-hw:latest")
    }

    stage('Push Docker Image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            docker.image("artemchepenkov/third-hw:latest").push()
        }
    }

    stage('Post Actions') {
        if (currentBuild.currentResult == 'SUCCESS') {            
	    currentBuild.description = "Docker image pushed successfully. To pull the image, run: docker pull artemchepenkov/third-hw:latest"
        }
	cleanWs()
    }
}
