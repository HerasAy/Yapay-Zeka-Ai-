from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
from sympy.abc import P, Q, R
from sympy.logic.inference import satisfiable

def generate_truth_table(expression):
    """
    Verilen mantıksal ifadenin doğruluk tablosunu basar.
    """
    print(f"İfade: {expression}")
    print(f"{'P':<5} | {'Q':<5} | {'R':<5} | {'SONUÇ'}")
    print("-" * 30)

    # P, Q, R için tüm True/False kombinasyonları (2^3 = 8 durum)
    for p_val in [True, False]:
        for q_val in [True, False]:
            for r_val in [True, False]:
                # İfadeyi bu değerlerle değerlendir (subs = substitute)
                result = expression.subs({P: p_val, Q: q_val, R: r_val})

                print(f"{str(p_val):<5} | {str(q_val):<5} | {str(r_val):<5} | {result}")

# ÖRNEK SENARYO:
# P: Hava Yağmurlu
# Q: Şemsiyem Var
# R: Islanırım

# Kural: (Hava Yağmurlu VE Şemsiyem Yok) => Islanırım
# Formül: (P AND (NOT Q)) => R
logic_sentence = Implies(And(P, Not(Q)), R)

generate_truth_table(logic_sentence)
