# Flask container app in Docker

A simple Flask application developed to be deployed inside a Docker container.

## Instructions
1. Clone the repository to your local machine.
> `git clone` [`https://github.com/santiadlv/flask-container.git`](https://github.com/santiadlv/flask-container.git)
2. Move to the project directory.
> `cd flask-container`
3. After starting the Docker daemon, build the image and tag it.
> `docker build -t flask-login .`
4. Create and run a new container based on the built image in detached mode, exposing the needed port for communication and subsequently naming it.
> `docker run -d -p 5000:5000 --name login-container flask-login`
5. Visit `localhost` in port `5000` to interact with the application.
> http://localhost:5000/
6. When done, stop the container and remove it from the system.
> `docker stop login-container`
>
> `docker rm login-container`
7. Optionally, remove generated image as well to avoid storage clutter.
> `docker rmi flask-login`