class MathBot:
    def solve(self, query):
        # Basit matematik işlemleri için ayrı bir 'Dar Zeka'
        if "+" in query:
            nums = [int(n) for n in query.split() if n.isdigit()]
            return sum(nums)
        return None

class GeneralBotSimulation:
    def __init__(self):
        self.chat_bot = NarrowAIBot() # Önceki bot
        self.math_bot = MathBot()     # Matematik botu

    def respond(self, query):
        # 1. Önce matematik botuna sor
        math_result = self.math_bot.solve(query)
        if math_result:
            return f"[AGI_SIM]: Bu bir matematik sorusu, cevap: {math_result}"

        # 2. Matematik değilse sohbet botuna sor
        return self.chat_bot.respond(query).replace("[BOT]", "[AGI_SIM]")

# Test
simulated_agi = GeneralBotSimulation()
print(simulated_agi.respond("2 + 5 kaç eder?")) # Artık bunu da biliyor!
