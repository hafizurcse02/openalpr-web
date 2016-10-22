FROM python:3

RUN apt-get -y update && \
    apt-get -y install curl wget libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev liblog4cplus-dev libcurl3-dev beanstalkd && \
    pip install tornado

ADD webservice /webservice

ADD openalpr /storage/projects/alpr

RUN cd /storage/projects/alpr/src && \
      mkdir build && \
      cd build && \
      cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc .. && \
      make -j2 && \
      make install

RUN cd /storage/projects/alpr/src/bindings/python && \
      python setup.py install && \
      ./make.sh

ENTRYPOINT ["python"]

CMD ["/webservice/openalpr_web.py"]
