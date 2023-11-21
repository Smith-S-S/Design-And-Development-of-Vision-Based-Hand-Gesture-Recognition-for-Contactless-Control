void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(4, OUTPUT);  // for left forward
  pinMode(5, OUTPUT);  // for left backward
  pinMode(6, OUTPUT);  // for right forward
  pinMode(7, OUTPUT);  // for right backward
  pinMode(9, OUTPUT);  // for LED 1
  pinMode(10, OUTPUT);  // for LED 2
  pinMode(11, OUTPUT);  // for LED 3
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    String xx = Serial.readString();
    
    if (xx == "Front") {
      // Move forward
 
      digitalWrite(4, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(9, HIGH); 
      delay(500);
      digitalWrite(4, LOW);
      digitalWrite(6, LOW);
      digitalWrite(9, LOW);
    } 
    else if (xx == "Back") {
      // Move backward
      digitalWrite(5, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(10, HIGH);
      delay(500);
      digitalWrite(5, LOW);
      digitalWrite(7, LOW);
      digitalWrite(10, LOW);
    }
     
    else if (xx == "Right") {
      // Turn right 
      digitalWrite(4, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(11, HIGH);
      delay(200);
      digitalWrite(4, LOW);
      digitalWrite(7, LOW);
      digitalWrite(11, LOW);
    } 
    else if (xx == "Left") {
      // Turn left
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(12, HIGH);
      delay(200);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(12, LOW);
    }
    else if (xx == "Clock Wise") {
      // Turn Clock wise 
      digitalWrite(4, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(11, HIGH);
      delay(500);
      digitalWrite(4, LOW);
      digitalWrite(7, LOW);
      digitalWrite(11, LOW);
    } 
    else if (xx == "Anit-Clock Wise") {
      // Turn Anit-Clock Wise
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(12, HIGH);
      delay(500);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(12, LOW);
    } 
    
    else if (xx == "Front and Back") {
      // Move backward
      digitalWrite(4, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(9, HIGH);
      
      delay(500);
      digitalWrite(4, LOW);
      digitalWrite(6, LOW);
      digitalWrite(9, LOW);
      
      
      digitalWrite(5, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(10, HIGH);
      delay(500);
      digitalWrite(5, LOW);
      digitalWrite(7, LOW);
      digitalWrite(10, LOW);
    } 
    else if (xx == "Front and Anti-Clock Wise") {
      // Move backward
      digitalWrite(4, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(9, HIGH);
      delay(500);
      digitalWrite(4, LOW);
      digitalWrite(6, LOW);
      digitalWrite(9, LOW);

      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(11, HIGH);
      delay(200);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(11, LOW);
    }
    else if (xx == "Front and Clock Wise") {
      // Move backward
      digitalWrite(4, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(9, HIGH);
      delay(500);
      digitalWrite(4, LOW);
      digitalWrite(6, LOW);
      digitalWrite(9, LOW);

      digitalWrite(4, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(12, HIGH);
      delay(200);
      digitalWrite(4, LOW);
      digitalWrite(7, LOW);
      digitalWrite(12, LOW);

      
    }  
  }
}
