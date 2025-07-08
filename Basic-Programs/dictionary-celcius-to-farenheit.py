
weathere_dic =eval(input("Enter the weather in Celsius:"))


weathere_farenheit={city: temp *9/5 +32 for (city, temp) in weathere_dic.items()}
print(weathere_farenheit)