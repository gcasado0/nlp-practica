# nlp-practica

# crear enviroment
```bash
# Crear entorno virtual (opcional pero recomendado)
python3 -m venv .venv
source .venv/bin/activate  # En Windows: venv\Scripts\activate
```

# Instalar dependencias

- Version de python requerida: 3.12

```bash
pip install -r requirements.txt
```

# Iniciar servicio de mongoDB
```bash
sudo systemctl start mongod
sudo systemctl status mongod
```

# Iniciar base de datos Neo4j (Docker)

El proyecto utiliza **Neo4j** como base de datos de grafos. Se incluye una configuración de Docker Compose para levantar el servicio localmente de forma rápida.

## Requisitos previos

- Tener instalado [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/).

## Instrucciones de uso

1. **Levantar el servicio:**
   ```bash
   docker-compose up -d
   ```

2. **Detener el servicio:**
   ```bash
   docker-compose down
   ```

## Detalles de conexión

Una vez levantado el contenedor, el servicio estará disponible con los siguientes datos (los cuales coinciden con la configuración en [config.ini](file:///home/gcasado0/aprendizaje/UNR/NLP/nlp-practica/config.ini)):

- **Consola Web (Neo4j Browser):** [http://localhost:7474](http://localhost:7474)
- **URI de Conexión (Bolt):** `bolt://localhost:7687`
- **Usuario:** `neo4j`
- **Contraseña:** Configurada en `NEO4J_AUTH` dentro de [docker-compose.yml](file:///home/gcasado0/aprendizaje/UNR/NLP/nlp-practica/docker-compose.yml) (debe coincidir con la definida en [config.ini](file:///home/gcasado0/aprendizaje/UNR/NLP/nlp-practica/config.ini)).


> [!NOTE]
> - La configuración incluye la instalación automática de la librería **APOC** (útil para procesamiento de grafos/NLP).
> - Los datos y logs de la base de datos se persisten localmente en el directorio `./.neo4j_data/`.