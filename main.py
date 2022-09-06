from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])


def cadastro():
    variavel = "Aprovando Empréstimos"

    if request.method == 'GET':
     return render_template("cadastro.html", cadastro=variavel)
    
    else:
        valorcasa = int(request.form.get('valorcasa'))
        salario = int(request.form.get('salario'))
        parcelas = int(request.form.get('anospagar'))
        calculo = valorcasa/parcelas 
        porcentagem = salario*0.3
        
        if calculo >= porcentagem:     
            return "Seu Empréstimo foi negado! o resultado deu R$%.2f por parcela, ultrapassando 30 porcento do sálário!" % calculo  
            
        else:
            return f"Seu Empréstimo foi Aceito, PARABÉNS! o resultado deu R${calculo} por parcela, É menor que 30% do sálário!" 
            

@app.route('/<string:nome>')  


def erro(nome):
    variavel = f'Página ({nome}) não existe'
    return render_template('erro.html', variavel2=variavel)


if __name__ == '__main__':
  app.run(debug=True)
