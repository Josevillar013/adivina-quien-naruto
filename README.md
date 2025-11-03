# adivina-quien-naruto

🌀 README.txt — Akinator de Naruto

Autor: [Tu nombre aquí]
Proyecto: Akinator de Naruto
Lenguaje: Python 3

Descripción:
Juego tipo Akinator basado en el universo de Naruto Shippuden.
El jugador piensa en un personaje, y el programa hace preguntas de “sí” o “no” hasta adivinarlo.
Incluye imágenes y puede ejecutarse tanto desde consola como desde Jupyter Notebook.

------------------------------------------------------------
📁 Estructura de carpetas

AkinatorNaruto/
│
├── akinator_naruto.py          ← código principal
├── conocimiento.json            ← base de conocimiento (preguntas y personajes)
├── Akinator_Naruto.ipynb        ← versión para Jupyter Notebook
│
└── imagenes/                    ← carpeta con imágenes (.png)
     ├── naruto_uzumaki.png
     ├── sasuke_uchiha.png
     ├── sakura_haruno.png
     ├── hinata_hyuga.png
     ├── ...

⚠️ Importante:
El nombre de cada imagen debe coincidir con el personaje, en minúsculas y con guiones bajos.
Ejemplo:
"Naruto Uzumaki" → naruto_uzumaki.png
"Itachi Uchiha" → itachi_uchiha.png

------------------------------------------------------------
▶️ OPCIÓN 1 – Ejecutar desde consola

1. Asegúrate de tener Python 3 instalado.
   (Puedes verificarlo con python --version o python3 --version).
2. Abre una terminal en la carpeta del proyecto:
   cd ruta/donde/guardaste/AkinatorNaruto
3. Ejecuta el juego:
   python akinator_naruto.py
4. Sigue las instrucciones en pantalla y responde con “si” o “no”.
   Cuando adivine tu personaje, se abrirá una ventana con su imagen.

------------------------------------------------------------
▶️ OPCIÓN 2 – Ejecutar desde Jupyter Notebook

1. Abre el archivo Akinator_Naruto.ipynb en Jupyter o VSCode.
2. Ejecuta cada celda en orden (Shift + Enter).
3. Contesta las preguntas con “si” o “no”.
4. Las imágenes se mostrarán directamente dentro del notebook.

------------------------------------------------------------
💾 OPCIONAL – Subir a itch.io o GitHub

1. Comprime toda la carpeta en un archivo .zip
   AkinatorNaruto.zip
2. Incluye dentro del ZIP:
   - akinator_naruto.py
   - conocimiento.json
   - Akinator_Naruto.ipynb
   - Carpeta imagenes/
   - Este archivo README.txt

------------------------------------------------------------
💡 Créditos y mejoras futuras

- Proyecto educativo para práctica de inteligencia artificial básica.
- Posibles mejoras:
  - Añadir más personajes.
  - Guardar lo aprendido en conocimiento.json.
  - Crear versión web con Gradio para publicación interactiva en itch.io.
