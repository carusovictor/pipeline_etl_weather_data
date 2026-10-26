# Pipeline ETL de Dados Meteorológicos

Projeto de engenharia de dados que coleta informações meteorológicas de São Paulo pela API OpenWeatherMap,
transforma os dados com Python e Pandas e os armazena em um banco PostgreSQL.
 O fluxo é orquestrado pelo Apache Airflow, executado com Docker.

## Como funciona

O pipeline possui três tarefas, executadas nesta ordem:

1. Extract: consulta a API OpenWeatherMap e salva
    a resposta em "data/weather_data.json".
   
3. Transform: normaliza o JSON, organiza e renomeia as colunas
    e converte datas para o fuso de São Paulo. O resultado intermediário é salvo em Parquet.
   
5. Load: insere os dados tratados na tabela "sp_weather" do PostgreSQL.

A DAG "weather_pipeline" está programada para executar a cada hora.

## Tecnologias

Python · Pandas · Requests · SQLAlchemy · PostgreSQL · Apache Airflow · Docker

## Como executar

Pré-requisitos: Docker com Compose, um PostgreSQL acessível
na máquina e uma chave da [OpenWeatherMap](https://openweathermap.org/api).

1. Criar o arquivo "config/.env" com as credenciais:

   API_KEY=
   user=
   password=
   database=
   
2. Acesse http://localhost:8080 e ative ou execute a DAG "weather_pipeline".

Observação: no código atual, a carga usa "host.docker.internal:5432" para acessar o PostgreSQL da máquina host.
Esse endereço deve estar acessível a partir dos contêineres.

## Estrutura principal

dags/weather_dag.py   # Orquestração do ETL
src/extract_data.py   # Extração da API
src/transform_data.py # Tratamento dos dados
src/load_data.py      # Carga no PostgreSQL
data/                 # Arquivos intermediários


OBRIGADO POR ANALISAR MINHA PRIMEIRA PIPELINE DE DADOS!

