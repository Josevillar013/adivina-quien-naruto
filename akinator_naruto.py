#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Akinator de Naruto - versión para GitHub Codespaces
✅ Incluye 32 personajes
❌ No usa Tkinter; muestra imágenes en HTML/Jupyter
"""

import json
import os
import IPython.display as display
from IPython.display import Image as IPImage

IMAGENES_DIR = "imagenes"

# ------------------------
# BLOQUE DE CONOCIMIENTO INICIAL
# ------------------------
DEFAULT_KNOWLEDGE = {
    "pregunta": "¿Tu personaje pertenece a la Aldea de la Hoja?",
    "si": {
        "pregunta": "¿Tu personaje es un héroe principal?",
        "si": {
            "pregunta": "¿Tu personaje tiene el Kyubi dentro?",
            "si": "Naruto Uzumaki",
            "no": {
                "pregunta": "¿Tu personaje tiene Sharingan?",
                "si": "Sasuke Uchiha",
                "no": {
                    "pregunta": "¿Tu personaje es chica?",
                    "si": {
                        "pregunta": "¿Tu personaje tiene cabello rosa?",
                        "si": "Sakura Haruno",
                        "no": "Hinata Hyuga"
                    },
                    "no": {
                        "pregunta": "¿Tu personaje usa gafas y tiene vestimenta verde?",
                        "si": "Rock Lee",
                        "no": {
                            "pregunta": "¿Tu personaje pertenece al clan Hyuga?",
                            "si": "Neji Hyuga",
                            "no": "Tenten"
                        }
                    }
                }
            }
        },
        "no": {
            "pregunta": "¿Tu personaje es un sensei o Jonin?",
            "si": {
                "pregunta": "¿Tu personaje tiene cabello verde y es experto en taijutsu?",
                "si": "Might Guy",
                "no": {
                    "pregunta": "¿Tu personaje es miembro del clan Sarutobi?",
                    "si": "Asuma Sarutobi",
                    "no": {
                        "pregunta": "¿Tu personaje es médico ninja?",
                        "si": "Kurenai Yuhi",
                        "no": {
                            "pregunta": "¿Tu personaje es uno de los legendarios Sannin?",
                            "si": {
                                "pregunta": "¿Tu personaje tiene cabello blanco y gran nariz?",
                                "si": "Jiraiya",
                                "no": {
                                    "pregunta": "¿Tu personaje es mujer con cabello rubio?",
                                    "si": "Tsunade",
                                    "no": "Minato Namikaze"
                                }
                            },
                            "no": "Yamato"
                        }
                    }
                }
            },
            "no": {
                "pregunta": "¿Tu personaje es otro ninja conocido?",
                "si": {
                    "pregunta": "¿Tu personaje es de la Arena?",
                    "si": "Gaara",
                    "no": "Shikamaru Nara"
                },
                "no": None
            }
        }
    },
    "no": {
        "pregunta": "¿Tu personaje pertenece a Akatsuki?",
        "si": {
            "pregunta": "¿Tu personaje tiene Sharingan?",
            "si": "Itachi Uchiha",
            "no": {
                "pregunta": "¿Tu personaje tiene aspecto acuático?",
                "si": "Kisame Hoshigaki",
                "no": {
                    "pregunta": "¿Tu personaje usa explosivos o marionetas?",
                    "si": {
                        "pregunta": "¿Tu personaje es un maestro de marionetas?",
                        "si": "Sasori",
                        "no": "Deidara"
                    },
                    "no": {
                        "pregunta": "¿Tu personaje tiene dos cabezas o cuerpo extraño?",
                        "si": {
                            "pregunta": "¿Tu personaje tiene aspecto ritualista?",
                            "si": "Hidan",
                            "no": "Kakuzu"
                        },
                        "no": {
                            "pregunta": "¿Tu personaje es líder de Akatsuki?",
                            "si": "Pain",
                            "no": "Konan"
                        }
                    }
                }
            }
        },
        "no": {
            "pregunta": "¿Tu personaje es villano legendario?",
            "si": {
                "pregunta": "¿Tu personaje es científico o médico?",
                "si": "Kabuto Yakushi",
                "no": {
                    "pregunta": "¿Tu personaje es maestro de jutsus prohibidos?",
                    "si": "Orochimaru",
                    "no": {
                        "pregunta": "¿Tu personaje tiene Sharingan y aspiraciones de dominar el mundo?",
                        "si": {
                            "pregunta": "¿Tu personaje usa máscara?",
                            "si": "Obito Uchiha",
                            "no": "Madara Uchiha"
                        },
                        "no": "Kaguya Otsutsuki"
                    }
                }
            },
            "no": {
                "pregunta": "¿Tu personaje es planta/alien o mitad vegetal?",
                "si": "Zetsu",
                "no": None
            }
        }
    }
}

# ------------------------
# FUNCIONES
# ------------------------

def normalizar_nombre(personaje: str) -> str:
    return personaje.strip().lower().replace(" ", "_")

def mostrar_imagen(personaje: str):
    """Muestra imagen si existe (HTML / Codespaces / Jupyter)."""
    nombre_archivo = normalizar_nombre(personaje) + ".png"
    ruta = os.path.join(IMAGENES_DIR, nombre_archivo)
    if os.path.exists(ruta):
        display.display(IPImage(filename=ruta))
    else:
        print(f"(No se encontró imagen para {personaje})")

def pedir_si_no(pregunta: str) -> str:
    while True:
        r = input(pregunta + " (si/no): ").strip().lower()
        if r in ("si", "no"):
            return r
        print("Por favor responde 'si' o 'no'.")

def jugar_nodo(nodo):
    if isinstance(nodo, str):
        r = pedir_si_no(f"¿Tu personaje es {nodo}?")
        if r == "si":
            print(f"🎉 ¡Lo adiviné! Tu personaje es {nodo}.\n")
            mostrar_imagen(nodo)
            return nodo
        else:
            nuevo = input("¿En qué personaje estabas pensando?: ").strip()
            nueva_pregunta = input(f"Escribe una pregunta que diferencie a {nuevo} de {nodo}:\n")
            respuesta_nuevo = pedir_si_no(f"Si fuera {nuevo}, ¿la respuesta sería 'si'? ")
            if respuesta_nuevo == "si":
                return {"pregunta": nueva_pregunta, "si": nuevo, "no": nodo}
            else:
                return {"pregunta": nueva_pregunta, "si": nodo, "no": nuevo}
    else:
        r = pedir_si_no(nodo["pregunta"])
        if r == "si":
            nodo["si"] = jugar_nodo(nodo["si"])
        else:
            nodo["no"] = jugar_nodo(nodo["no"])
        return nodo

# ------------------------
# MAIN
# ------------------------

def main():
    print("=====================================")
    print("   AKINATOR DE NARUTO - CODESPACES 🌀")
    print("=====================================\n")
    print("Piensa en un personaje del universo Naruto y responde con 'si' o 'no'.\n")

    conocimiento = DEFAULT_KNOWLEDGE

    while True:
        conocimiento = jugar_nodo(conocimiento)

        seguir = input("\n¿Quieres jugar otra vez? (si/no): ").strip().lower()
        if seguir != "si":
            print("¡Gracias por jugar! 🍥")
            break

if __name__ == "__main__":
    main()
