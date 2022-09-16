int dWhell, dRobot, pulse;

int rotate(int degree) {
  int result = ((degree / 180) * (dWhell / dRobot) * pulse);
  return result;
}

void translation(int motor, int id) {
  if (id == 1) {
    configMotor(motor, 0);
  }
  if (id == 2) {
    configMotor(0, motor);
  }
}

void rotation(int motor, int id) {
  if (id == 1) {
    configMotor(motor, 0);
  }
  if (id == 2) {
    configMotor(0, -motor);
  }
}
