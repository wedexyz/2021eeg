#define pinMotorA 9
#define pinMotorB 10

#define pinMotorC 6
#define pinMotorD 5
 
bool motorMaju = false;
bool motorHidup = false;
char chrKecepatan[5];
byte Kecepatan;
 
void setup() {
  Serial.begin(9600);
  Serial.println("Mengatur kecepatan motor DC 5V menggunakan PWM dilengkapi aksi maju-mundur");
  Serial.println("dengan rangkaian sederhana menggunakan Arduino dan 4 transistor");
  Serial.println("entri [M] untuk maju");
  Serial.println("entri [m] untuk mundur");
  Serial.println("entri [Kxxx] untuk set kecepatan, xxx = 0 s/d 255");
  Serial.println("entri [+] untuk menambah kecepatan 10 angka");
  Serial.println("entri [-] untuk kurangi kecepatan 10 angka");
  Serial.println("entri [B] untuk berhenti");

 
  pinMode(pinMotorA, OUTPUT);
  pinMode(pinMotorB, OUTPUT);
  pinMode(pinMotorC, OUTPUT);
  pinMode(pinMotorD, OUTPUT);
}
 
void loop() {
  if(Serial.available())
  {
    char c = Serial.read();
    /*
    if(c == 'M')
    {
      motorMaju = true;
      Serial.println("Motor maju");
      motorHidup = true;
    }
     else if(c == 'm')
    {
      motorMaju = false;
     Serial.println("Motor mundur");
      Motor = true;
    }
    */
   if(c == 'M')
    {

digitalWrite(pinMotorB, LOW);
digitalWrite(pinMotorC, LOW);
analogWrite(pinMotorA, Kecepatan);
analogWrite(pinMotorD, Kecepatan);
    }
      if(c == 'R')
    {
  
 digitalWrite(pinMotorB, LOW);
 digitalWrite(pinMotorD, LOW);
 analogWrite(pinMotorA, Kecepatan);
 analogWrite(pinMotorC, Kecepatan);
    } 
      if(c == 'L')
    {
  
 digitalWrite(pinMotorA, LOW);
 digitalWrite(pinMotorC, LOW);
 analogWrite(pinMotorB, Kecepatan);
 analogWrite(pinMotorD, Kecepatan);
    } 



    
    else if(toupper(c) == 'K')
    {
      delay(10);
      Serial.readBytesUntil('\n', chrKecepatan, sizeof(chrKecepatan));
      Kecepatan = String(chrKecepatan).toInt();
      Serial.print("Set kecepatan = ");
      Serial.println(Kecepatan);
    }
    else if(c == '+')
    {
      if(Kecepatan <= 245)
      {
        Kecepatan += 10;
      }
      Serial.print("Set kecepatan = ");
      Serial.println(Kecepatan);
    }
    else if(c == '-')
    {
      if(Kecepatan >= 10)
      {
        Kecepatan -= 10;
      }
      Serial.print("Set kecepatan = ");
      Serial.println(Kecepatan);
    }
    else if(toupper(c) == 'B')
    {
      digitalWrite(pinMotorA, LOW);
      digitalWrite(pinMotorB, LOW);
      
      digitalWrite(pinMotorC, LOW);
      digitalWrite(pinMotorD, LOW);
      motorHidup = false;
      Serial.println("Motor berhenti");
    }
  }
  /*
  if(motorHidup)
  {
    if(motorMaju)
    {
      digitalWrite(pinMotorB, LOW);
      analogWrite(pinMotorA, Kecepatan);
      digitalWrite(pinMotorC, LOW);
      analogWrite(pinMotorD, Kecepatan);
    }
    else
    {
      digitalWrite(pinMotorA, LOW);
      analogWrite(pinMotorB, Kecepatan);
      
      digitalWrite(pinMotorD, LOW);
      analogWrite(pinMotorC, Kecepatan);
    }

    
  }
  */
  
 
}
