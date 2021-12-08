# Trabalho Redes de Computadores/DCC042

Client-Server usando SOCKET

## Execução
**1.** instale a versão Python3: 

**Windows:** https://www.python.org/downloads/

**Linux:** `$ sudo apt-get install python3`

## Instruções de uso

**1.** Execute o seguinte comando primeiro:

```bash
$ python3 server.py
```

Agora o servidor está esperando a conexão do cliente...

Para o cliente se conectar com o servidor, ele anuncia(maquina/porta) e o servidor aloca uma porta local a qual será utilizada durante essa conexão(automático pelo sistema). Se o servidor aceitar a conexão o socket é criado com sucesso e o cliente usa esse socket para comunicar com o
servidor. Para isso acontecer...

**2.** Execute o comando abaixo:

```bash
$ python3 client.py
```

Pronto! Cliente conectado no servidor. 

Agora o cliente e o servidor podem se comunicar escrevendo/lendo de seus respectivos sockets. Para essa comunicação ocorrer é necessário que o usuário digite **echo** antes da mensagem.

**Relatório do trabalho:** https://drive.google.com/file/d/1eT_kx6V8lMSwz-TBiBBFLoQpVZE_aRgv/view?usp=sharing
