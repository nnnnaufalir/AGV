
void interrupt1() {
  (digitalRead(interruptPin1) == digitalRead(channelPin1)) ? varInt1++ : varInt1--;
}

void interrupt2() {
  (digitalRead(interruptPin2) == digitalRead(channelPin2)) ? varInt2-- : varInt2++;
}


void cekpulsamotor() {
  Serial2.print("Pulsa 1= "); Serial2.print(varInt1);
  Serial2.print(" Pulsa 2= "); Serial2.print(varInt2);

  delay(100);
}
void cekotomatis(int u, int varInt) {
  Serial2.print("  U: "); Serial2.print(u);
  Serial2.print(" Pulsa= "); Serial2.print(varInt);
  delay(100);
}
