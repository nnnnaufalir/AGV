void jalan () {

  while (1) {
    parsingData(false);
    if (pos == 0 && pil == 0) {
      if (S6()) {
        rumah();
      }
      else {
        berhenti();
      }
    }

    if (pos == 1 && pil == 1) {
      if (S6()) {
        rumah();
      }
      else {
        berhenti();
        digitalWrite(ledJalan,HIGH);
        delay(500);
        digitalWrite(ledJalan,LOW);
        delay(500);
      }
    }

    if (pos == 2 && pil == 2) {
      if (S6()) {
        rumah();
      }
      else {
        berhenti();
         digitalWrite(ledJalan,HIGH);
        delay(500);
        digitalWrite(ledJalan,LOW);
        delay(500);
      }
    }


    else {
      if (S6()) {
        rumah();
         digitalWrite(ledJalan,HIGH);
        delay(500);
        digitalWrite(ledJalan,LOW);
        delay(500);
      }
      else {
        maju(200);
        digitalWrite(ledJalan,HIGH);
      }
    }
    // maju(200);
  }
}

void berhenti () {
  analogWrite(MP1, 0);
  digitalWrite(M1A, LOW);
  digitalWrite(M1B, LOW);

  analogWrite(MP2, 0);
  digitalWrite(M2A, LOW);
  digitalWrite(M2B, LOW);
}

void maju (int pwm) {
  analogWrite(MP1, pwm);
  digitalWrite(M1A, HIGH);
  digitalWrite(M1B, LOW);

  analogWrite(MP2, pwm + 20);
  digitalWrite(M2A, HIGH);
  digitalWrite(M2B, LOW);
}

void mundur (int pwm) {
  analogWrite(MP1, pwm);
  digitalWrite(M1A, LOW);
  digitalWrite(M1B, HIGH);

  analogWrite(MP2, pwm);
  digitalWrite(M2A, LOW);
  digitalWrite(M2B, HIGH);
}

void kiri (int pwm) {
  analogWrite(MP1, pwm);
  digitalWrite(M1A, HIGH);
  digitalWrite(M1B, LOW);

  analogWrite(MP2, pwm);
  digitalWrite(M2A, LOW);
  digitalWrite(M2B, HIGH);
}

void kanan (int pwm) {
  analogWrite(MP1, pwm);
  digitalWrite(M1A, LOW);
  digitalWrite(M1B, HIGH);

  analogWrite(MP2, pwm);
  digitalWrite(M2A, HIGH);
  digitalWrite(M2B, LOW);
}
