//====================================================================
// ATIVIDADE FIAP - GLOBAL SOLUTION
//====================================================================
// Autor.....: Diego Nunes Veiga
// RM........: 560658
// Turma.....: Graduação - 1TIAOR
// Data......: 02/06/2025
//====================================================================

#include <DHT.h>
#include <math.h>

// Sensor DHT22
#define pinoDHT 23
#define modelo DHT22
DHT dht(pinoDHT, modelo);

// Sensor de radiação (simulado com potenciômetro)
#define pinoRadiacao 34

// Variáveis globais
float tempMax = -1000, tempMin = 1000;
float orvalhoMax = -1000, orvalhoMin = 1000;
float umidadeMax = -1, umidadeMin = 101;
float irradianciaWm2 = 0;
float energiaKJm2 = 0;
unsigned long tempoAnterior = 0;

//====================================================================
// STARTUP INICIAL
//====================================================================

void setup() {
  Serial.begin(9600);
  dht.begin();
}


//====================================================================
// PROGRAMA PRINCIPAL
//====================================================================


void loop() {
  for (int i = 0; i <= 21; i++) {

    // DHT22 - Temperatura e Umidade
    float hum = dht.readHumidity();
    float temp = dht.readTemperature();

    // Cálculo do ponto de orvalho
    float a = 17.27, b = 237.7;
    float alpha = ((a * temp) / (b + temp)) + log(hum / 100.0);
    float pontoOrvalho = (b * alpha) / (a - alpha);

    if (!isnan(temp)) {
      if (temp > tempMax) tempMax = temp;
      if (temp < tempMin) tempMin = temp;
    }

    if (!isnan(pontoOrvalho)) {
      if (pontoOrvalho > orvalhoMax) orvalhoMax = pontoOrvalho;
      if (pontoOrvalho < orvalhoMin) orvalhoMin = pontoOrvalho;
    }

    if (!isnan(hum)) {
      if (hum > umidadeMax) umidadeMax = hum;
      if (hum < umidadeMin) umidadeMin = hum;
    }

    // Sensor de radiação
    int valorADC = analogRead(pinoRadiacao);
    float tensao = valorADC * (3.3 / 4095.0);
    irradianciaWm2 = (tensao / 3.3) * 1500;

    unsigned long tempoAtual = millis();
    if (tempoAtual - tempoAnterior >= 1000) {
      energiaKJm2 += irradianciaWm2 / 1000.0;
      tempoAnterior = tempoAtual;
    }

    // Impressão final
    if (i == 21) {
      Serial.println("------ SENSOR DHT22 ------");
      Serial.print("Temperatura do Ar: "); Serial.println(temp);
      Serial.print("Temperatura Máxima do Ar: "); Serial.println(tempMax);
      Serial.print("Temperatura Mínima do Ar: "); Serial.println(tempMin);
      Serial.print("Ponto de Orvalho: "); Serial.println(pontoOrvalho);
      Serial.print("Temperatura Máxima de Orvalho: "); Serial.println(orvalhoMax);
      Serial.print("Temperatura Mínima de Orvalho: "); Serial.println(orvalhoMin);
      Serial.print("Umidade Relativa: "); Serial.println(hum);
      Serial.print("Umidade Máxima: "); Serial.println(umidadeMax);
      Serial.print("Umidade Mínima: "); Serial.println(umidadeMin);

      Serial.println("------ SENSOR DE RADIAÇÃO ------");
      Serial.print("Irradiância: "); Serial.print(irradianciaWm2); Serial.println(" W/m²");
      Serial.print("Energia acumulada: "); Serial.print(energiaKJm2); Serial.println(" kJ/m²");
    }

    delay(100);
  }
}
