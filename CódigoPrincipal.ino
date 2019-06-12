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
    botoes();
    //imprime mensagem no LCD e inicia os botões
  }

  void mensagemnegada()   //###### QUANDO DÁ ERRO ######
{
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
      
      if(digitalRead(buttonPin1) == HIGH)
      {
        lcd.clear();
        lcd.print("Estressado");
        Serial.println("1");
        delay(1000);
        apertou = 1;
       mensagemInicial();
      }
      else if(digitalRead(buttonPin2) == HIGH)
      {
        lcd.clear();
        lcd.print("Ansioso");
        Serial.println("2");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin3) == HIGH)
      {
        lcd.clear();
        lcd.print("Neutro");
        Serial.println("3");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin4) == HIGH)
      {
        lcd.clear();
        lcd.print("Feliz");
        Serial.println("4");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }
      else if(digitalRead(buttonPin5) == HIGH)
      {
        lcd.clear();
        lcd.print("Triste");
        Serial.println("5");
        delay(1000);
        apertou = 1;
        mensagemInicial();
      }

    }
}
  
void setup() 
{
  Serial.begin(9600);   // Inicia a serial
  
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  lcd.begin(16, 2);  //Define o número de colunas e linhas do LCD:
  mensagemInicial();
}
 
void loop() 
{
  String ID;
  String tag_lida;
  if(Serial.available() > 0) //lê a porta serial para um valor maior que zero.
  {
    ID = Serial.readString();

    ID = ID.substring(1, 13);

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
