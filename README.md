# Sistema de Gestión y Venta de Artesanías Saraguro (SGV-APS)

Este proyecto implementa una solución web para la gestión de ventas de artesanías utilizando una **Arquitectura Estricta de 3 Capas (Cliente/Servidor)** desplegada en un único nodo lógico.

## 🏗️ Arquitectura del Sistema

El sistema respeta estrictamente la separación de responsabilidades:

1.  **Capa de Presentación (Frontend/Controlador):** * Tecnología: Flask + Jinja2 Templates.
    * Ruta: `capa_presentacion/`.
    * Responsabilidad: Interacción con el usuario y renderizado de vistas. No tiene acceso a la BD.

2.  **Capa de Negocio (Lógica):**
    * Tecnología: Python (Clases de Servicio).
    * Ruta: `capa_negocio/`.
    * Responsabilidad: Reglas de validación (Stock, Precios) y orquestación.

3.  **Capa de Datos (Persistencia):**
    * Tecnología: MySQL Connector.
    * Ruta: `capa_datos/`.
    * Responsabilidad: Consultas SQL directas a la base de datos `sistema_sarag`.

## 🚀 Instalación y Ejecución

1.  Clonar el repositorio.
2.  Crear entorno virtual: `python -m venv venv`
3.  Instalar dependencias: `pip install flask mysql-connector-python`
4.  Asegurar que MySQL esté corriendo (Base de datos: `sistema_sarag`).
5.  Ejecutar: `python run.py`

## 👥 Desarrollador
Proyecto desarrollado para la evaluación de Ingeniería de Software.