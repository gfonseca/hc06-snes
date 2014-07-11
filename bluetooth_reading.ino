
char command[20];
int index = 0;
int c = 0;

void setup(){

  Serial.begin(9600);
}

void loop(){
  index = 0;
  while(c = Serial.read() != -1){
    c = Serial.read();
    command[index] = c;
    index ++;
    command[index] = '\0';
  }
  Serial.print("ok +");
  Serial.println(command);
  delay(1000);
}
