# question #3: Prerform access list, change list. add list and remove list methods

countryName = ["Afghanistan", "Tajikistan", "USA", "Uzbekistan"]
print(countryName[2])


countryName = ["Afghanistan", "Tajikistan", "USA", "Uzbekistan", "Haland", "Danmark"]
countryName[2:4] = ["Pakistan", "iran"]
print(countryName)


countryName = ["Afghanistan", "Tajikistan", "USA", "Uzbekistan"]
countryName.append("pakistan")
print(countryName)


countryName = ["Afghanistan", "Tajikistan", "USA", "Uzbekistan"]
countryName.remove("USA")
print(countryName)