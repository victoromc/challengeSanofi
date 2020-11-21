# challengeSanofi [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/victoromc/challengeSanofi/blob/master/LICENSE)

Projeto desenvolvido para explorar a base do DATASUS e converter os arquivos DBC's em CSV's, compativel apenas para Linux.

## Como instalar?

- git
- [docker](https://store.docker.com/editions/community/docker-ce-server-ubuntu)

Logo em seguinda execute os passos abaixo:

```bash
$ git clone https://github.com/greatjapa/dbc2csv.git
$ cd challengeSanofi
$ docker build -t dbc2csv .
$ ./challengeSanofi.sh
```

## Como funciona?

Ao executar o comando, dentro da pasta "challengeSanofi"
```bash
$ ./challengeSanofi.sh
```

E então, navegar pelo FTP do DATASUS até o arquivo DBC que você deseja baixar.
Após escolher o arquivo, será criado um diretório "Source" e em seguido convertido
Ao final do processo, o diretório `Source` será preenchido com arquivos `dbf` e `csv`:

```
source/
    file00.dbc
    file00.dbf
    csv/
        file00.csv
        ...
    ...
```


## Referências

* [GIT greatjapa](https://github.com/greatjapa/dbc2csv)

* [Documentação oficial do SUS](http://cnes.datasus.gov.br/pages/downloads/documentacao.jsp), `http://CNES.DataSUS.gov.br`.
