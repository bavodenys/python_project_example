FROM python:3.9
COPY /example /example
COPY /bade /bade
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /example
ENTRYPOINT ["python", "example.py"]
# To build the container: docker build -t imagename .
# Example: docker build -t "speedconversion" .
# To run this container: docker run imagename --speed=x
# Example: docker run badebade/speedconversion --speed=10
