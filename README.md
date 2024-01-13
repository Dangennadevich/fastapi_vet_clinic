# fastapi_vet_clinic
Higher School of Economics: MOVS - FastAPI Tutorial Project

This is a educational project from HSE (4Q23).

Service for a veterinary clinic

The director of the veterinary clinic turned to us and said:
"The clinic needs a microservice for storing and updating information for dogs!"
The director talked to the IT department, and they compiled documentation in the OpenAPI format.

To open it, we need:<br> 
● Download <a href="https://drive.google.com/file/d/1qtHEGCl2gpLxOR7CJPOC40tHp4hwYL5_/view">file</a> with its description in YAML format <br> 
● Open [Swagger Editor](https://editor-next.swagger.io)<br> 
● upload the contents of the file to the left side <br> 
Our goal is to implement the described microservice!

important: We use a blank <a href="https://drive.google.com/file/d/14wEjgs97V9im6zHZo3JIwU8rTsus0cI4/view">main.py</a> to work on a task



The next task was to compile a docker container

https://drive.google.com/file/d/1ZQMPWCCQTC3WgtZCLH4C1OQ_EX-Cc4qK/view

container here:
https://hub.docker.com/r/dangennadevich/movs

TAG: fastapi_vet_clinic

Terminal

docker pull dangennadevich/movs:fastapi_vet_clinic

docker run -p 5555:8005 8536b076784c

Open in a web

http://localhost:5555/

http://localhost:5555/docs
