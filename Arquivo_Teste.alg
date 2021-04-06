algoritmo "Calculadora"
var
   calc, N1, N2: real
   Esc: inteiro

inicio
      Escreva ("        Calculadora         ")
      Enquanto (calc >= -10000000000000000000   ) faca
               EscrevaL
               EscrevaL
               EscrevaL("Selecione uma das op��es aritimeticas abaixo:")
               Escreval
               Escreval("Digite 1 para soma")
               Escreval("Digite 2 para subtra��o")
               Escreval("Digite 3 para multiplica��o")
               EscrevaL("Digite 4 para divis�o")
               Escreval("Digite 5 para potencia ao quadrado")
               Escreval("Digite 6 para potencia ao cubo")
               EscrevaL("Digite 0 para sair")
               Escreva("Sua escolha �: ")
               Leia(calc)
               Escreval
               Escreva(" Digite o primeiro numero: ")
               Leia(N1)
               escreval
               Escreva("ALERTA: Em caso de potencia o segundo numero ser� sempre 0")
               EscrevaL
               Escreval
               Escreva(" Digite o segundo numero: ")
               Leia(N2)
               Escreval

                       Se (calc >= 7 ) entao
                       Escreval(" operador invalido! ")
                       Escreval
                       FimSe


      Escolha calc
              Caso 1
              calc <- N1 + N2
                   Escreva("o resultado �: ",calc)
                   Escreval
              Caso 2
              calc <- N1 - N2
                   Escreva("O resultado �: ",calc)
                   Escreval
              caso 3
              calc <- N1 * N2
                   Escreva("O resultado �: ",calc)
                   Escreval
              Caso 4
              calc <- N1 / N2
                   Escreva("O resultado �: ",calc)
                   Escreval
              caso 0
              calc <- N1 - 1000000000000000000000
                   Escreva("Saindo ....")
                   Escreval
              Caso  5
                   calc <- N1 * N1
                   Escreva("O resultado �: ",calc)
                   Escreval
                   
              Caso 6
                   calc <- N1 * N1 * N1
                   Escreva("O resultado �: ",calc)
                   Escreval
      FimEscolha

      FimEnquanto
fimalgoritmo
