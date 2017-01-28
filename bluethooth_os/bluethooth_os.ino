#include "SoftwareSerial.h"
SoftwareSerial serial_connection(13,12);
int button_up = 4;
int button_down = 5;
int button_left = 3;
int button_right = 6;
int button_send=8;
int button_bit1=11;
int button_bit2=10;
int button_bit3=9;
int leftclick = 2;
int rightclick = 7;
int Sersend = 0;
int Clicksend = 0;
int val=0;
int read_butup;
int read_butdown;
int read_butleft;
int read_butright;
int read_clkleft ;
int read_clkright ;
int read_send;
int read_bit1;
int read_bit2;
int read_bit3;
byte command;
void setup(){
  pinMode(button_up,INPUT);
  pinMode(button_down,INPUT);
  pinMode(button_left,INPUT);
  pinMode(button_right,INPUT);
  pinMode(leftclick,INPUT);
  pinMode(rightclick,INPUT);
  pinMode(button_send,INPUT);
  pinMode(button_bit1,INPUT);
  pinMode(button_bit2,INPUT);
  pinMode(button_bit3,INPUT);
  Serial.begin(9600);
  serial_connection.begin(9600);
}

void loop()
{
  
 read_butup = digitalRead(button_up); 
 read_butdown = digitalRead(button_down); 
 read_butleft = digitalRead(button_left); 
 read_butright = digitalRead(button_right); 
 read_clkleft = digitalRead(leftclick); 
 read_clkright = digitalRead(rightclick); 
 read_send = digitalRead(button_send);
 read_bit1 = digitalRead(button_bit1);
 read_bit2 = digitalRead(button_bit2);
 read_bit3 = digitalRead(button_bit3);
  //Serial.println(val);
  if(!read_butup){
    //Serial.println("88");
    serial_connection.println("88");
  }
  //else{Serial.print("");}
   else if(!read_butdown){
    //Serial.println("22");
    serial_connection.println("22");
  }
   else if(!read_butleft){
    //Serial.println("33");
    serial_connection.println("33");
  }
   else if(!read_butright){
    //Serial.println("77");
    serial_connection.println("77");
  }
  
   else if(!read_clkleft){
    //Serial.println("66");
    serial_connection.println("66");
  }
   else if(!read_clkright){
    //Serial.println("11");
    serial_connection.println("11");
  }
  delay(30);
  if(!read_send){
    if((read_bit3)&&(read_bit2)&&(read_bit1))
      command=B000;
    else if((read_bit3)&&(read_bit2)&&(!read_bit1))
      command=B001;
    else if((read_bit3)&&(!read_bit2)&&(read_bit1))
      command=B010;
    else if((read_bit3)&&(!read_bit2)&&(!read_bit1))
      command=B011;
    else if((!read_bit3)&&(read_bit2)&&(read_bit1))
      command=B100;
    else if((!read_bit3)&&(read_bit2)&&(!read_bit1))
      command=B101;
    else if((!read_bit3)&&(!read_bit2)&&(read_bit1))
      command=B110;
    else if((!read_bit3)&&(!read_bit2)&&(!read_bit1))
      command=B111;
    //Serial.println(command);
    serial_connection.println(command);
    delay(500);
  }
  
}
