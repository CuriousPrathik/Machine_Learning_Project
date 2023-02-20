# specify the python for the OS
FROM python 3.11

# copy all the files in app folder of OS, except the ones you want to ignore
COPY . /app 

# create a working directory
WORKDIR /app 

# install req.
RUN pip install -r requirements.txt

# create a port for the app to run
EXPOSE $PORT

# we will launch the app with the help of gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app