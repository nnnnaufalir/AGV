void preparePID(int err) {
  errorPID = err;
  toleranceErr = (errorPID * tolerance);
  scale = fabs(errorPID);
  if (scale > maxPIDPWM) {
    scale = maxPIDPWM;
  }
  dir = 1;
  if (err < 0) {
    dir = -1;
  }
}

void donePID(int varInt) {
  if (varInt < (varInt + toleranceErr) && varInt > (varInt - toleranceErr)) {
    configMotor(0, 0);
    delay(2000);
  }
  delay(50);
}

void translationPID(int dir, int scale, int id) {
  if (dir == -1) {
    translation(scale, id);
  }
  else if (dir == 1) {
    translation(-scale, id);
  }
}

void rotationPID(int dir, int scale, int id) {
  if (dir == -1) {
    rotation(scale, id);
  }
  else if (dir == 1) {
    rotation(-scale, id);
  }
}


void translationTPID(int a) {
  target = a;
  preparePID(PID1);
  translationPID(dir, scale, 1);
  donePID(varInt1);
  preparePID(PID2);
  translationPID(dir, scale, 2);
  if (a == 0) {
    rencana = true;
  }
  else {
    rencana = false;
  }
}

void rotationTPID(int a) {
  target = a;
  preparePID(PID1);
  rotationPID(dir, scale, 1);
  donePID(varInt1);
  preparePID(PID2);
  rotationPID(dir, scale, 2);
  donePID(varInt2);
}
