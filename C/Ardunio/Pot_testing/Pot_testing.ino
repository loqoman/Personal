
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int Pot = 0;
int Pot2 = 1;
int Py = 2;
int Pswitch = 2;
int Pbutton = 3;
int P;
char test = 1;
int but;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(115200);
  pinMode(Pswitch,INPUT);
  digitalWrite(Pswitch, HIGH);//Puts up the pull-up resistor. reounds up unless it gets gnd 
  pinMode(Pbutton,INPUT);
  //digitalWrite(Pbutton,HIGH);
}
// Function to sync up with master by exchanging 'I' for "Initial"
void establishcontact(){  
   while (Serial.available() <= 0) {
    Serial.write('I');
    delay(1000);  //Wait 1 second to try again
  } 
    char inByte = Serial.read(); // Receive the echoed 'I' for initialized

}

// Function to get next command from the master
char getcommand(){
  char inbyte;
  while (Serial.available() <= 0) { // read byte when available
  }
  return Serial.read();  // Return the command from the master
}


// the loop routine runs over and over again forever:
void loop() {
    
  establishcontact();
  while (true) {
   
    // Get a command 
    char command = getcommand();

    // Handle commands
    switch (command) {
      case ('0'):  // Analog scan request
        Pot = analogRead(0);
        Serial.print('0');
        Serial.println(Pot);
        //Serial.println();
        //delay(1);
        break;
      case ('1'):
        Pot = analogRead(1);
        Serial.print('1');
        Serial.println(Pot);
        //delay(1);
        break;
      case ('2'):
        P = digitalRead(2);
        Serial.print('2');
        Serial.println(P);
        break;
      case ('3'):
        but = digitalRead(3);
        //Serial.print('3');
        Serial.println(but);
        break;
      default: 
        break;
    
   }
  }
}
  
  
  
  


  
