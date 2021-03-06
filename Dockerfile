# 1) indicamos la imagen base a usar
FROM faucet/python3

#Author and Maintainer
MAINTAINER wisrovi.rodriguez@gmail.com

# 2) creamos una carpeta para alojar los archivos del proyecto
WORKDIR /monitor_contingencia

RUN echo monitor_contingencia

# 3) instalamos sudo y actualizamos
#RUN apt-get update -y
#RUN apt-get -y install sudo

# 4) instalar dependencias del SO

# 5) instalar dependencias de python
RUN pip3 install flask
RUN pip3 install pyTelegramBotAPI
RUN pip3 install python-decouple
RUN pip3 install requests

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# 6) copiamos la carpeta del codigo y todos sus recursos
COPY src .

# 7) le damos permisos a la carpeta donde se alojan los archivos del proyecto para que los archivos python puedan trabajar sin problemas
#RUN sudo chmod -R +777 /monitor_contingencia

# 8) le decimos que archivo ejecutar cuando se lance el container
# CMD [ "tail" ,"-f", "/etc/hosts" ]
CMD ["python3", "./service.py" ]
