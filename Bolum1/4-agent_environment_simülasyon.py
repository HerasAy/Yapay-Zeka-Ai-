def run_simulation(steps=10):
    room = ServerRoom()
    bot = SmartAgent()

    simulation_data = []

    print(f"{'ADIM':<5} | {'SICAKLIK':<10} | {'NEM':<10} | {'AKSİYON':<15}")
    print("-" * 50)

    for i in range(steps):
        # 1. Algıla (Sense)
        current_status = room.get_status()

        # 2. Düşün ve Karar Ver (Think)
        action = bot.decide(current_status)

        # 3. Hareket Et (Act)
        room.apply_action(action)

        # Veri Toplama (Analiz için)
        simulation_data.append({
            "Step": i+1,
            "Temp": round(current_status['temp'], 2),
            "Humidity": round(current_status['humidity'], 2),
            "Action": action
        })

        print(f"{i+1:<5} | {current_status['temp']:.2f}°C    | {current_status['humidity']:.2f}%    | {action:<15}")

        # Ortamın doğal değişimi
        room.update_environment()
        time.sleep(0.5) # Gözlem kolaylığı için bekleme

    return pd.DataFrame(simulation_data)

# Simülasyonu Başlat
df_results = run_simulation(10)
