<<<<<<< HEAD
FROM python:3.9-alpine
WORKDIR /<github-repo>
ENV  MSG="Hello World!"
COPY . .
RUN pip3 install -r requirement.txt
EXPOSE 5000
=======
FROM python:3.9-alpine
WORKDIR /<github-repo>
ENV  MSG="Hello World!"
COPY . .
RUN pip3 install -r requirement.txt
EXPOSE 5000
>>>>>>> 362b2fc3fdaa515230f4e5c970b18a4f9a0824d0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]