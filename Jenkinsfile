node {
    stage('Preparation') {
        deleteDir()
        checkout scm
        sh 'git submodule update --init --recursive'
        env.GIT_URL = sh(returnStdout: true, script: 'git config --get remote.origin.url').trim()
        env.GIT_BRANCH = sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
        env.GIT_COMMIT = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
        def workspace = pwd()
        sh '''if [ ! -d "venv" ]; then
            python -m venv venv
        fi'''
        sh "source venv/bin/activate"
        sh "pip install --upgrade pip"
        sh "pip install -r requirements.txt"
        sh "python manage.py makemigrations"
        sh "python manage.py migrate"
    }

    stage('Test') {
        sh "python manage.py test"
    }

}