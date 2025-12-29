class ExpertSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition_func, action_func):
        """
        Kural Ekleme:
        condition_func: True dönerse kural çalışır.
        action_func: Kural çalıştığında yapılacak işlem (Teşhis).
        """
        self.rules.append((condition_func, action_func))

    def diagnose(self, facts):
        """
        Gerçekleri (Facts) alır ve uygun kuralı bulur.
        """
        suggestions = []
        for condition, action in self.rules:
            if condition(facts):
                suggestions.append(action())

        if not suggestions:
            return ["Üzgünüm, bu durum için tanımlı bir çözümüm yok. Bir servise gidin."]
        return suggestions

# --- Bilgi Tabanı Oluşturma ---
engine_bot = ExpertSystem()

# Kural 1: Akü Sorunu
def check_battery(facts):
    return facts.get('marş_basıyor_mu') == False and facts.get('ışıklar_yanıyor_mu') == False
def result_battery(): return "Akü bitmiş olabilir. Aküyü şarj edin veya değiştirin."

# Kural 2: Yakıt Sorunu
def check_fuel(facts):
    return facts.get('marş_basıyor_mu') == True and facts.get('motor_çalışıyor_mu') == False
def result_fuel(): return "Yakıt deposunu kontrol edin veya yakıt pompası arızalı olabilir."

# Kural 3: Motor Isınması
def check_overheat(facts):
    return facts.get('motor_çalışıyor_mu') == True and facts.get('duman_var_mı') == True
def result_overheat(): return "Motor hararet yapmış! Hemen durun ve soğumasını bekleyin."

# Kuralları Sisteme Yükle
engine_bot.add_rule(check_battery, result_battery)
engine_bot.add_rule(check_fuel, result_fuel)
engine_bot.add_rule(check_overheat, result_overheat)

# --- Simülasyon ---
print("--- SENARYO 1 ---")
user_input_1 = {'marş_basıyor_mu': False, 'ışıklar_yanıyor_mu': False}
print(f"Durum: {user_input_1}")
print(f"Uzman Tavsiyesi: {engine_bot.diagnose(user_input_1)}")

print("\n--- SENARYO 2 ---")
user_input_2 = {'marş_basıyor_mu': True, 'motor_çalışıyor_mu': False}
print(f"Durum: {user_input_2}")
print(f"Uzman Tavsiyesi: {engine_bot.diagnose(user_input_2)}")
