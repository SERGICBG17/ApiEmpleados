
# 📘 Manual de Despliegue: API de Empleados

Este tutorial te guiará desde la creación de los archivos de configuración hasta el despliegue final en contenedores.

## 1. Preparación del Entorno

Antes de empezar, asegúrate de tener la siguiente estructura de carpetas:

```text
/api_empleados
├── app/                <-- Tu código Python
├── data/               <-- CREA ESTA CARPETA (Para SQLite)
├── .env                <-- Configuración de variables
├── Dockerfile          <-- Receta de la imagen
├── docker-compose.yml  <-- Orquestación de servicios
└── requirements.txt    <-- Librerías necesarias

```

---

## 2. Configuración de Archivos Base

### A. `requirements.txt`

Es vital incluir el driver de Postgres para que la API pueda comunicarse con él.

```text
fastapi
sqlmodel
uvicorn
pydantic-settings
psycopg2-binary

```

### B. `Dockerfile`

Este archivo define cómo se construye la imagen de tu API.

```dockerfile
FROM python:3.12-slim

WORKDIR /code

# Crear carpeta para la base de datos SQLite
RUN mkdir -p /code/data

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el entorno y el código
COPY .env .
COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

```

---

## 3. Orquestación con Docker Compose

El archivo `docker-compose.yml` permite levantar la base de datos Postgres y la API al mismo tiempo, conectándolas automáticamente.

```yaml
services:
  db:
    image: postgres:15
    restart: always
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
      - POSTGRES_DB=empleados_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  api:
    build: .
    ports:
      - "8080:8000"
    environment:
      - DATABASE_URL=postgresql://myuser:mypassword@db:5432/empleados_db
      - DEBUG=True
    depends_on:
      - db

volumes:
  postgres_data:

```

---

## 4. Pasos para el Despliegue

### Caso 1: Usar PostgreSQL (Producción/Docker Compose)

Ideal cuando quieres una base de datos robusta.

1. Abre tu terminal en la carpeta raíz.
2. Ejecuta: `docker compose up --build`.
3. La API estará disponible en: **`http://localhost:8080/docs`**.

### Caso 2: Usar SQLite (Desarrollo/IntelliJ)

Ideal para pruebas rápidas sin levantar servidores externos.

1. **Edita tu `.env**`: Comenta la línea `DATABASE_URL` poniendo un `#` al principio.
2. **Configura IntelliJ**:
* Ve a **Run/Debug Configurations** -> **Docker**.
* En **Bind Mounts**, añade:
* **Host path**: Selecciona tu carpeta `/data` local.
* **Container path**: `/code/data` (¡No olvides la barra inicial `/`!).




3. **Ejecuta**: Pulsa el botón Play. El archivo `database.db` aparecerá en tu carpeta local.

---

## 5. Verificación y Pruebas

Una vez levantada la API (en cualquiera de los dos casos):

1. **Accede a Swagger**: Ve a `http://localhost:8080/docs`.
2. **Inicialización**: El código ejecuta `SQLModel.metadata.create_all(engine)` al arrancar, por lo que las tablas ya deberían estar creadas.
3. **Prueba un POST**: Crea un empleado.
* Si usas **Postgres**: Los datos viven en el volumen `postgres_data`.
* Si usas **SQLite**: Los datos viven en tu carpeta `data/database.db`.


