
# API de Empleados

API REST desarrollada con FastAPI para la gestión de empleados, departamentos y sedes. Esta API sirve como backend para la aplicación [AppGestionEmpleadosII](https://github.com/SERGICBG17/AppGestionEmpleadosII).

## Descripción

API RESTful que proporciona endpoints para realizar operaciones CRUD sobre empleados, departamentos y sedes. Soporta dos tipos de bases de datos según la configuración: SQLite para desarrollo local y PostgreSQL para producción/contenedores.

## Tecnologías

- **FastAPI** - Framework web moderno y rápido
- **SQLModel** - ORM basado en SQLAlchemy y Pydantic
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **PostgreSQL** - Base de datos relacional (producción)
- **SQLite** - Base de datos local (desarrollo)
- **Docker** - Contenedorización

## Características

- CRUD completo para empleados, departamentos y sedes
- Documentación automática con Swagger UI
- Soporte para SQLite y PostgreSQL mediante variables de entorno
- Ejecución con Docker o sin Docker
- Validación de datos con Pydantic
- Migraciones automáticas de base de datos

## Estructura del Proyecto

```
ApiEmpleados/
├── app/
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── models.py            # Modelos de datos
│   ├── database.py          # Configuración de base de datos
│   ├── routes/              # Endpoints de la API
│   └── schemas.py           # Esquemas de validación
├── data/                    # Carpeta para SQLite (crear si no existe)
├── .env                     # Variables de entorno
├── Dockerfile               # Imagen Docker de la API
├── docker-compose.yaml      # Orquestación de servicios
└── requirements.txt         # Dependencias Python
```

## Requisitos Previos

### Para ejecución sin Docker
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Para ejecución con Docker
- Docker Desktop instalado
- Docker Compose

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/SERGICBG17/ApiEmpleados.git
cd ApiEmpleados
```

### 2. Preparar la Estructura de Carpetas

Crear la carpeta `data` para SQLite si no existe:

```bash
mkdir data
```

### 3. Instalar Dependencias (Solo para ejecución sin Docker)

```bash
# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración de Variables de Entorno

La aplicación utiliza variables de entorno para determinar qué base de datos usar. Crea un archivo `.env` en la raíz del proyecto:

### Opción 1: SQLite (Desarrollo Local)

```env
# Comentar o eliminar DATABASE_URL para usar SQLite
# DATABASE_URL=postgresql://user:password@host:port/database
DEBUG=True
```

Con esta configuración, la API creará automáticamente un archivo `database.db` en la carpeta `data/`.

### Opción 2: PostgreSQL (Producción/Docker)

```env
DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/empleados_db
DEBUG=True
```

**Nota**: Cuando uses Docker Compose, la URL debe apuntar al nombre del servicio: `@db` en lugar de `@localhost`.

## Ejecución de la API

### Método 1: Sin Docker (Desarrollo Local con SQLite)

Ideal para desarrollo rápido y pruebas locales.

1. **Configurar variables de entorno**:
   - Asegúrate de que `DATABASE_URL` esté comentada en `.env`
   - O simplemente elimina esa línea del archivo `.env`

2. **Ejecutar la aplicación**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Acceder a la API**:
   - Documentación Swagger: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`
   - Endpoint base: `http://localhost:8000`

La base de datos SQLite se creará automáticamente en `data/database.db`.

### Método 2: Con Docker y PostgreSQL (Producción)

Ideal para entornos de producción o cuando necesitas PostgreSQL.

1. **Asegúrate de que el archivo `docker-compose.yaml` esté configurado**:

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

2. **Construir y ejecutar los contenedores**:
   ```bash
   docker compose up --build
   ```

3. **Acceder a la API**:
   - Documentación Swagger: `http://localhost:8080/docs`
   - ReDoc: `http://localhost:8080/redoc`
   - Endpoint base: `http://localhost:8080`

**Nota**: El puerto en Docker es `8080` para evitar conflictos.

### Método 3: Solo Docker para la API (SQLite en contenedor)

Si quieres usar Docker pero con SQLite:

1. **Construir la imagen**:
   ```bash
   docker build -t api-empleados .
   ```

2. **Ejecutar el contenedor con volumen montado**:
   ```bash
   docker run -d \
     -p 8080:8000 \
     -v $(pwd)/data:/code/data \
     --name api-empleados \
     api-empleados
   ```

3. **Acceder a la API**: `http://localhost:8080/docs`

## Endpoints de la API

### Empleados

- `GET /empleados` - Listar todos los empleados
- `GET /empleados/{id}` - Obtener un empleado por ID
- `POST /empleados` - Crear nuevo empleado
- `PUT /empleados/{id}` - Actualizar empleado
- `DELETE /empleados/{id}` - Eliminar empleado

### Departamentos

- `GET /departamentos` - Listar todos los departamentos
- `GET /departamentos/{id}` - Obtener un departamento por ID
- `POST /departamentos` - Crear nuevo departamento
- `PUT /departamentos/{id}` - Actualizar departamento
- `DELETE /departamentos/{id}` - Eliminar departamento

### Sedes

- `GET /sedes` - Listar todas las sedes
- `GET /sedes/{id}` - Obtener una sede por ID
- `POST /sedes` - Crear nueva sede
- `PUT /sedes/{id}` - Actualizar sede
- `DELETE /sedes/{id}` - Eliminar sede

## Documentación Interactiva

FastAPI genera automáticamente documentación interactiva:

- **Swagger UI**: Interfaz visual para probar los endpoints
  - URL: `http://localhost:8000/docs` (sin Docker)
  - URL: `http://localhost:8080/docs` (con Docker)

- **ReDoc**: Documentación alternativa más limpia
  - URL: `http://localhost:8000/redoc` (sin Docker)
  - URL: `http://localhost:8080/redoc` (con Docker)

## Base de Datos

### SQLite

- **Ubicación**: `data/database.db`
- **Uso**: Desarrollo local
- **Ventajas**: No requiere instalación adicional, fácil de configurar
- **Activación**: No definir `DATABASE_URL` en `.env`

### PostgreSQL

- **Uso**: Producción, Docker
- **Ventajas**: Mejor rendimiento, más robusto para producción
- **Activación**: Definir `DATABASE_URL` en `.env`

Las tablas se crean automáticamente al iniciar la aplicación mediante `SQLModel.metadata.create_all(engine)`.

## Verificación y Pruebas

1. **Verificar que la API está funcionando**:
   ```bash
   curl http://localhost:8000/docs
   # o
   curl http://localhost:8080/docs
   ```

2. **Probar un endpoint**:
   ```bash
   # Crear un empleado
   curl -X POST "http://localhost:8000/empleados" \
     -H "Content-Type: application/json" \
     -d '{
       "nombre": "Juan Pérez",
       "email": "juan@example.com",
       "departamento_id": 1,
       "sede_id": 1
     }'
   ```

3. **Ver los datos**:
   - SQLite: Usar un visor de SQLite como DB Browser
   - PostgreSQL: Conectar con herramientas como pgAdmin o DBeaver

## Solución de Problemas

### La API no se conecta a PostgreSQL

1. Verifica que PostgreSQL esté ejecutándose
2. Comprueba las credenciales en `DATABASE_URL`
3. Asegúrate de que el puerto no esté ocupado
4. Si usas Docker, verifica que el servicio `db` esté levantado: `docker compose ps`

### Error al crear tablas en SQLite

1. Verifica que la carpeta `data/` exista
2. Comprueba los permisos de escritura
3. Asegúrate de que `DATABASE_URL` no esté definida

### Puerto ocupado

Si el puerto 8000 u 8080 está ocupado:

```bash
# Sin Docker - cambiar el puerto
uvicorn app.main:app --reload --port 8001

# Con Docker - modificar docker-compose.yaml
# Cambiar "8080:8000" a "8081:8000"
```

### Error de importación de módulos

```bash
# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall
```

## Comandos Útiles de Docker

```bash
# Ver logs de la API
docker compose logs api

# Ver logs de la base de datos
docker compose logs db

# Detener servicios
docker compose down

# Detener y eliminar volúmenes (elimina datos)
docker compose down -v

# Reconstruir sin caché
docker compose build --no-cache

# Ejecutar en segundo plano
docker compose up -d
```

## Integración con el Frontend

Esta API está diseñada para trabajar con [AppGestionEmpleadosII](https://github.com/SERGICBG17/AppGestionEmpleadosII). Asegúrate de:

1. La API esté ejecutándose antes de iniciar el frontend
2. La URL de la API en el frontend apunte a `http://localhost:8000` o `http://localhost:8080`
3. CORS esté configurado correctamente en la API para aceptar peticiones del frontend

## Licencia

Este proyecto está bajo la Licencia MIT.

## Enlaces Relacionados

- [Frontend - AppGestionEmpleadosII](https://github.com/SERGICBG17/AppGestionEmpleadosII)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de SQLModel](https://sqlmodel.tiangolo.com/)
