FROM selenium/standalone-chrome:3.141.59

# Install pip
RUN sudo apt-get update
RUN sudo apt-get -y install python3-pip

# Install Python dependencies and chromedriver package by current module of chrome installed
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

CMD exec python3 main.py --name=$NAME --password=$PASSWORD