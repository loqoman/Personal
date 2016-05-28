
/*
* Getting Started example sketch for nRF24L01+ radios
 * This is a very basic example of how to send data from one node to another
 * Updated: Dec 2014 by TMRh20
 */

/*
*--------------------Notes---------------------
 *Rewrite code so that it filters out packets that dont start in T or H or something.
 * This way we filter out the 
 */

#include <SPI.h>
#include "RF24.h"

/****************** User Config ***************************/
/***      Set this radio as radio number 0 or 1         ***/
bool radioNumber = 0;
int message = 10001;

/* Hardware configuration: Set up nRF24L01 radio on SPI bus plus pins 7 & 8 */
RF24 radio(7,8);
/***************0*******************************************/

byte addresses[][6] = {
  "1Node","2Node"};

// Used to control whether this node is sending or receiving
bool role = 1;// 1 is talker, 0 is non-talker

void setup() {
  
  Serial.begin(115200);
  Serial.println(F("Personal/C/Arudio/Wireless_Transmitter"));

  radio.begin();

  // Set the PA Level low to prevent power supply related issues since this is a
  // getting_started sketch, and the likelihood of close proximity of the devices. RF24_PA_MAX is default.
  radio.setPALevel(RF24_PA_LOW);

  // Open a writing and reading pipe on each radio, with opposite addresses
  if(radioNumber){
    radio.openWritingPipe(addresses[1]);
    radio.openReadingPipe(1,addresses[0]);
  }
  else{
    radio.openWritingPipe(addresses[0]);
    radio.openReadingPipe(1,addresses[1]);
  }

  // Start the radio listening for data
}

void loop() {


  /****************** Ping Out Role ***************************/
  if (role == 1)  { //HEHE! IM THE TALKER!!!

    Serial.println(F("Now sending"));

    unsigned long start_time = micros();                       //Take the time, and send it.  This will block until complete
    if (!radio.write( &message, sizeof(int) )){
      Serial.println(F("failed"));                             //If for some reason we can not send it 
    }
    
    boolean timeout = false;                                   //Set up a variable to indicate if a response was received or not

    // Try again 1s later
    delay(1000);
  }



} // Loop


