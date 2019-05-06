const int buttonPin1 = 10;     // the number of the pushbutton pin
const int buttonPin2 =  9;  
const int buttonPin3 = 11;
const int buttonPin4 = 12;
const int buttonPin5 = 13;
void setup() {
  // put your setup code here, to run once:

  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin1, INPUT);
  //pinMode(buttonPin3, INPUT);
  //pinMode(buttonPin4, INPUT);
  //pinMode(buttonPin5, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
if(digitalRead(buttonPin1) == HIGH){
  Serial.println("1");
  delay(300);
}
else if(digitalRead(buttonPin2) == HIGH){
  Serial.println("2");
  delay(300);
  }
else if(digitalRead(buttonPin3) == HIGH){
  Serial.println("3");
  delay(300);
  }
else if(digitalRead(buttonPin4) == HIGH){
  Serial.println("4");
  delay(300);
  }
else if(digitalRead(buttonPin5) == HIGH){
  Serial.println("5");
  delay(300);
  }
}
