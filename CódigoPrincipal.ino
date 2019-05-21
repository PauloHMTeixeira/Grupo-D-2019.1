#include <FastIO.h>
#include <Wire.h>
#include <I2CIO.h>
#include <LCD.h>
#include <LiquidCrystal.h>
#include <LiquidCrystal_I2C.h>


LiquidCrystal_I2C lcd(0x3F,2,1,0,4,5,6,7,3, POSITIVE); 

const int buttonPin1 = 2;     // pin do botão
const int buttonPin2 = 3;  
const int buttonPin3 = 4;
const int buttonPin4 = 5;
const int buttonPin5 = 6;

void mensagemInicial()
{
  lcd.clear();
  lcd.setCursor(4,0);
  lcd.print("Aproxime");  
  lcd.setCursor(4,1);
  lcd.print("seu cracha");
  Serial.print("funcionando");
}

void mensagemaprovada()   //###### QUANDO CARTÃO É APRESENTADO ######
{
    //Serial.println("Proximo passo");
    //Serial.println();
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Olá!");
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Como voce esta");
    lcd.setCursor(0,1);
    lcd.print("se sentindo ?");
    delay(1000);
    Serial.println("antes dos botoes");
    botoes(); 
    Serial.println("depois dos botoes");
    //imprime mensagem no LCD e inicia os botões
  }

  void mensagemnegada()   //###### QUANDO DÁ ERRO ######
{
    Serial.println("Olá!");
    Serial.println();
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print(" Cartão Detectado! ");
    lcd.setCursor(0,1);
    lcd.print(" Accesso Negado! ");
    delay(3000);
    mensagemInicial();
  }

  void botoes()
  {
    bool apertou= 0; //botão começa com valor booleano "False"
    
    while (!apertou){ // quando for diferente de "False"
      if(digitalRead(buttonPin1) == HIGH){
        lcd.clear();
        lcd.print("Estressado");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin2) == HIGH)
      {
        lcd.clear();
        lcd.print("Ansioso");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin3) == HIGH)
      {
        lcd.clear();
        lcd.print("Neutro");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin4) == HIGH)
      {
        lcd.clear();
        lcd.print("Feliz");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin5) == HIGH)
      {
        lcd.clear();
        lcd.print("Triste");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
    }
}
  
void setup() 
{
  Serial.begin(9600);   // Inicia a serial
  Serial.print("Aproxime o seu crachá do leitor...");
  Serial.println();
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  //Serial.println("lcd off");
  lcd.begin(16, 2);  //Define o número de colunas e linhas do LCD:
  //Serial.println("lcd on");
  mensagemInicial();
}
 
void loop() 
{
  String ID;
  String tag_lida;
  if(Serial.available() > 0) //lê a porta serial para um valor de "tag" maior que zero.
  {
    ID = Serial.readString(); //armazena tag do cracha na variável ID
  
    tag_lida = ID;
    Serial.println(ID);
  
    if (tag_lida == ID) 
    {
      mensagemaprovada(); 
    }
  
    if (tag_lida != ID) 
    {
      mensagemnegada();
    }
   }
 }
