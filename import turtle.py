import turtle # Aqui estamos important uma bliblioteca do Python para gerar graficos simples para nosso jogo.

# Configuração da tela
window = turtle.Screen() # Window é o nome do meu objeto e "turtle.Screen" e o tipo de objeto que vem diretamente da bliblioteca importada.
window.title("Pong Simples - Python") # Aqui temos o titulo da janela.
window.bgcolor("black") # Definimos a cor para minha janela.
window.setup(width=1200, height=600) # Dimenções da minha janela.
window.tracer(0) #Trava as animações até que eu de um comando.

# Raquete A -> O código a baixo define as caracteristicas de nossa raquete.
paddle_a = turtle.Turtle() #Novamente estamos criando um objeto.Imaagine que turtle com a letra minusccula é uma caixa cheia de tartarugas e Turtle com letra maiuscula é como se voce estivesse pegando uma dessas tartaugas e chamando dela de paddle_a. Então essa tartaruga, agora vai virar nossa raquete!
paddle_a.speed(2) #Aqui definimos a velocidade de nossa raquete.
paddle_a.shape("square") #qual a forma de nossa raquete?
paddle_a.color("white") #qual a cor de nossa raquete?
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Aqui estamos definindo o tamanho de nossa raquete em pixels.
paddle_a.penup() #Essa linha em especifico serve apenas para evitar que fique um rastro quando nossa raquete se mover.
paddle_a.goto(-300, 0) # Define o posicionamento de nossa raquete na tela, jogando ela para a esqueda.

# Raquete B -> Considere as mesmas informações a cima.
paddle_b = turtle.Turtle()
paddle_b.speed(2)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(300, 0)

# Bola -> Aqui vamos começar a definir as caracteristicas de nossa bola, La ele.
ball = turtle.Turtle()#Novamente estamos criando um objeto.Mas agora ela se chama paddle_b. Então essa tartaruga, agora vai virar nossa bola.
ball.speed(0) #velocidade de nossa bola.
ball.shape("circle") #Formado de nossa bola.
ball.color("white") #cor de nossa bola.
ball.penup() #Assim como nos blcos anteriores, esse comando serve apenas para não termos rastros na tela.
ball.goto(0, 0) #Aqui temos a posição inicial de nossa bola.
ball.dx = 0.05  #Movimento em X (velocidade)
ball.dy = 0.05  #Movimento em Y (velocidade)
score_a=0 #Aqui vamos guardar o placar.
score_b=0 #Aqui vamos guardar o placar.

pen = turtle.Turtle() #aqui criamos o placar do nosso jogo.
pen.speed(0) #velocidade da animação do placar.
pen.color("white") #cor do placar.
pen.penup() # A essa altura voces ja sabem o que essa linha faz.
pen.hideturtle() # Esconde a seta do objeto, queremos só o texto
pen.goto(0, 260) #posição do placar na tela.
pen.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 24, "normal")) #O que nosso placar vai escrever.

# Funções de movimento
def paddle_a_up(): #Define quem vai se mover e para onde vai se mover.
    y = paddle_a.ycor() #verifica a altura da raquete A.
    if y < 250: paddle_a.sety(y + 20) # O começo define o limite até onde nossa raquete pode subir na tela.Ja a segunda parte verifica a posição atual e soma mais 20 pixels nela, dando a iluzão de movimento.

def paddle_a_down():#mesma coisa do de cima, so que pra baixo.
    y = paddle_a.ycor()
    if y > -250: paddle_a.sety(y - 20)

def paddle_b_up():# A mesma coisa que a raquete A.
    y = paddle_b.ycor() 
    if y < 250: paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250: paddle_b.sety(y - 20)

# Mapeamento do teclado -> Capta e define as teclas de comando
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Loop principal do jogo -> Esse é o loop responsavel por manter noso jogo rodando o tempo todo.
while True:
    window.update()
    
    # Mover a bola
    ball.setx(ball.xcor() + ball.dx) #pergunta ao codigo qual o atual posicionamento da bola no eixo X e soma um valor a ele para fazer a bola andar na tela.
    ball.sety(ball.ycor() + ball.dy)#pergunta ao codigo qual o atual posicionamento da bola no eixo X e soma um valor a ele para fazer a bola andar na tela.

    # Colisão com bordas superiores/inferiores
    if ball.ycor() > 290 or ball.ycor() < -290: # Verifica se a bola batel no limite da tela.
        ball.dy *= -1 #se a bola bater na bosda, o valor da posição da bola sera multiplicado por -1, tornando-onegativo e jogando a bola para o outro lado.

    # Marcar ponto (Borda esquerda/direita)
   # Marcar ponto (Borda Direita - Ponto do Jogador A)
    if ball.xcor() > 390: #verifica se a bola ultrapassou a margem da direita, se passar marca ponto para o jogador da esqueda.
        ball.goto(0, 0) #caso a bola passe da margem, redefine o posicionamento da bola para 0.
        ball.dx *= -1 #inverte  a direção em que a bola estava se movendo.
        score_a += 1 #soma 1 ao valor atal dos pontos do jogador A.
        pen.clear() # Limpa o placar antigo para que um valor não seja escrito um por cima do outro.
        pen.write(f"Jogador A: {score_a}  Jogador B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Marcar ponto (Borda Esquerda - Ponto do Jogador B)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_b += 1
        pen.clear() # Limpa o placar antigo
        pen.write(f"Jogador A: {score_a}  Jogador B: {score_b}", align="center", font=("Courier", 24, "normal"))
    

    # Colisão com as raquetes
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1