days = 45
growth = 2.0  # money doubles

monthly = growth ** (30 / days) - 1
annual  = growth ** (365 / days) - 1

print(f"Implied return per month : {monthly*100:,.1f} %")
print(f"Implied return per year  : {annual*100:,.0f} %")
print(f"$1,000 after 1 year      : ${1000*growth**(365/days):,.0f}")

# Benchmark comparison
benchmarks = {
    "Long-run US large-cap equities (nominal, ~long-term avg)": 0.10,
    "High-yield savings / money-market (current-ish)": 0.04,
    "Top-tier hedge fund, exceptional year": 0.30,
    "This offer (annualised)": annual,
}
for k, v in benchmarks.items():
    print(f"{k:60s} {v*100:>12,.0f} % / yr")