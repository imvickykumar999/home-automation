//https://console.firebase.google.com/u/0/project/home-automation-336c0/database/home-automation-336c0-default-rtdb/data
//https://console.firebase.google.com/u/0/project/home-automation-336c0/settings/serviceaccounts/databasesecrets

#include <WiFi.h>
#include "FirebaseESP32.h"

int ledpin = 2;

#define WIFI_SSID "Vicky"
#define WIFI_PASSWORD "oyevicks"

#define FIREBASE_HOST "home-automation-336c0-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "Gb3UMfmGbxoFT68kFKatNy8UzcZ79FzX77GBCqUo"

FirebaseData firebaseData;

void setup() {
  Serial.begin(115200);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }

  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);

  //Set database read timeout to 1 minute (max 15 minutes)
  Firebase.setReadTimeout(firebaseData, 1000 * 60);

  pinMode(ledpin, OUTPUT);
}

void loop() {
    if (Firebase.getInt(firebaseData,"A/B/C/Switch")){
      int val2 = (firebaseData.intData());
      
      if(val2==1){
        digitalWrite(ledpin, HIGH);
        Serial.println("HIGH");
      }
      
      else{
        digitalWrite(ledpin, LOW);
        Serial.println("LOW");
      }
    }

    delay(200);
}