FROM continuumio/miniconda3:4.5.12

COPY . /app

WORKDIR /app

#RUN scrips/download_resources.sh

RUN pip install --upgrade pip
RUN conda env update -f environment.yml && conda clean -y --all

EXPOSE 8080

CMD uwsgi --ini ./config/uwsgi.ini
