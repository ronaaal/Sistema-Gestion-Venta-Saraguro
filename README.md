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

### 2. Capa de Negocio (Lógica)
- **Tecnología:** Python (Clases de Servicio)
- **Ruta:** [`capa_negocio/`](capa_negocio/)
- **Responsabilidad:**
  - Validación de reglas de negocio
  - Validación de stock
  - Validación de precios
  - Orquestación entre presentación y datos
- **Archivos principales:**
  - [`servicios.py`](capa_negocio/servicios.py) - Clase `ServicioVentas`

### 3. Capa de Datos (Persistencia)
- **Tecnología:** MySQL Connector
- **Ruta:** [`capa_datos/`](capa_datos/)
- **Responsabilidad:**
  - Consultas SQL directas
  - Conexión a base de datos `sistema_sarag`
  - Gestión de persistencia
- **Archivos principales:**
  - [`repositorio.py`](capa_datos/repositorio.py) - Clase `RepositorioArtesanias`

## ✨ Características

- ✅ Catálogo de artesanías con búsqueda en tiempo real
- ✅ Gestión de stock automática
- ✅ Sistema de compras con validación
- ✅ Interfaz responsiva y amigable
- ✅ Arquitectura de 3 capas desacoplada
- ✅ Base de datos MySQL integrada
- ✅ Mensajes de error y éxito informativos

## 🔧 Requisitos Previos

- Python 3.8 o superior
- MySQL 5.7 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación y Ejecución

### Paso 1: Clonar el repositorio
```bash
git clone <https://github.com/ronaaal/Sistema-Gestion-Venta-Saraguro.git>
cd prueba_parcial
```

### Paso 2: Crear entorno virtual
```bash
python -m venv venv
```

### Paso 3: Activar el entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### Paso 4: Instalar dependencias
```bash
pip install flask mysql-connector-python
```

### Paso 5: Configurar la base de datos

Asegurate de que MySQL esté corriendo y crear la base de datos:
```sql
CREATE DATABASE sistema_sarag;
```

Actualizar credenciales en [`capa_datos/repositorio.py`](capa_datos/repositorio.py) si es necesario:
```python
self.config = {
    'user': 'root',          
    'password': 'UTPL2023',          
    'host': 'localhost',
    'database': 'sistema_sarag', 
    'port': 3306
}
```

### Paso 6: Ejecutar la aplicación
```bash
python run.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
prueba_parcial/
├── README.md                          # Este archivo
├── run.py                             # Punto de entrada principal
├── capa_presentacion/                 # Capa de Presentación (Web UI)
│   ├── __init__.py
│   ├── rutas.py                       # Controladores Flask
│   ├── __pycache__/
│   └── templates/
│       ├── index.html                 # Catálogo de productos
│       └── venta.html                 # Confirmación de venta
├── capa_negocio/                      # Capa de Negocio (Lógica)
│   ├── __init__.py
│   ├── servicios.py                   # ServicioVentas - Orquestación
│   └── __pycache__/
└── capa_datos/                        # Capa de Datos (Persistencia)
    ├── __init__.py
    ├── repositorio.py                 # RepositorioArtesanias - Acceso a BD
    └── __pycache__/
```

## 💻 Uso

### Flujo de Usuario

1. **Ver Catálogo:** El usuario accede a la página principal y ve todos los productos disponibles
2. **Seleccionar Cantidad:** Elige la cantidad deseada (validado contra el stock disponible)
3. **Confirmar Compra:** Hace clic en "Comprar"
4. **Procesar:** El sistema valida stock y aplica la compra
5. **Resultado:** Se muestra un mensaje de éxito o error

### Ejemplo de Compra

```
1. Usuario navega a http://localhost:5000
2. Ve "Collar Chakana - $25.00 - Stock: 10"
3. Selecciona cantidad: 2
4. Hace clic en "Comprar"
5. Respuesta: "¡Éxito! Compra realizada por $50.00"
6. Stock se actualiza a 8
```

## 🛠️ Tecnologías

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Presentación | Flask | 2.0+ |
| Presentación | Jinja2 | Incluido en Flask |
| Negocio | Python | 3.8+ |
| Datos | MySQL Connector | 8.0+ |
| Base Datos | MySQL | 5.7+ |

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

### Datos Iniciales

La aplicación inserta automáticamente estos productos:

| ID | Nombre | Tipo | Precio | Stock | Artesana |
|----|--------|------|--------|-------|----------|
| 1 | Collar Chakana | Collar | $25.00 | 10 | María Saraguro |
| 2 | Aretes de Mullos | Aretes | $12.50 | 20 | Juana Quizhpe |
| 3 | Manilla Tejida | Manilla | $8.00 | 15 | Rosa Gualán |

## 🔐 Reglas de Negocio

✓ La cantidad debe ser mayor a 0  
✓ El stock no puede ser negativo  
✓ Solo se vende si hay suficiente inventario  
✓ El precio se calcula automáticamente  
✓ Los productos agotados se deshabilitan  

## ⚠️ Notas Importantes

- Las credenciales de MySQL están en [`capa_datos/repositorio.py`](capa_datos/repositorio.py)
- Para producción, usar variables de entorno en lugar de hardcodear credenciales
- La base de datos se inicializa automáticamente al ejecutar la aplicación

## 👥 Desarrollador

Proyecto desarrollado para la evaluación de **Ingeniería de Software - Séptimo Ciclo**  
Universidad Técnica Particular de Loja (UTPL)

---

**Última actualización:** 2025