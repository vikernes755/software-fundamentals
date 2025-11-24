//Brayan Cortés de la Cruz
//Juan David Burbano Mejia 
//Angel Damian Bravo Enriquez
//Norvy Alejandra García Lara

const int BATHROOM_LIGHT = 11;
const int BEDROOM_LIGHT = 10;
const int KITCHEN_LIGHT = 9;

// Light states
bool bathroom_state = LOW;
bool bedroom_state  = LOW;
bool kitchen_state  = LOW;

bool blinking_mode = false;

void menu() {
  Serial.println("[1] Turn ON bathroom light");
  Serial.println("[2] Turn OFF bathroom light");
  Serial.println("[3] Turn ON bedroom light");
  Serial.println("[4] Turn OFF bedroom light");
  Serial.println("[5] Turn ON kitchen light");
  Serial.println("[6] Turn OFF kitchen light");
  Serial.println("[7] Turn ON all lights");
  Serial.println("[8] Turn OFF all lights");
  Serial.println("[9] Activate infinite blinking mode");
}

void setup() {
  pinMode(BATHROOM_LIGHT, OUTPUT);
  pinMode(BEDROOM_LIGHT, OUTPUT);
  pinMode(KITCHEN_LIGHT, OUTPUT);

  Serial.begin(9600);
  menu();
}

void loop() {

  
  if (Serial.available() > 0) {
    char opt = Serial.read();

    switch (opt) {

      case '1': bathroom_state = HIGH; break;
      case '2': bathroom_state = LOW; break;

      case '3': bedroom_state = HIGH; break;
      case '4': bedroom_state = LOW; break;

      case '5': kitchen_state = HIGH; break;
      case '6': kitchen_state = LOW; break;

      case '7':
        bathroom_state = HIGH;
        bedroom_state  = HIGH;
        kitchen_state  = HIGH;
        break;

      case '8':
        bathroom_state = LOW;
        bedroom_state  = LOW;
        kitchen_state  = LOW;
        blinking_mode = false;  
        break;

      case '9':
      
        blinking_mode = true;


        bathroom_state = HIGH;
        bedroom_state  = HIGH;
        kitchen_state  = HIGH;
        break;
    }
  }

 
  if (blinking_mode) {

    
    if (bathroom_state == LOW && bedroom_state == LOW && kitchen_state == LOW) {
      blinking_mode = false;
   
      return;
    }

   
    if (bathroom_state == HIGH) digitalWrite(BATHROOM_LIGHT, HIGH);
    if (bedroom_state  == HIGH) digitalWrite(BEDROOM_LIGHT, HIGH);
    if (kitchen_state  == HIGH) digitalWrite(KITCHEN_LIGHT, HIGH);
    delay(300);

   
    if (bathroom_state == HIGH) digitalWrite(BATHROOM_LIGHT, LOW);
    if (bedroom_state  == HIGH) digitalWrite(BEDROOM_LIGHT, LOW);
    if (kitchen_state  == HIGH) digitalWrite(KITCHEN_LIGHT, LOW);
    delay(300);

  } else {
    
    digitalWrite(BATHROOM_LIGHT, bathroom_state);
    digitalWrite(BEDROOM_LIGHT, bedroom_state);
    digitalWrite(KITCHEN_LIGHT, kitchen_state);
  }
}