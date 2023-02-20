# Machine_Learning_Project

**Real World END-To-END Project that includes MLOP'S**

Advantage of Git

    Git is a widely used distributed version control system (VCS) that provides a number of advantages to software development teams. 

    Distributed Development: Each developer has their own copy of the repository. This allows for more flexibility and reduces the risk of losing work.

    Branching and Merging: Git allow developers to work on different features and bug fixes simultaneously.

    Integration with Other Tools: Git can be integrated with many other development tools, such as continuous integration and deployment systems, bug tracking tools, and code review tools. This makes it easy to automate and streamline the development process.

CI - Continuous Integration is the practice of automating the integration of frequent code changes/commits from multiple contributors into a single software project.

CD - Continuous Deployment/Delivery is the practice where code changes are automatically prepared for a release to production.

Git Branches

    Main Branch - main branch is the primary branch in a VCS that typically represents the latest stable version of the software. It is where the production-ready code resides.

    Integration Branch - An integration branch is a shared branch in a version control system (VCS) where changes from multiple development branches are merged and tested together, before merging in the main branch.
    
    Sub Branches - Developers typically work on their own development branches and integrate their changes into the integration branch for testing and review before merging into the main branch.

Docker - Docker is a platform for building, shipping, and running applications in containers. Containers allow applications to run in isolated environments, making them portable and easy to deploy across different environments.

    Portability:

    Scalability: Docker containers can be easily scaled up or down

    Resource efficiency: Docker containers use fewer resources compared to virtual machines.

    Isolation: Docker containers provide an isolated environment for applications, reducing the risk of conflicts or interference with other applications or the host system.

    Version control: Docker images can be versioned, allowing for easy rollbacks or updates to the application. 

    Install docker

    run the docker pull command of the docker image

    image will be downloaded, which contains all the files

    once you run the image code you can acsess all the files

    To create a Docker image, you can follow these general steps:

        Write a Dockerfile: A Dockerfile is a script that contains instructions for building the image. It specifies the base image, adds any required files and dependencies, and sets up the environment.

        Build the image: Once you have written the Dockerfile, use the docker build command to build the image. The command takes the Dockerfile as input and creates an image based on the instructions in the file.

        Create a dockerfile with the name “Dockerfile”, “.dockerignore”, we need

Create Conda venv

    conda create -p venv python -y

Activate venv

    in cmd type conda activate venv/ 

Git Commands for CI

    git status - This command lists all the files that have to be committed.

    git add [file] - This command adds a file to the staging area.

    git add */. - This command adds one or more to the staging area.

    git log - This command is used to list the version history for the current branch.

    git commit -m "commit msg" - This command records the file permanently in the version history.

    git push [variable name] [branch] - This command sends the branch commits to your remote repository.


CD in Heroku, we need 3 things:

    Email id
    API key
    APP name

Create a dockerfile with name "Dockerfile" and mention the protocall

Build docker image

    docker build -t <imagename>:<tagname> .

    > Note: Image name for docker image always in small

See list of docker images

    docker images

Run docker image

    docker run -p 5000:5000 -e PORT=5000 <Image ID>

Check running containers

    docker ps

To stop docker container

    docker stop <container_id>

Once we can run this in our system we can upload this to cloud and create a CD pipeline.