From python:3.8.2-alpine
WORKDIR /API
ADD . /API
RUN pip install --upgrade setuptools 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python","app.py" ]