FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install behave allure-behave
RUN pip install requests
RUN pip install behave
CMD ["behave", "--format=allure_behave.formatter:AllureFormatter", "--outfile=allure-results"]
