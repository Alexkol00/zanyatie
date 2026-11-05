ROUTES = [
    {"name": "Кратер", "energy": 35, "risk": 7},
    {"name": "Равнина", "energy": 50, "risk": 2},
    {"name": "Каньон", "energy": 45, "risk": 4},
]

def choose_route(routes, battery, max_risk, reserve=0):
    """Выбрать самый экономичный допустимый маршрут; при равенстве — первый."""
    if battery < 0 or max_risk < 0 or reserve < 0:
        raise ValueError("Параметры миссии не могут быть отрицательными")
    best_route = None
    for route in routes:
        enough_energy = route["energy"] + reserve <= battery
        safe_enough = route["risk"] <= max_risk
        if enough_energy and safe_enough:
            if best_route is None or route["energy"] < best_route["energy"]:
                best_route = route
    return best_route

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Миссия марсохода")
    parser.add_argument("--battery", type=int, default=60)
    parser.add_argument("--max-risk", type=int, default=4)
    parser.add_argument("--reserve", type=int, default=0)
    args = parser.parse_args()
    if min(args.battery, args.max_risk, args.reserve) < 0:
        parser.error("Параметры миссии не могут быть отрицательными")
    selected = choose_route(ROUTES, args.battery, args.max_risk, args.reserve)
    if selected is None:
        print("Безопасного маршрута нет. Остаёмся на месте.")
    else:
        print("Маршрут:", selected["name"])
        print("Остаток энергии:", args.battery - selected["energy"])

if __name__ == "__main__":
    main()
