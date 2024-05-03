pipeline {
    agent any

    stages {
        stage('Get Code') {
            steps {
                //Obtener el código del repositorio
                git 'https://github.com/Alex201666/UNIR.git'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Ey, esto es python y no hay que compilar nada'
                echo WORKSPACE
                sh 'ls -l'
            }
        }
        
        stage('Test'){
            parallel{
                
                stage('Unit') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
                            sh '''
                                export PYTHONPATH=.
                                pytest --junitxml=result-unit.xml test/unit
                            '''
                        }
                    }
                }
                
                stage('Rest') {           
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE'){
                            sh '''
                            export FLASK_API=app/api.py
                            flask run --port=5001 &
                            java -jar /home/alex/Escritorio/UNIR/test/wiremock/wiremock-standalone-3.5.4.jar --port=9090 --root-dir test/wiremock
                            export PYTHONPATH=.
                            pytest --junitxml=result-rest.xml test/rest
                            '''
                        }
                    }
                }
            }
        }
        stage('Results') {
            steps {
                junit 'result*.xml'
                echo 'FINALIZADO' 
            }
        }
    }
}
