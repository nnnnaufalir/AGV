void mainFUNC() {
  bool play = false;
  int nowDegree;
  delay(10);
  lcd.setCursor(0, 0); lcd.print("Lagi Jalan");
  delay(10);
  play = true;

  if (play) {
    parsingData(false);

    if (pos == 0) {
      Serial.println("A");
    }
    if (pos == 1) {
      Serial.println("B");
    }
    if (pos == 2) {
      Serial.println("C");
    }

    delay(10);
    nowDegree = Degree;
//    if (S1()) {
//      delay(10);
//      lcd.clear();
//      rumah();
//    }
    if (prevDegree == nowDegree) {
      rotationTPID(prevDegree - nowDegree);
      prevDegree = nowDegree;
    }

    else {
      if (pos == pil) {
        translationTPID(Speed);
        if (rencana) {
          Serial.println("Path Selesai");
          translationTPID(0);
          play = false;
        }
      }
      else {
        translationTPID(Speed);
        if (rencana) {
          Serial.println("Plan Selesai");
          translationTPID(Speed);
        }
      }
    }
  }
  else {
    lcd.setCursor(0, 0);
    lcd.print("SELESAI PERJALANAN");
    delay(2000);
    rumah();
  }
}
