# esp8266_mqtt
Dies ist eine Weiterentwicklung von  **[wetterstation-ESP8266](https://github.com/dk2jk/wetterstation-ESP8266).**
Als Protokoll wird MQTT verwendet. Als Server wird ein RaspberryPi verwendet , auf dem läuft ein Mosquitto- Server
und Node-Red läuft.
Es wird im Genesatz zum o.a. [Projekt](https://github.com/dk2jk/wetterstation-ESP8266)  kein externer Server wie z.b. Thingspeak benötigt.

Das ESP8266-Modul läuft im Stromspar-Modus. Der Stromspar- Modus wird dadurch erreicht, dass der Prozessor für längere Zeit in Tiefschlaf versetzt wird ( “deepsleep“ ). Unsere Wetterstation-Platine hat neben dem Prozessor nur noch einen Low-Current-Spannungsregler für 3.3 V, so dass der Schlafstrom bei ca. 22 uA liegt ( 20 uA die ESP8266 und 2 uA der  MCP1703). Bei Modulen mit USB-Serial-Wandlern – etwa bei Modul „Wemos D1 Mini“ läge der Ruhestrom wesentlich höher.

Das Aufwecken der CPU wird durch einen Timer ausgelöst, der als Einziges im Schlafmodus läuft. Wenn der Timer abgelaufen ist, so wird über GPIO16 ein Reset der CPU ausgelöst. Für den Deepsleep- Reset muss GPIO16 mit RST verbunden werden.

**Wenn die Messung nur einmal in der Stunde erfolgt, so sollte bei Versorgung mit 4.5 Volt , d.h. 3 x AA-Zellen die Laufzeit der Wetterstation bei ca. einem Jahr liegen.**

