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
Crea un diagrama de flujo que muestre cómo una IA analiza tickets de Zendesk para soporte técnico.
 Debe incluir: 1) Carga inicial de documentos (KBs, runbooks), 2) Procesamiento de tickets nuevos (NLP/clasificación),
 3) Sugerencias a agentes humanos, y 4) Aprendizaje continuo.
 4) Revision si es un ticket recurrente o es uno nuevo para incluir en los datos de la IA
 Usa colores: morado (datos), verde (IA), azul (humanos).
 Destaca con negritas (Paso X) y emojis (:books:, :robot_face:)

# Especificación Técnica: Dashboard de Monitoreo de Errores

## 1. Objetivo General
Definir las especificaciones funcionales y de diseño para un dashboard web interactivo destinado al monitoreo en tiempo real de errores de sistema/aplicación, incluyendo visualizaciones clave, análisis básicos y navegación a detalles.

## 2. Estructura General del Dashboard
El dashboard constará de las siguientes secciones principales, organizadas en un layout de cuadrícula (grid) flexible y responsivo:
    - Fila 1: Tarjetas de Estadísticas (KPI Cards)
    - Fila 2: Gráficos de Visualización (Tendencia y Distribución)
    - Fila 3: Lista de Errores Recientes y Componente de Análisis IA

## 3. Componentes Detallados

### 3.1. Tarjetas de Estadísticas (KPI Cards)
* **Cantidad:** 4 tarjetas.
* **Disposición:** Horizontal, ocupando el ancho disponible en la Fila 1.
* **Contenido por Tarjeta:**
    * Título claro de la métrica.
    * Valor numérico principal (grande y destacado).
    * Icono representativo asociado a la métrica.
    * Indicador de tendencia (comparado con el periodo anterior, e.g., últimas 24h o 7 días):
        * Formato: Porcentaje de cambio (e.g., +5.2%, -1.0%).
        * Visual: Icono de flecha (arriba/verde para mejora/reducción de errores, abajo/rojo para empeoramiento/aumento, neutral/gris si no hay cambio significativo).
* **Métricas Específicas:**

    ```json
    [
      {
        "id": "total_errors",
        "title": "Total Errores (Últimas 24h)",
        "icon": "bug_report", // Placeholder: usar nombre de icono de una librería (e.g., Material Icons)
        "data_source": "api/errors/count?period=24h" // Placeholder: endpoint API
      },
      {
        "id": "critical_errors",
        "title": "Errores Críticos (Activos)",
        "icon": "error",
        "data_source": "api/errors/count?severity=critical&status=active"
      },
      {
        "id": "anomalies_detected",
        "title": "Anomalías Detectadas (Última Hora)",
        "icon": "warning",
        "data_source": "api/anomalies/count?period=1h"
      },
      {
        "id": "active_alerts",
        "title": "Alertas Activas",
        "icon": "notifications_active",
        "data_source": "api/alerts/count?status=active"
      }
    ]
    ```

### 3.2. Gráficos de Visualización
* **Disposición:** Dos gráficos lado a lado en la Fila 2 (o uno encima del otro en pantallas pequeñas).

    * **Gráfico 1: Tendencia de Errores y Anomalías**
        * **Tipo:** Gráfico de líneas (Line Chart).
        * **Datos:**
            * Serie 1: Conteo de errores por unidad de tiempo.
            * Serie 2: Conteo de anomalías detectadas por unidad de tiempo.
        * **Eje X:** Tiempo (últimos 7 días, con granularidad diaria o incluso horaria si es posible).
        * **Eje Y:** Conteo (número de ocurrencias).
        * **Interactividad:** Tooltips al pasar el cursor sobre puntos de datos mostrando fecha/hora y conteo exacto. Leyenda para distinguir las series.

    * **Gráfico 2: Distribución de Errores por Severidad**
        * **Tipo:** Gráfico circular (Pie Chart) o de Donut.
        * **Datos:** Distribución porcentual de los errores activos o de las últimas 24h según su nivel de severidad.
        * **Categorías (Severidad):** Utilizar las definidas en la sección 5 (Estructura de Datos).
        * **Visualización:**
            * Cada sector representa una severidad.
            * Mostrar porcentaje y/o conteo en cada sector o en la leyenda.
            * **Paleta de Colores:** Asignar colores consistentes y semánticamente apropiados (e.g., Rojo para Crítico, Naranja para Alto, Amarillo para Medio, Azul/Gris para Bajo/Informativo). Definir la paleta explícitamente.

            ```json
            {
              "chart_type": "pie",
              "data_source": "api/errors/distribution?period=24h&group_by=severity",
              "color_palette": {
                "critical": "#FF0000", // Rojo
                "high": "#FFA500",     // Naranja
                "medium": "#FFFF00",   // Amarillo
                "low": "#ADD8E6",      // Azul claro
                "info": "#D3D3D3"      // Gris claro
              }
            }
            ```

