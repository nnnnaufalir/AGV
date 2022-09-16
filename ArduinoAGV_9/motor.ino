int setPWM(int args) {
  if (args >= maxPIDPWM) {
    args = maxPIDPWM;
    return fabs(args);
  }
  if (args <= minPIDPWM) {
    args = maxPIDPWM;
    return fabs(args);
  } else {
    return fabs(args);
  }
}

void writeSignal(int main, int a, int b, int c, bool xA, bool xB) {
  analogWrite(a, setPWM(main));
  digitalWrite(b, xA);
  digitalWrite(c, xB);
}

void setMotor(int main, int mA, int mB, int mP) {
  if (main > 0) {
    writeSignal(main, mP, mA, mB, HIGH, LOW);
  }
  if (main < 0) {
    writeSignal(main, mP, mA, mB, LOW, HIGH);
  }
  if (main == 0) {
    writeSignal(main, mP, mA, mB, LOW, LOW);
  }
}

void configMotor(int m1, int m2) {
  setMotor(m1, M1A, M1B, MP1);
  setMotor(m2, M2A, M2B, MP2);
}
