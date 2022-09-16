void setHome() {
  if (S2()) {
    delay(10);
    setPerjalanan();
  }
  if (S3()) {
    delay(10);
    setInfo();
  }
}

void setPosisi () {
  if (S4()) {
    delay(100);
    pilih = true;
    pos++;
  }
  if (S5()) {
    delay(100);
    pilih = true;
    pos--;
  }
  if (S6()) {
    delay(10);
    pilih = false;
    setPerjalanan();
  }
  if (S7()) {
    delay(250);
    konfirmasi();
  }
  if (S1()) {
    delay(10);
    pilih = false;
  }
  if (pos > 2) {
    pos = 0;
  }
  else if (pos < 0) {
    pos = 2;
  }
}

void datang () {
  lcd.setCursor(0, 0); lcd.print("====================");
  lcd.setCursor(0, 3); lcd.print("====================");
  lcd.setCursor(2, 1); lcd.print("S E L A M A T");
  lcd.setCursor(7, 2); lcd.print("D A T A N G");
}

void tekan () {
  lcd.setCursor(0, 0); lcd.print("====================");
  lcd.setCursor(0, 3); lcd.print("====================");
  lcd.setCursor(2, 1); lcd.print("--TEKAN & TAHAN--");
  lcd.setCursor(7, 2); lcd.print("\"START\"");
}

void rumah () {
  while (1) {
    digitalWrite(ledJalan,LOW);
    lcd.clear();
    if (S1()) {
      delay(10);
      setPerjalanan();
    }
    datang(); delay(1000);
    if (S1()) {
      delay(10);
      setPerjalanan();
    }
    delay(1000);
    datang(); delay(1000);
    if (S1()) {
      delay(10);
      setPerjalanan();
    }
    delay(1000);
    lcd.clear();
    tekan(); delay(1000);
    if (S1()) {
      delay(10);
      setPerjalanan();
    }
    delay(1000);
    tekan(); delay(1000);
    if (S1()) {
      delay(10);
      setPerjalanan();
    }
    delay(1000);
  }
}

void setPerjalanan() {
  lcd.clear();
  while (1) {
    lcd.setCursor(0, 0); lcd.write(TANDA); lcd.print("Atur Perjalanan ");
    lcd.setCursor(1, 2); lcd.print("INFO ");
    setHome();
    if (S7()) {
      delay(200);
      aturPerjalanan();
    }
  }
}

void setInfo () {
  lcd.clear();
  while (1) {
    lcd.setCursor(1, 0); lcd.print("Atur Perjalanan ");
    lcd.setCursor(0, 2); lcd.write(TANDA); lcd.print("INFO ");
    setHome();
    if (S7()) {
      delay(200);
      info();
    }
  }
}

void aturPerjalanan () {
  lcd.clear();
  while (1) {
    parsingData(false);
    lcd.setCursor(0, 0); lcd.print("Posisi : "); lcd.print(tujuan[pil]);//posisi cam
    lcd.setCursor(0, 1); lcd.print("Tujuan : ");
    if (pilih == true) {
      lcd.print(tujuan[pos]);
    }
    else {
      lcd.print("          ");
    }
    lcd.setCursor(7, 3); lcd.write(HOME);
    lcd.setCursor(13, 3); lcd.write(RESET);
    lcd.setCursor(10, 3); lcd.write(OKE);
    if (pilih == false) {
      if (S7()) {
        delay(10);
        lcd.clear();
        lcd.setCursor(0, 0); lcd.print("ANDA BELUM MEMASUKAN TUJUAN!");
        delay(3000);
        aturPerjalanan();
      }
    }
    setPosisi();
  }
}

void konfirmasi() {
  lcd.clear();
  while (1) {
    parsingData(false);
    if (pil == pos) {
      lcd.setCursor(0, 1); lcd.print(" ANDA SUDAH BERADA ");
      lcd.setCursor(4, 2); lcd.print("DI "); lcd.print(posisi[pos]);
      delay(50);
      if (pos == 0) {
        Serial.println("A");
      }
      if (pos == 1) {
        Serial.println("B");
      }
      if (pos == 2) {
        Serial.println("C");
      }
      delay(3000); aturPerjalanan();
    }
    else {
      lcd.setCursor(0, 0); lcd.print("Perjalanan dari "); lcd.write(PANAH2); lcd.write(PANAH2); lcd.write(PANAH2);
      lcd.setCursor(0, 1); lcd.print(posisi[pil]); lcd.print(" menuju "); lcd.write(PANAH1); lcd.write(PANAH1); lcd.write(PANAH1);
      lcd.setCursor(0, 2); lcd.print(posisi[pos]); lcd.print(" ? ");
      lcd.setCursor(8, 3); lcd.write(RESET);
      lcd.setCursor(12, 3); lcd.write(OKE);
      if (S6()) {
        delay(250);
        aturPerjalanan();
      }

      //INTI DARI INTI
      if (S7()) {
        lcd.clear();
        while (1) {
          parsingData(false);
          delay(10);
          mainFUNC();
          //jalan();
        }
      }
    }
  }
}

void info () {
  lcd.clear();
  while (1) {
    if (S6()) {
      delay(10);
      lcd.clear();
      setInfo();
    }
    else {
      parsingData(true);
    }
  }
}
