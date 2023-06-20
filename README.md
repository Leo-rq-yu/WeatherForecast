# WeatherForecast

### Initialization command: 
Build image in local
`docker image build -t flask_docker .` <br />
Run the image
`docker run -p 5000:5000 -d flask_docker` <br />
Check the Dockerfile to start the app. <br />
Use Docker Desktop to overview and manage all containers and images. 

### Local test:
run Python file to test
`python app.py` <br />
Edit requirements.txt to add more dependencies.

### Deployment:
Used fly.io to deploy this Flask app. config settings in the fly.toml file. <br />
To launch the app to the server: 
`fly launch` <br />
To check the app's status:
`fly status` <br />
To see the web app page:
`fly open \<args>` <br />

To see the full tutorial:
https://fly.io/docs/hands-on/
