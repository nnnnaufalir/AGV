int PID1() {
  // time difference
  currT1 = micros();
  deltaT1 = ((float) (currT1 - prevT1)) / ( 1.0e6 );
  prevT1 = currT1;

  // error
  e1 = varInt1 - target;

  // derivative
  dedt1 = (e1 - eprev1) / (deltaT1);

  // integral
  eintegral1 = eintegral1 + e1 * deltaT1;

  // control signal
  u1 = kp * e1 + kd * dedt1 + ki * eintegral1;

  // store previous error
  eprev1 = e1;
  return e1;
}

int PID2() {
  // time difference
  currT2 = micros();
  deltaT2 = ((float) (currT2 - prevT2)) / ( 1.0e6 );
  prevT2 = currT2;

  // error
  e2 = varInt2 - target;

  // derivative
  dedt2 = (e2 - eprev2) / (deltaT2);

  // integral
  eintegral2 = eintegral2 + e2 * deltaT2;

  // control signal
  u2 = kp * e2 + kd * dedt2 + ki * eintegral2;

  // store previous error
  eprev2 = e2;
  return e2;
}


//void checkCalc(){
//    Serial.print(scale);Serial.print("; u=");
//    Serial.print(u);Serial.print("; e=");
//    Serial.print(e);Serial.print("; dedt=");
//    Serial.print(dedt);Serial.print("; i=");
//    Serial.print(eintegral);Serial.print("; s=");
//    Serial.print(varInt2*hasiljarak);Serial.println("cm");
//  }
