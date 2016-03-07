const byte pHpin = A0;    // Connect the sensor's Po output to analogue pin 0.

float Po;
float a=.027;
float b=-6.824;
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    Po = (1023 - analogRead(pHpin)) ;
    Serial.print("Raw: "); 
    Serial.print(Po, 2);                      // Print the result in the serial monitor.
    Serial.print(", ph =");
    Po=Po*a+b;
    Serial.println(Po, 2);                    // print ph
    delay(1000);                              // Take 1 reading per second.
}
