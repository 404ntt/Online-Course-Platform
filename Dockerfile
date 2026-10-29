FROM python:3.14.4-slim
WORKDIR /app
COPY /home/n404nt/online-course-work /app/online_platform
ENTRYPOINT [ "python3", "manage.py", "runserver" ]