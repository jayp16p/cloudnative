# cloudnative
Cloud Native Monitoring Application
Python and How to create Monitoring Application in Python using Flask and psutil
How to run a Python App locally.
Learn Docker and How to containerize a Python application
Creating Dockerfile
Building DockerImage
Running Docker Container
Docker Commands
Create ECR repository using Python Boto3 and pushing Docker Image to ECR
Learn Kubernetes and Create EKS cluster and Nodegroups
Create Kubernetes Deployments and Services using Python!


## **Prerequisites** !

(Things to have before starting the projects)

- [x]  AWS Account.
- [x]  Programmatic access and AWS configured with CLI.
- [x]  Python3 Installed.
- [x]  Docker and Kubectl installed.
- [x]  Code editor (Vscode)

# ✨Let’s Start the Project ✨

## **Part 1: Deploying the Flask application locally**

### **Step 1: Clone the code**

Clone the code from the repository:

$ git clone <repository_url>


### **Step 2: Install dependencies**

The application uses the **`psutil`** and **`Flask`, Plotly, boto3** libraries. Install them using pip:

pip3 install -r requirements.txt


### **Step 3: Run the application**

To run the application, navigate to the root directory of the project and execute the following command:

$ python3 app.py


This will start the Flask server on **`localhost:5000`**. Navigate to [http://localhost:5000/](http://localhost:5000/) on your browser to access the application.

## **Part 2: Dockerizing the Flask application**

### **Step 1: Create a Dockerfile**

Create a **`Dockerfile`** in the root directory of the project with the following contents:

Use the official Python image as the base image
FROM python:3.9-slim-buster

Set the working directory in the container
WORKDIR /app

Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

Copy the application code to the working directory
COPY . .

Set the environment variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

Expose the port on which the Flask app will run
EXPOSE 5000

Start the Flask app when the container is run
CMD ["flask", "run"]


### **Step 2: Build the Docker image**

To build the Docker image, execute the following command:

$ docker build -t <image_name> .


### **Step 3: Run the Docker container**

To run the Docker container, execute the following command:

$ docker run -p 5000:5000 <image_name>


This will start the Flask server in a Docker container on **`localhost:5000`**. Navigate to [http://localhost:5000/](http://localhost:5000/) on your browser to access the application.

## **Part 3: Pushing the Docker image to ECR**

### **Step 1: Create an ECR repository**

Create an ECR repository using Python:

import boto3

Create an ECR client
ecr_client = boto3.client('ecr')

Create a new ECR repository
repository_name = 'my-ecr-repo' response = ecr_client.create_repository(repositoryName=repository_name)

Print the repository URI
repository_uri = response['repository']['repositoryUri'] print(repository_uri)


### **Step 2: Push the Docker image to ECR**

Push the Docker image to ECR using the push commands on the console:

$ docker push <ecr_repo_uri>:


## **Part 4: Creating an EKS cluster and deploying the app using Python**

### **Step 1: Create an EKS cluster**

Create an EKS cluster and add node group

### **Step 2: Create a node group**

Create a node group in the EKS cluster.

### **Step 3: Create deployment and service**

```jsx
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="568373317874.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)
make sure to edit the name of the image on line 25 with your image Uri.

Once you run this file by running “python3 eks.py” deployment and service will be created.
Check by running following commands:
kubectl get deployment -n default (check deployments)
kubectl get service -n default (check service)
kubectl get pods -n default (to check the pods)
Once your pod is up and running, run the port-forward to expose the service

kubectl port-forward service/<service_name> 5000:5000

#######SCREENSHOTS THAT MAY BE USEFUL, might save you hours of troubleshooting!

![image](https://github.com/jayp16p/cloudnative/assets/106398902/ba1ce0d3-5a71-4a69-bdd0-17e526650624)
Use the push commands to push docker image to ECR - see below
![image](https://github.com/jayp16p/cloudnative/assets/106398902/ed122d46-3649-4a9e-9192-3ab605346e33)

Once done it'll look like
![image](https://github.com/jayp16p/cloudnative/assets/106398902/c83c9b56-3ec0-4a1c-916b-a21d3a715bb4)
CREATE EKS clusters and roles,
![image](https://github.com/jayp16p/cloudnative/assets/106398902/fc169a84-06da-41ee-91c6-92093f98893d)
![image](https://github.com/jayp16p/cloudnative/assets/106398902/62ff4148-238c-4d45-814e-b09a67833997)

MAKE SURE SG has right inbound and outbound rules, inbound allow 5000

Add node group once cluster is up

![image](https://github.com/jayp16p/cloudnative/assets/106398902/864da54f-eecc-4a41-8847-6e7dc36341d8)

Create node groups
![image](https://github.com/jayp16p/cloudnative/assets/106398902/d231a57d-d8bc-4721-b626-874ae1e7eafa)
![image](https://github.com/jayp16p/cloudnative/assets/106398902/a9b28596-1e3e-443e-ac9a-582ca8f2a50a)


MAKE SURE TO RUN THIS BEFORE RUNNING EKS.py - change as necessary
aws eks update-kubeconfig --name cloud-native-cluster


![image](https://github.com/jayp16p/cloudnative/assets/106398902/9dffa8f3-4341-440a-8481-27e36dde1339)

![image](https://github.com/jayp16p/cloudnative/assets/106398902/f2fe58eb-cd31-4248-ae27-0cd089aa44f3)

![image](https://github.com/jayp16p/cloudnative/assets/106398902/bf879969-f550-4e33-8f37-0b259838cad7)

PORT FORWARD FOR IT TO WORK ON MY DEVICE

![image](https://github.com/jayp16p/cloudnative/assets/106398902/b9a82b37-8629-49db-b933-73a7a7a95cdf)


FINAL TEST

![image](https://github.com/jayp16p/cloudnative/assets/106398902/a5d82b62-588d-4842-9941-eb4878f8658a)











