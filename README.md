### Setting up your environment

```
virtualenv api-env
source api-env/bin/activate
pip install -r requirements.txt
```

### Running the server

```
python app.py
``


### Building Docker Image

```
docker build -t beaten-track .
docker run -p 8000:8000 beaten-track

aws ecr get-login --region eu-west-1
docker tag beaten-track:latest 740465614213.dkr.ecr.eu-west-1.amazonaws.com/beaten-track:latest
docker push 740465614213.dkr.ecr.eu-west-1.amazonaws.com/beaten-track:latest

````
