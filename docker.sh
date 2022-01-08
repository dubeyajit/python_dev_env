docker rmi -f python_dev
docker build -t python_dev .
docker rm -f python_dev_env
docker run -it --name python_dev_env -v /Users/sohan/projects/python_dev_env/workdir:/home/ajitdubey/workdir -p 5000:5000 python_dev