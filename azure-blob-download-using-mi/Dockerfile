FROM python:3.8

RUN mkdir /application
WORKDIR "/application"

# Upgrade pip
RUN pip install --upgrade pip

# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ADD requirements.txt /application/
ADD app/main.py /application/

# RUN echo "Setting Up Python environment.."
# RUN pip install pip==21.3.1

RUN pip install -r /application/requirements.txt

CMD [ "python", "main.py" ]