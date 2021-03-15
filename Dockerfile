FROM python

RUN pip install openapi-python-client

RUN printf "\nYou can change me! Edit https://github.com/waldronlab/MetagenomicsClient/blob/main/Dockerfile" >> /etc/motd
