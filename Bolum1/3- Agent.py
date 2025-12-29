class SmartAgent:
    def __init__(self):
        self.actions_taken = []

    def decide(self, sensors):
        """
        Sensör verilerine göre karar verir.
        Algoritma: Kural Tabanlı (Rule-Based)
        """
        temp = sensors["temp"]
        humidity = sensors["humidity"]
        action = "BEKLE"

        # Kural 1: Sıcaklık Kontrolü
        if temp > (TARGET_TEMP + TEMP_TOLERANCE):
            action = "SOGUTMA_AC"
        elif temp < (TARGET_TEMP - TEMP_TOLERANCE):
            action = "ISITMA_AC"

        # Kural 2: Nem Kontrolü (Sıcaklık normalse neme bak)
        elif humidity > (TARGET_HUMIDITY + 10):
            action = "NEM_ALMA_AC"

        self.actions_taken.append(action)
        return action
