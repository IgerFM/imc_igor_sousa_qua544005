#SECTION - Flask
from flask import Flask, render_template, request #!SECTION

app = Flask(__name__)

#SECTION - Rotas
@app.route("/", methods = ['GET','POST'])
def index():
    massa = None
    altura = None
    diagnostico = None
    result = None

    if request.method == 'POST':
        massa = float(request.form.get('massa','').replace(',','.'))
        altura = float(request.form.get('altura','').replace(',','.'))
        imc = massa/(altura**2)
        if imc < 18.5:
            diagnostico = f'Você atualmente esta em um estado de Magreza, Se cuide, pois não é saudavel permanecer neste estado'

        elif imc >= 18.5 and imc <= 24.9:
            diagnostico = f'Você atualmente esta em um estado Normal\n\n Parabens!!! Continue saudavel assim!'

        elif imc >= 25 and imc <= 29.9:
            diagnostico = f'Você atualmente esta em um estado de Sobrepeso\n\nSe cuide, pois não é saudavel permanecer neste estado'

        elif imc >= 30 and imc <= 34.9:
            diagnostico = f'Você atualmente esta em um estado de Obesidade grau I\n\nSe cuide, pois não é saudavel permanecer neste estado'

        elif imc >= 35 and imc <= 40:
            diagnostico = f'Você atualmente esta em um estado de Obesidade grau II\n\nSe cuide, pois não é saudavel permanecer neste estado'

        elif imc > 40:
            diagnostico = f'Você atualmente esta em um estado de Obesidade grau III\n\nSe cuide, pois não é saudavel permanecer neste estado'

        else:
            diagnostico = f'Algo deu errado'

        result = f"Seu IMC é {imc:.2f}.\n{diagnostico}"

    return render_template("index.html", result=result)


#!SECTION


#SECTION - Runner
if __name__ == "__main__":
    app.run(debug=True) #!SECTION