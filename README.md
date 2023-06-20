# WeatherForecast

### Initialization command: 
Build image in local
$`docker image build -t flask_docker .` <br />
Run the image
$`docker run -p 5000:5000 -d flask_docker` <br />
Check the Dockerfile to start the app. <br />
Use Docker Desktop to overview and manage all containers and images. 

### Local test:
run Python file to test
$`FLASK_APP=app flask run` <br />
Edit requirements.txt to add more dependencies.

### Deployment(to Hub):
First, create a repo in Docker Hub <br/>
Then in the local terminal, run: `docker login -u YOUR-USER-NAME` to login <br/>
Next, tag the local image to rename: `docker tag local-name YOUR-USER-NAME/new-name` <br/>
Finally, push: `docker push YOUR-USER-NAME/new-name` <br/>

https://docs.docker.com/get-started/04_sharing_app/
### Deployment (host web app):
Add gunicorn into the requirements.txt, then create a new empty repo and push files to it. <br/>
Set the repo as remote, and then use DigitalOcean to access the repo and then build and deploy. <br/>
https://docs.digitalocean.com/tutorials/app-deploy-flask-app/

Remote repo: https://github.com/Leo-rq-yu/weather-forecast.git

Website: https://stingray-app-i8a35.ondigitalocean.app/
