hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Prices and Cuts:
total_price=0
for price in prices:
  total_price+=pricehttps://github.com/linhto1211/Learning-Python
average_price=total_price/len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

#Revenue
total_revenue=0
total_revenue +=1
for i in list(range(len(hairstyles))):
  total_revenue+=prices[i]*last_week[i]

print("Total Revenue: " + str(total_revenue))
average_daily_revenue=total_revenue/7

cut_under_30 = [hairstyles[i] for i in list(range(len(new_prices)-1)) if new_prices[i] <30]

print(cut_under_30)
