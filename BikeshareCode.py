import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_filters ():

    """
    Asks the users to specify a city, month and day for analysis.

    Returns:
        str(name of the city to filter by)
        str(name of the month to filter by, or "all" to apply no month filter)
        str(name of the day to filter by, or "all" to apply no day filter)

    """

    print("Hi! Let\'s go right ahead and explore some Bikeshare data!")

    #get user input for city to filter by
    city = input('Would you like to see data for New York, Chicago or Washington?(New York, Chicago, Washington) ').lower()
    while city not in (CITY_DATA.keys()):
        print("Invalid city name!!?")
        city = input('Would you like to see data for New York, Chicago or Washington?(New York, Chicago, Washington) ').lower()

    #get user input to filter by month, day, both or none
    filter = input('Would you like to filter by month, day, both or none?(month, day, both, none) ').lower()
    while filter not in (['month', 'day', 'both', 'none']):
        print("Invalid input!!?")
        filter = input('Would you like to filter by month, day, both or none?(month, day, both, none) ').lower()

    #get user input for months or all for filtering
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both':
        month = input('Which month - January, February, March, April, May or June?  ').lower()
        while month not in months:
            print("Invalid input!!?")
            month = input('Which month - January, February, March, April, May or June?  ').lower()
    else:
        month = 'all'

    #get user input for day of the week to filter by
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if filter == 'day' or filter == 'both':
        day = input('Which day - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ').lower()
        while day not in days:
            print("Invalid input!!?")
            day = input('Which day - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? ').lower()
    else:
        day = 'all'

    print("\n")
    print('><' * 50)

    return city, month, day


def load_data(city, month, day):

    """
    Will load data for the specified city and filter by month and day.

    Args:
       (str)city: name of city
       (str)month: name of month or 'all' fo no filter
       (str)day: name of day or 'all' for no filter
    Returns:
       df - Pandas DataFrame containing city data filtered by month and day

    """
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #create new columns from month and day of week from Start Time to extract month
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day
    if day != 'all':

        #filter by day to create new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays stats on the most frequent times of travel"""

    print("\nCalculating the most frequent times of travel...\n")
    start = time.time()

    #display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}'.title())

    #display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f"The most common day of week is: {day}")

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {popular_hour}")

    print(f"\nThis took %s seconds." % (time.time() - start))
    print("_"*50)



def station_stats(df):
    """Displays stats on the most popular stations and trip"""

    print("\nCalculating the most popular stations and trip...\n")
    start = time.time()

    #display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"The most popular start station is: {popular_start_station}")

    #display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"The most popular end station is: {popular_end_station}")

    #display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    print(f"The most popular trip is from: {popular_trip.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start))
    print("_"*50)

def trip_duration_stats(df):
    from datetime import timedelta as td

    """Displays stats on the total and average trip duration"""

    print("\nCalculating trip duration...\n")
    start = time.time()

    #display total time of travel
    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60
    print(f"Total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds")

    #display mean travel time
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = average_travel_duration.days
    hours = average_travel_duration.seconds // (60 * 60)
    minutes = average_travel_duration.seconds % (60 * 60) // 60
    seconds = average_travel_duration.seconds % (60 * 60) % 60
    print(f"Average travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds.")

    print("\nThis took %s seconds." % (time.time() - start))
    print("_"*50)

def user_stats(df):
    """Displays stats on bikeshare users."""

    print("\nCalculating user stats...\n")
    start = time.time()

    #Display counts of user types
    print(df['User Type'].value_counts())
    print("\n\n")

    #Display counts on gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print("\n\n")

    #Display earliest, most recent and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year']
        print(f"Earliest birth year is: {year.min():.0f} \nMost recent birth year is: {year.max():.0f} \nMost common birth year is: {year.mode()[0]:.0f}")


    print("\nThis took %s seconds." % (time.time() - start))
    print("_"*50)

def display_raw_data(df):
    """Ask if the user wants to display the raw data and print 5 rows at a time"""

    raw = input('\nWould you like to display raw data 5 rows at a time? \n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count + 5])
            count += 5
            ask = input('Next 5 raws? ')
            if ask.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart?(yes, no) \n')
        if restart.lower() != 'yes':
            print("HAVE A GOOD DAY. ADIOS!...")
            break



if __name__ == "__main__":
    main()

