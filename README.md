# Ticket Analyzer Demo

Esta es una demostración de una herramienta de análisis de tickets de soporte técnico. La aplicación simula el proceso de análisis de tickets de Zendesk utilizando IA para proporcionar recomendaciones y soluciones.

## 🚀 Características de la Demo

- Interfaz moderna y fácil de usar
- Simulación de análisis de tickets
- Ejemplo predefinido de ticket de soporte técnico
- Visualización estructurada de la información
- Diseño responsivo

## 📋 Ejemplo de Ticket Incluido

La demo incluye un ejemplo real de ticket (#35691) que muestra:

- **Información del Ticket**:
  - ID: #35691
  - Estado: Resuelto
  - Prioridad: Normal
  - Categoría: Educación - (EDU)

- **Problema**: 
  - Formato de fecha en la columna FECHAPAGO
  - Necesidad de conversión al formato 2024-12-27
  - Problemas con formatos múltiples

- **Solución Propuesta**:
  - Identificación de formatos (ddMMyyyy.0, ddMyyyy.0, dMMyyyy.0)
  - Fórmula de transformación para manejar casos especiales
  - Recomendaciones específicas

## 🛠️ Tecnologías Utilizadas

- **Frontend**:
  - HTML5
  - Tailwind CSS
  - JavaScript Vanilla

- **Backend**:
  - FastAPI
  - OpenAI GPT-4 (simulado en la demo)

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Iniciar el servidor:
```bash
uvicorn backend.main:app --reload
```

4. Abrir `frontend/index.html` en tu navegador

## 🎯 Uso de la Demo

1. Abre la aplicación en tu navegador
2. Haz clic en "Analizar PDF" para ver el ejemplo predefinido
3. Observa la estructura del análisis y las recomendaciones

## ⚠️ Notas Importantes

- Esta es una **DEMO** y no una aplicación en producción
- El análisis mostrado es un ejemplo predefinido
- La funcionalidad de carga de PDF está presente pero no procesa realmente los archivos
- El ejemplo muestra un caso real de soporte técnico con formato de fechas

## 📝 Estructura del Proyecto

```
.
├── backend/
│   └── main.py
├── frontend/
│   └── index.html
├── requirements.txt
└── README.md
```

## 🔍 Ejemplo de Análisis

El análisis incluye:
1. Información básica del ticket
2. Descripción del problema
3. Solución propuesta
4. Recomendaciones específicas
5. Código de ejemplo para la solución

## 🤝 Contribuciones

Esta es una demo educativa. Si deseas contribuir o tienes sugerencias, por favor abre un issue en el repositorio.

## 📄 Licencia

Este proyecto es una demo educativa y está disponible para uso libre.
# hackaton_simetrik
