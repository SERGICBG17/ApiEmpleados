from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.responses import HTMLResponse

from app.db.session import engine
from app.routers import departamentos, empleados, sedes

app = FastAPI(
    title="API de Empleados",
    description="API para gestionar sedes, departamentos y empleados",
    version="1.0.0"
)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()

app.include_router(departamentos.router)
app.include_router(empleados.router)
app.include_router(sedes.router)

@app.get("/", response_class=HTMLResponse)
def html():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <title>FastAPI - Welcome</title>
    </head>
    <body class="bg-slate-50 flex items-center justify-center min-h-screen font-sans">
        <div class="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 text-center border border-slate-100">
            <div class="flex justify-center mb-6">
                <div class="bg-teal-100 p-3 rounded-full">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-teal-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                </div>
            </div>
            <h1 class="text-3xl font-bold text-slate-800 mb-2">¡API Operativa!</h1>
            <p class="text-slate-500 mb-8">La conexión con el servidor de FastAPI se ha establecido correctamente.</p>
            
            <div class="space-y-3">
                <a href="/docs" class="block w-full py-3 px-4 bg-teal-600 hover:bg-teal-700 text-white font-semibold rounded-lg transition duration-200">
                    Ir a la Documentación (Swagger)
                </a>
                <a href="/redoc" class="block w-full py-3 px-4 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold rounded-lg transition duration-200">
                    Ver ReDoc
                </a>
            </div>
            
            <footer class="mt-8 pt-6 border-t border-slate-100 text-xs text-slate-400">
                FastAPI • SQLModel • Python 3.12
            </footer>
        </div>
    </body>
    </html>
    """