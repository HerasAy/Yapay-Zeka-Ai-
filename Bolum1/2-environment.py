class ServerRoom:
    def __init__(self):
        # Başlangıç durumu (Rastgele)
        self.temperature = random.uniform(18, 30)
        self.humidity = random.uniform(30, 60)
        self.status_log = []

    def update_environment(self):
        """Doğal değişimleri simüle eder (Isınma eğilimi vb.)"""
        self.temperature += random.uniform(-0.5, 0.8) # Hafif ısınma eğilimi
        self.humidity += random.uniform(-1, 1)

    def get_status(self):
        """Sensör verisi döndürür"""
        return {"temp": self.temperature, "humidity": self.humidity}

    def apply_action(self, action):
        """Ajanın aksiyonuna göre ortamı değiştirir"""
        if action == "SOGUTMA_AC":
            self.temperature -= 2.0
        elif action == "ISITMA_AC":
            self.temperature += 2.0
        elif action == "NEM_ALMA_AC":
            self.humidity -= 5.0
        # "BEKLE" durumunda ortam değişmez (sadece doğal değişim)
