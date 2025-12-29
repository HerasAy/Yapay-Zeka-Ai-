# Değişkenler (Bölgeler)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Alanlar (Renkler)
colors = ['Kırmızı', 'Yeşil', 'Mavi']
domains = {var: colors for var in variables}

# Kısıtlar (Komşuluklar)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  [] # Tazmanya ada olduğu için komşusu yok
}

def is_valid(assignment, var, color):
    """
    Seçilen renk, o bölgenin komşularıyla çakışıyor mu?
    """
    for neighbor in neighbors[var]:
        # Eğer komşu zaten boyanmışsa ve aynı renkse -> GEÇERSİZ
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    """
    Recursive Backtracking Algoritması
    """
    # 1. Tüm değişkenler atandı mı? (Çözüm Bulundu)
    if len(assignment) == len(variables):
        return assignment

    # 2. Atama yapılmamış bir değişken seç (Sıradaki)
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    # 3. Bu değişken için renkleri dene
    for color in domains[var]:
        if is_valid(assignment, var, color):
            assignment[var] = color # Ata

            # Recursive çağrı: Bir sonraki adıma git
            result = backtrack(assignment)
            if result: return result

            del assignment[var] # Backtrack (Geri al)

    return None # Çözüm yok

# Çalıştır
solution = backtrack({})
print("--- Harita Boyama Çözümü ---")
for region, color in solution.items():
    print(f"{region}: {color}")
