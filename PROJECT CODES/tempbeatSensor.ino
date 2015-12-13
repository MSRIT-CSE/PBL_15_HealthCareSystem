int outputpin= 0; 
float celsius=0.0;
int rawvoltage=0;
const int analogIn = A1;

void setup() 
{ 
 Serial.begin(9600); 
 
} 
void loop() 
{ 

int rawvoltage= analogRead(analogIn); 
int sensorValue = analogRead(A0);
float millivolts= (rawvoltage/1024.0) * 5000; 
float celsius= rawvoltage*0.0583497053;
float voltage = sensorValue * (5.0 / 1023.0);
 // Serial.print("sensor = " );                       
//  Serial.print(rawvoltage);      
//  Serial.print("\t output = ");    
  Serial.print(celsius);
  Serial.print(" ");
  Serial.println(voltage); 


 
delay(1000); 
}
