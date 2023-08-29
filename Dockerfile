FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["behave", "--format=allure_behave.formatter:AllureFormatter", "--outfile=allure-results"]