### 3.3. Lista de Errores Recientes
* **Tipo:** Tabla o lista densa.
* **Disposición:** Ocupando una parte de la Fila 3.
* **Contenido:** Mostrar los N errores más recientes (e.g., N=10, con opción de paginación o scroll infinito si hay muchos).
* **Columnas/Campos por Error:**
    * `Timestamp`: Fecha y hora de ocurrencia (formato legible, e.g., `YYYY-MM-DD HH:MM:SS`).
    * `Severity`: Nivel de severidad (usando las categorías definidas), visualmente destacado (e.g., con color o badge).
    * `Status`: Estado actual del error (e.g., `Nuevo`, `Investigando`, `Resuelto`).
    * `Message`: Mensaje o descripción corta del error.
    * `Error ID`: Identificador único del error (clickable para navegación).
* **Orden:** Descendente por `Timestamp` (más reciente primero).
* **Interactividad:** Hacer que cada fila o el `Error ID` sea clickable para navegar a la vista de detalles (ver Sección 7).

### 3.4. Componente de Análisis IA
* **Tipo:** Tarjeta o sección dedicada.
* **Disposición:** Ocupando la parte restante de la Fila 3, junto a la Lista de Errores Recientes.
* **Contenido:**
    * Título: "Análisis IA de Problemas Potenciales".
    * Lista de hallazgos o un resumen principal. Para cada hallazgo:
        * `Potential Issue`: Descripción del problema inferido por la IA (e.g., "Incremento anómalo de errores 5xx en servicio de pagos").
        * `Confidence Level`: Nivel de confianza del análisis (e.g., `Alto (95%)`, `Medio (70%)`).
        * `Recommendation`: Acción sugerida (e.g., "Revisar logs del servicio de pagos", "Escalar a equipo de infraestructura").
* **Data Source:** `api/ai/analysis/summary` (Placeholder: endpoint que provee este análisis).

## 4. Diseño Responsivo
* **Requisito:** El layout del dashboard debe adaptarse fluidamente a diferentes tamaños de pantalla (desktop, tablet, móvil).
* **Estrategia:**
    * Utilizar un sistema de cuadrícula (grid) CSS (e.g., CSS Grid, Flexbox, o frameworks como Bootstrap/Tailwind).
    * En pantallas pequeñas (móvil):
        * Las tarjetas de estadísticas pueden apilarse verticalmente (1 o 2 columnas).
        * Los gráficos pueden apilarse verticalmente.
        * La lista de errores y el análisis IA pueden apilarse verticalmente.
        * Considerar simplificar la información mostrada o usar tabs si el espacio es muy limitado.

## 5. Estructura de Datos - Categorización de Errores
* **Propósito:** Definir una estructura consistente para clasificar los errores.
* **Formato Sugerido:** JSON.

    ```json
    {
      "error_severities": [
        {
          "level": "critical",
          "description": "Errores que causan inoperabilidad del sistema o pérdida de datos crítica.",
          "color_code": "#FF0000"
        },
        {
          "level": "high",
          "description": "Errores que afectan funcionalidades principales pero el sistema sigue operativo.",
          "color_code": "#FFA500"
        },
        {
          "level": "medium",
          "description": "Errores que afectan funcionalidades secundarias o causan degradación del rendimiento.",
          "color_code": "#FFFF00"
        },
        {
          "level": "low",
          "description": "Errores menores, problemas de UI, o fallos no críticos.",
          "color_code": "#ADD8E6"
        },
        {
          "level": "info",
          "description": "Mensajes informativos o de depuración, no son errores funcionales.",
          "color_code": "#D3D3D3"
        }
      ],
      "error_statuses": [
        {"status": "new", "description": "Error recién registrado, sin asignar."},
        {"status": "assigned", "description": "Error asignado a un responsable."},
        {"status": "investigating", "description": "Se está investigando la causa del error."},
        {"status": "resolved", "description": "Se ha aplicado una solución."},
        {"status": "closed", "description": "Solución verificada, caso cerrado."},
        {"status": "ignored", "description": "Error marcado como no relevante o duplicado."}
      ]
    }
    ```

## 6. Sistema de Navegación
* **Requisito:** Permitir la navegación desde el dashboard principal a una vista detallada para cada error.
* **Mecanismo:**
    * En la "Lista de Errores Recientes", el `Error ID` o la fila completa debe ser un enlace.
    * Al hacer clic, el usuario debe ser redirigido a una nueva página/vista (e.g., `/errors/details/{error_id}`).
    * Esta vista detallada debe mostrar toda la información disponible del error específico (logs, stack trace, historial de estado, etc.). (La especificación de esta página de detalle está fuera del alcance de este prompt, pero se menciona la necesidad de la navegación).

## 7. Consideraciones Adicionales (Opcional)
* **Actualización de Datos:** Especificar si el dashboard requiere actualización en tiempo real (e.g., WebSockets) o mediante polling periódico (e.g., cada 30 segundos).
* **Filtrado/Rango de Fechas:** Considerar añadir controles globales para filtrar todo el dashboard por rango de fechas o por otros criterios (e.g., tipo de servicio, entorno).
* **Stack Tecnológico:** Si aplica, mencionar las tecnologías preferidas (e.g., React, Vue, Angular para el frontend; librerías de gráficos como Chart.js, D3.js, etc.).

---

Este prompt tecnificado proporciona una estructura clara, detalla cada componente con sus atributos y datos necesarios, utiliza JSON para la configuración y estructuras de datos, y aborda requisitos técnicos como la responsividad y la navegación. Es una base mucho más sólida para un equipo de desarrollo o diseño.




# hackaton_simetrik



