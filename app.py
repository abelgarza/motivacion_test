from flask import Flask, render_template
import random

app = Flask(__name__)

frases_motivadoras = [
  "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
  "No esperes oportunidades, crea las tuyas.",
  "Si puedes soñarlo, puedes lograrlo.",
  "Cree en ti mismo y todo será posible.",
  "Cada día es una oportunidad para ser mejor.",
  "No hay nada imposible, la palabra misma lo dice: 'soy posible'.",
  "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.",
  "Atrévete a ser diferente y a ser libre.",
  "El fracaso es una gran oportunidad para empezar de nuevo con más inteligencia.",
  "Tu tiempo es limitado, no lo desperdicies viviendo la vida de otro.",
  "Si no te gusta algo, cámbialo. Si no puedes cambiarlo, cambia tu actitud.",
  "No te rindas, cada fracaso es una oportunidad para comenzar de nuevo.",
  "El camino hacia el éxito está siempre en construcción.",
  "No te compares con nadie más, sé tu propia competencia.",
  "Nunca es tarde para ser lo que podrías haber sido.",
  "La única forma de hacer un gran trabajo es amando lo que haces."
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/frase-motivadora')
def frase_motivadora():
    frase = random.choice(frases_motivadoras)
    return render_template('frase_motivadora.html', frase=frase)

if __name__ == '__main__':
    app.run(debug=True)
