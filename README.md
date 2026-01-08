# Sistema de Gestión y Venta de Artesanías Saraguro (SGV-APS)

Este proyecto implementa una solución web para la gestión de ventas de artesanías utilizando una **Arquitectura Estricta de 3 Capas (Cliente/Servidor)** desplegada en un único nodo lógico.

## 📋 Tabla de Contenidos

- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Características](#-características)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación-y-ejecución)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Tecnologías](#-tecnologías)
- [Base de Datos](#-base-de-datos)
- [Desarrollador](#-desarrollador)

## 🏗️ Arquitectura del Sistema

El sistema respeta estrictamente la separación de responsabilidades en 3 capas:

### 1. Capa de Presentación (Frontend/Controlador)
- **Tecnología:** Flask + Jinja2 Templates
- **Ruta:** [`capa_presentacion/`](capa_presentacion/)
- **Responsabilidad:** 
  - Interacción con el usuario
  - Renderizado de vistas HTML
  - No tiene acceso directo a la BD
- **Archivos principales:**
  - [`rutas.py`](capa_presentacion/rutas.py) - Rutas y controladores Flask
  - [`templates/index.html`](capa_presentacion/templates/index.html) - Vista del catálogo
  - [`templates/venta.html`](capa_presentacion/templates/venta.html) - Vista de confirmación de venta

```markdown
# Sistema de Gestión y Venta de Artesanías Saraguro (SGV-APS)

Este proyecto implementa una solución web para la gestión de ventas de artesanías utilizando una **Arquitectura Estricta de 3 Capas (Cliente/Servidor)** desplegada en un único nodo lógico.

## 📋 Tabla de Contenidos

- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Características](#-características)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Tecnologías](#-tecnologías)
- [Base de Datos](#-base-de-datos)
- [Notas de Implementación](#-notas-de-implementación)
- [Desarrollador](#-desarrollador)

## 🏗️ Arquitectura del Sistema

El sistema respeta la separación de responsabilidades en 3 capas:

### 1. Capa de Presentación (Frontend/Controlador)
- **Tecnología:** Flask + Jinja2 Templates
- **Ruta:** [`capa_presentacion/`](capa_presentacion/)
- **Responsabilidad:**
  - Interacción con el usuario
  - Renderizado de vistas HTML
  - No tiene acceso directo a la BD
- **Archivos principales:**
  - [`rutas.py`](capa_presentacion/rutas.py) - Rutas y controladores Flask
  - [`templates/index.html`](capa_presentacion/templates/index.html) - Vista del catálogo
  - [`templates/venta.html`](capa_presentacion/templates/venta.html) - Vista de confirmación de venta

### 2. Capa de Negocio (Lógica)
- **Tecnología:** Python (Clases de Servicio)
- **Ruta:** [`capa_negocio/`](capa_negocio/)
- **Responsabilidad:**
  - Validación de reglas de negocio
  - Validación de stock
  - Validación de precios
  - Orquestación entre presentación y datos
- **Archivos principales:**
  - [`servicios.py`](capa_negocio/servicios.py) - Clase `ServicioVentas` (inicia un hilo en background para simular avance de estados de pedidos)

### 3. Capa de Datos (Persistencia)
- **Tecnología:** MySQL Connector
- **Ruta:** [`capa_datos/`](capa_datos/)
- **Responsabilidad:**
  - Consultas SQL directas
  - Conexión a base de datos `sistema_sarag`
  - Gestión de persistencia
- **Archivos principales:**
  - [`repositorio.py`](capa_datos/repositorio.py) - Clase `RepositorioArtesanias` (crea tablas, semillas y tiene métodos para pedidos y simulación)

## ✨ Características

- ✅ Catálogo de artesanías
- ✅ Gestión automática de stock y registro de pedidos
- ✅ Soporte para diferentes métodos de pago y tipo de cliente
- ✅ Simulación automática del avance de estado de pedidos (background thread)
- ✅ Inserción de datos semilla al inicializar la BD

## 🔧 Requisitos Previos

- Python 3.8 o superior
- MySQL 5.7 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación y Ejecución

### 1) Clonar el repositorio
```bash
git clone <https://github.com/ronaaal/Sistema-Gestion-Venta-Saraguro.git>
cd prueba_parcial
```

### 2) Crear y activar entorno virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3) Instalar dependencias
```bash
pip install -r requirements.txt || pip install flask mysql-connector-python
```

Si no tienes un `requirements.txt`, el comando alternativo instalará Flask y el conector MySQL.

### 4) Configurar la base de datos

Crear la base de datos en MySQL:
```sql
CREATE DATABASE sistema_sarag;
```

Por seguridad se recomienda usar variables de entorno para las credenciales. Ejemplo (Windows PowerShell):
```powershell
$env:DB_USER='root'
$env:DB_PASS='UTPL2023'
$env:DB_HOST='localhost'
$env:DB_NAME='sistema_sarag'
$env:DB_PORT='3306'
```

La configuración por defecto está en `capa_datos/repositorio.py` (valor hardcodeado). Puedes cambiarla ahí o modificar el código para leer variables de entorno.

### 5) Ejecutar la aplicación
```bash
python run.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
prueba_parcial/
├── README.md
├── run.py
├── capa_presentacion/
│   ├── __init__.py
│   ├── rutas.py
│   └── templates/
│       ├── index.html
│       └── venta.html
├── capa_negocio/
│   ├── __init__.py
│   └── servicios.py
└── capa_datos/
    ├── __init__.py
    └── repositorio.py
```

## 💻 Uso

### Flujo de Usuario

1. Acceder a la página principal y ver los productos
2. Seleccionar cantidad y método de pago
3. Confirmar compra
4. El pedido se registra con estado `Pendiente`
5. Un hilo en background avanza automáticamente los estados: `Pendiente` -> `Enviado` -> `Entregado`

### Notas sobre ejecución
- El punto de entrada es `run.py`, que invoca `capa_presentacion.rutas.main()`.
- `ServicioVentas` inicia un hilo daemon que cada 5s ejecuta `simular_avance_estados()` para actualizar estados de pedidos.

## 🗄️ Base de Datos

### Tabla: `productos`

```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    precio DECIMAL(10, 2),
    stock INT,
    artesana VARCHAR(100)
);
```

### Tabla: `pedidos` (actualizada)

```sql
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_nombre VARCHAR(100),
    cantidad INT,
    total DECIMAL(10,2),
    metodo_pago VARCHAR(50),
    tipo_cliente VARCHAR(50),
    estado VARCHAR(50),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla: `eventos`

```sql
CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150), fecha VARCHAR(50), lugar VARCHAR(100), destacado BOOLEAN
);
```

### Datos Iniciales (semilla)

Al inicializar la BD el repositorio inserta productos y un evento si las tablas están vacías. Ejemplos insertados:
- `Collar Chakana`, `Aretes Mullos`, `Poncho Tradicional`
- Evento: `Feria Saraguro` (destacado)

## 🔐 Notas de Implementación

- `capa_datos/repositorio.py` crea tablas y semillas al iniciarse.
- Se añadieron los métodos `obtener_pedidos()` y `simular_avance_estados()` en el repositorio para mostrar pedidos recientes y avanzar estados.
- `servicios.py` instancia `RepositorioArtesanias` y expone `obtener_todo()` y `realizar_venta()`; además inicia un hilo daemon que llama a `simular_avance_estados()` cada 5 segundos.
- Para producción: mover credenciales a variables de entorno y usar un proceso de background adecuado (worker/cron) en lugar de hilo en proceso web.

## ✅ Cambios detectados y añadidos al README

- Background thread en `ServicioVentas` que simula avance de estados.
- Nueva columna/atributo `tipo_cliente` y `metodo_pago` en la tabla `pedidos`.
- Nuevos métodos: `obtener_pedidos()` y `simular_avance_estados()`.
- Datos semilla actualizados (incluye `Poncho Tradicional`).

## 👥 Desarrollador

Proyecto desarrollado para la evaluación de **Ingeniería de Software - Séptimo Ciclo**  
Universidad Técnica Particular de Loja (UTPL)

---

**Última actualización:** 2026-01-08
```