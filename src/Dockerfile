FROM python:3.10.11 as base-image

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /code
ADD tg_bot-requirements.txt requirements.txt
RUN python -m venv /opt/venv

RUN pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"

ENV PATH="/opt/venv/bin:$PATH"
RUN apt-get update \
 && apt-get install -y gcc \
 && pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt \
 && rm -rf /var/lib/apt/lists/*
COPY src/telegram_bot src
USER nobody:nogroup
HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:5000/ || exit 1
#CMD sudo chmod a+rwx debug.log
CMD ["python3", "-u", "src/__main__.py"]
#CMD ["ls"]
