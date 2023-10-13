# aisweb

Esta é uma aplicação que obtém informações do site https://aisweb.decea.mil.br/ sobre as condições meteorológicas dos aeródromos, horários de nascer e pôr do sol, assim como as cartas disponíveis. É necessário o fornecimento do código ICAO do aeródomo.


# Execução local
Foi criado um Dockerfile para caso queira executar a aplicação localmente. Clone esse
repositório, tenha o docker instalado e na pasta raiz
do projeto execute:

docker build -t aisweb .

docker run -it aisweb

E no docker execute:
python aisweb.py <código ICAO>

Exemplo:
python aisweb.py SBMT

