#include <WiFi.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

// WiFi credentials
const char* ssid = "colesman";
const char* password = "12345678";

// LED Pin
const int ledPin = 2; // Built-in LED pin on ESP32

// Task Handles
TaskHandle_t TaskHandleBlink;
TaskHandle_t TaskHandleWiFiStatus;

// Define tasks
void TaskBlink(void *pvParameters);
void TaskWiFiStatus(void *pvParameters);

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Create tasks
  xTaskCreate(TaskBlink, "BlinkTask", 2048, NULL, 1, &TaskHandleBlink);
  xTaskCreate(TaskWiFiStatus, "WiFiStatusTask", 2048, NULL, 1, &TaskHandleWiFiStatus);
}

void loop() {
  // Empty. Tasks are handled in FreeRTOS.
}

void TaskBlink(void *pvParameters) {
  for (;;) {
    digitalWrite(ledPin, HIGH);
    vTaskDelay(500 / portTICK_PERIOD_MS);
    digitalWrite(ledPin, LOW);
    vTaskDelay(500 / portTICK_PERIOD_MS);
  }
}

void TaskWiFiStatus(void *pvParameters) {
  for (;;) {
    if (WiFi.status() == WL_CONNECTED) {
      Serial.print("WiFi IP: ");
      Serial.println(WiFi.localIP());
    } else {
      Serial.println("WiFi disconnected");
    }
    vTaskDelay(10000 / portTICK_PERIOD_MS); // Delay 10 seconds
  }
}
