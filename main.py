from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from typing import Optional
import PyPDF2
import io

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ZendeskTicket(BaseModel):
    ticket_id: str
    subject: str
    description: str
    priority: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[list] = None

def extract_text_from_pdf(pdf_file: UploadFile) -> str:
    try:
        # Leer el contenido del archivo PDF
        contents = pdf_file.file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
        
        # Extraer texto de todas las páginas
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text.strip()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar el PDF: {str(e)}")

@app.post("/api/analyze-ticket")
async def analyze_ticket(ticket: ZendeskTicket):
    try:
        # Construir el prompt para el análisis
        prompt = f'''
Analiza el siguiente ticket de Zendesk y proporciona una respuesta detallada:

ID del Ticket: {ticket.ticket_id}
Asunto: {ticket.subject}
Descripción: {ticket.description}
Prioridad: {ticket.priority or 'No especificada'}
Estado: {ticket.status or 'No especificado'}
Etiquetas: {', '.join(ticket.tags) if ticket.tags else 'No hay etiquetas'}

Proporciona un análisis que incluya:
1. Clasificación del tipo de ticket
2. Análisis del problema principal
3. Recomendaciones de solución
4. Sugerencias de seguimiento
5. Consideraciones adicionales basadas en la prioridad y estado
'''

        # Llamar a OpenAI para el análisis
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en soporte técnico y análisis de tickets de Zendesk."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return {
            "ticket_id": ticket.ticket_id,
            "analysis": response.choices[0].message['content']
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze-pdf")
async def analyze_pdf(pdf_file: UploadFile = File(...)):
    try:
        # Extraer texto del PDF
        pdf_text = extract_text_from_pdf(pdf_file)
        
        if not pdf_text:
            raise HTTPException(status_code=400, detail="No se pudo extraer texto del PDF")

        # Construir el prompt para el análisis
        prompt = f'''
Analiza el siguiente contenido extraído de un PDF y proporciona un análisis detallado:

{pdf_text}

Proporciona un análisis que incluya:
1. Resumen del contenido
2. Puntos clave identificados
3. Recomendaciones basadas en el contenido
4. Acciones sugeridas
5. Consideraciones importantes
'''

        # Llamar a OpenAI para el análisis
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de documentos y extracción de información relevante."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return {
            "filename": pdf_file.filename,
            "analysis": response.choices[0].message['content']
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"} 