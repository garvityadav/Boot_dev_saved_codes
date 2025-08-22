def decayed_followers(intl_followers, fraction_lost_daily, days):

    retention_rate = 1 - fraction_lost_daily
    remaining_rate = intl_followers * (retention_rate**days)
    return remaining_rate
