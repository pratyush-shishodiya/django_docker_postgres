#Python base-image
FROM --platform=linux/arm64/v8 python:3.10.2-slim-bullseye

#Directory in container
#RUN mkdir /django_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#workdirectory in container
WORKDIR /django_app

#Upgrade pip
RUN pip install --upgrade pip

#Copying requirement in container
COPY /requirements.txt /django_app

#Changing permission
RUN chmod +x requirements.txt

#Installing all the requirement
RUN pip install -r requirements.txt

#copying source code
COPY ./ ./

CMD ["python", "manage.py runserver 0.0.0.0:8000"]
