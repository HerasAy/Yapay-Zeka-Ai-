class KnowledgeBaseFOL:
    def __init__(self):
        self.facts = set()  # Gerçekler: Man(Socrates)
        self.rules = []     # Kurallar: Man(x) => Mortal(x)

    def tell_fact(self, predicate, entity):
        """Bilgi tabanına bir gerçek ekle (Örn: 'Man', 'Socrates')"""
        self.facts.add((predicate, entity))

    def tell_rule(self, condition_pred, result_pred):
        """Basit kural ekle: condition(x) => result(x)"""
        self.rules.append((condition_pred, result_pred))

    def ask(self, predicate, entity):
        """
        Sorgu: Bu entity bu predicate'i sağlıyor mu?
        Hem gerçeklere hem de kurallara bakar (Forward Chaining Basit Hali)
        """
        # 1. Doğrudan gerçeklerde var mı?
        if (predicate, entity) in self.facts:
            return True

        # 2. Kurallardan türetilebiliyor mu?
        # Kural: A(x) => B(x). Eğer A(entity) doğruysa, B(entity) de doğrudur.
        for cond, res in self.rules:
            if res == predicate: # Aradığımız sonuç bu kuraldan çıkıyor mu?
                if self.ask(cond, entity): # Kuralın şartı sağlanıyor mu? (Recursive)
                    return True

        return False

# --- Test Senaryosu ---
kb = KnowledgeBaseFOL()

# 1. Bilgi Ekleme (TELL)
kb.tell_fact("Man", "Socrates")  # Socrates bir İnsandır.
kb.tell_fact("Man", "Plato")     # Plato bir İnsandır.
kb.tell_rule("Man", "Mortal")    # Her İnsan Ölümlüdür. (Man(x) => Mortal(x))

# 2. Sorgulama (ASK)
print("Socrates ölümlü mü?", kb.ask("Mortal", "Socrates"))
print("Plato ölümlü mü?", kb.ask("Mortal", "Plato"))
print("Zeus ölümlü mü?", kb.ask("Mortal", "Zeus")) # Bilgi tabanında yok
