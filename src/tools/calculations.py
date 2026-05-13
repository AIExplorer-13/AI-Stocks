def calculate_pe(price, eps):
    return round(price / eps, 2)


def calculate_position_size(capital, risk_percent, entry, stop):

    risk_amount = capital * (risk_percent / 100)

    risk_per_share = entry - stop

    return risk_amount / risk_per_share