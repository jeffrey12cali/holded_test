# Introduction
Holded_test is a django-based app which its main function is to download salesorders and contact data in xlsx format from a Holded project consuming the [Holded API](https://developers.holded.com/reference/api-key).

# Installation
## Required Software
* **Git**: Download and install it from https://github.com/git-guides/install-git
* **Docker**: Download and install it from https://www.docker.com/get-started/

## Clone this repository
On you command line use git to clone this repository into your local machine.

    git clone https://github.com/jeffrey12cali/holded_test.git

## Create .env file
Once you are in the root of the respository directory you need to create a new file called `.env` within the folder `./holded_test/`. As a reference, in this folder you can see files such as `manage.py` or `.gitignore`.

This new file will contain the project API KEY. The `.env` file should have this same structure, where you will `YOUR_API_KEY_HERE` with the Holed API KEY.

    HOLDED_API_KEY=YOUR_API_KEY_HERE
    
 ## Get Python Image for Docker
 Run the following command to get the Python image needed to build the app image.
 
    docker pull python
    
 In case you get a *permission denied* error, if you are in a Linux based system you should use the `sudo` command.
 
## Build Docker Image
In the command line go to the root of the repository, where you can see files such as `Dockerfile` or `requirements.txt`. Once there execute the following command to build the Docker Image containing all necesary software to run the application. 

    docker build --tag holded-test .

## Run Docker Image in a new container
Execute the following command to run the aplication over a new container based on the image previously build. The container will communicate with our local machine through port `8000`.

    docker run --publish 8000:8000 holded-test

# Usage
## Start/stop containers
First of all you need to identificate the container. This command will list you all the containers that has holded-test as image.

    docker container ls -a --filter ancestor="holded-test"
    
Locate the `CONTAINER ID` column. This will be the identifier for start or stop the containers.

    docker start <CONTAINER ID>
    
    docker stop <CONTAINER ID>
    
## Get the xlsx file
Now that the container is running. Go to your web browser and access this url http://127.0.0.1:8000/download/xlsx.
