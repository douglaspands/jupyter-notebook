ARG PYTHON_TAG=3.8.10


FROM python:${PYTHON_TAG}

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src

COPY jupyter_notebook ./jupyter_notebook
ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN jupyter contrib nbextension install

EXPOSE 8888
ENTRYPOINT [ "jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--no-browser", "--allow-root", "--notebook-dir=./jupyter_notebook/notebook" ]
