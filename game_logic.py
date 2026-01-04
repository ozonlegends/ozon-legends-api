def calc_xp_from_income(income):
    return income * 0.02

def xp_required_for_level(level):
    return 50 * (level ** 1.4)

def check_level_up(xp, level):
    while xp >= xp_required_for_level(level):
        xp -= xp_required_for_level(level)
        level += 1
    return level, xp

def calc_coins_from_income(income):
    return 5 + income * 0.01

def streak_bonus_multiplier(streak):
    return 1 + min(streak * 0.01, 0.30)

def process_shift(income, level, xp, streak):
    xp += calc_xp_from_income(income)
    level, xp = check_level_up(xp, level)
    coins = calc_coins_from_income(income) * streak_bonus_multiplier(streak)
    rating = income / 100
    return {
        "level": level,
        "xp": xp,
        "coins": coins,
        "rating": rating
    }
