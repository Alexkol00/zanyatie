def check_mission(choose_route, final=False):
    routes = [
        {"name": "Кратер", "energy": 35, "risk": 7},
        {"name": "Равнина", "energy": 50, "risk": 2},
        {"name": "Каньон", "energy": 45, "risk": 4},
    ]
    cases = [(60, 4, "Каньон"), (60, 2, "Равнина"),
             (40, 4, None), (45, 4, "Каньон"), (35, 7, "Кратер")]
    count = 0
    for battery, risk, expected in cases:
        result = choose_route(routes, battery, risk)
        name = None if result is None else result["name"]
        if name != expected:
            raise AssertionError(f"Заряд={battery}, риск={risk}: ожидалось {expected}, получено {name}")
        count += 1
    if choose_route([], 60, 4) is not None:
        raise AssertionError("Для пустого списка ожидается None")
    count += 1
    tied = [{"name": "Первый", "energy": 20, "risk": 1},
            {"name": "Второй", "energy": 20, "risk": 1}]
    if choose_route(tied, 20, 1)["name"] != "Первый":
        raise AssertionError("При равной энергии оставьте первый маршрут")
    count += 1
    for params in [(-1, 4, 0), (60, -1, 0), (60, 4, -1)]:
        try:
            choose_route(routes, *params)
        except ValueError:
            count += 1
        else:
            raise AssertionError("Отрицательные параметры должны вызывать ValueError")
    if final:
        for battery, reserve, expected in [(55, 10, "Каньон"), (54, 10, None), (60, 61, None)]:
            result = choose_route(routes, battery, 4, reserve)
            name = None if result is None else result["name"]
            if name != expected:
                raise AssertionError(f"Заряд={battery}, резерв={reserve}: ожидалось {expected}, получено {name}")
            count += 1
    print(f"Проверки пройдены: {count}")

if __name__ == "__main__":
    import argparse
    import runpy
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", default="mission.py")
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()
    module = runpy.run_path(args.file)
    check_mission(module["choose_route"], final=args.final)
