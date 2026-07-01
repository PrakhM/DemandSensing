import pandas as pd
from datetime import date
from weather import get_weather_category

def create_product(df):
    rows = []
    date_now = date.today().isoformat()
    sku_id = "SKU0001"
    category = "Ethnic Wear"
    
    price = int(input("Enter price: "))
    discount_percentage = int(input("Enter discount%: "))
    ratings  = df.groupby('city')['purchase_intent'].mean().reset_index()
    ratings = ratings.set_index("city")
    channels = (df.groupby('city')['preferred_channel']
                   .value_counts()
                   .reset_index(name='count')
                   .drop_duplicates('city'))
    channels = channels.set_index("city")
    cities = df['city'].unique().tolist()
    light = bool(int(input("Made of light cloth? (0,1): ")))
    vibrant = bool(int(input("Is colourful? (0,1): ")))

    print(cities, ratings, channels)

    for city in cities:
        rating = ratings.loc[city, "purchase_intent"] * 2
        channel = channels.loc[city, "preferred_channel"]
        weather = get_weather_category(city, pd.to_datetime(date_now))
        print("Weather for", city, "is", weather)
        rows.append(
            {
                "date": date_now,
                "price": price,
                "discount_percentage": discount_percentage,
                "rating": rating,
                "city": city,
                "channel": channel,
                "weather": weather,
                "light": light,
                "vibrant": vibrant
            }
        )
    
    result = pd.DataFrame(rows)
    result["date"] = pd.to_datetime(result["date"])

    result["month"] = result["date"].dt.month
    result["day_of_week"] = result["date"].dt.dayofweek
    result["year"] = result["date"].dt.year
    result = result.drop(columns = ["date"])
    result = pd.get_dummies(result, drop_first=True)

    print(result.head())

    return cities, result

