# challengeSanofi [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/victoromc/challengeSanofi/blob/master/LICENSE)

Projeto desenvolvido para explorar a base do DATASUS, converter os arquivos DBC's em CSV's e carregar no mongoDB, compativel apenas para Linux.

## Como instalar?

- git
- [docker](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
- [mongodb](https://www.mongodb.com/try/download/database-tools)

Em seguida execute os passos abaixo:

```bash
$ cd ~/Desktop/
$ git clone https://github.com/victoromc/challengeSanofi.git
$ cd challengeSanofi
$ sudo docker build -t dbc2csv .
```

## Como funciona?

Basta executar o comando, dentro da pasta "challengeSanofi"
```bash
$ ./challengeSanofi.sh
```
E então, navegar pelo FTP do DATASUS até o arquivo DBC que você deseja baixar.

Ao longo do processo, os diretórios `Source` e `csv` serão preenchidos com os arquivos devidamente convertidos:

```
source/
    file00.dbc
    file00.dbf
    csv/
        file00.csv
        ...
    ...
```

Após a execução completa, as extensões finais para `.lido` e `.convertido`, evitando duplicidade:
```
source/
    file00.dbc.convertido
    file00.dbf.convertido
    csv/
        file00.csv.lido
        ...
    ...
```

## Referências

* [Documentação oficial do SUS](http://cnes.datasus.gov.br/pages/downloads/documentacao.jsp), `http://CNES.DataSUS.gov.br`.

## Desenvolvido por:
- [Átila Ferreira](https://github.com/atilafsantos)
- Mariana Lolato
- [Paloma Ricato](https://github.com/PalomaRicato)
- [Pedro Cardo](https://github.com/pedrocardo)
- [Victor Oliver](https://github.com/victoromc)

