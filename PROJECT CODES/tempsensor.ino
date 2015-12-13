int outputpin= 0; 
float celsius=0.0;
int rawvoltage=0;
const int analogIn = A0;

void setup() 
{ 
 Serial.begin(9600); 
 
} 
void loop() 
{ 

int rawvoltage= analogRead(analogIn); 
float millivolts= (rawvoltage/1024.0) * 5000; 
float celsius= rawvoltage*0.0583497053;
  Serial.print("sensor = " );                       
  Serial.print(rawvoltage);      
  Serial.print("\t output = ");    
  Serial.println(celsius); 


 
delay(1000); 
}
