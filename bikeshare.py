import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    for city in CITY_DATA:
        city = input('choose city please: chicago, new york city, washington:  ').lower()
        if city not in CITY_DATA:
            print('Wrong!! - Please choose a specific city!!')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    for month in months:
        month = input('choose month please: all, january, february, march, april, may, june:  ').lower()
        if month not in months:
            print('Wrong!! - Please choose the exact months or "ALL"!!')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    for day in days:
        day = input('choose day please: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all:  ').lower()
        if day not in days:
            print('Wrong!! - please write the correct name of the day or write "ALL"')
        else:
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['Start Station'] = df['Start Time'].mode()[0]
    df['End Station'] = df['Start Time'].mode()[0]
    df['User Stats'] = df['Start Time'].value_counts(type)
    df['count of gender'] = df['Start Time'].value_counts()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular day of week:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular day of week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Hour:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular Start Hour:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    print('most frequent combination of start station and end station trip: ', frequent_combination)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total of travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean of travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Stats'].value_counts()
    print('counts user type:', user_type)

    if city != 'washington':
        # TO DO: Display counts of gender
        count_of_gender = df['Gender'].value_counts()
        print('count of gender: ', count_of_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        most_common_year = df['Birth Year'].mode()[0]
        print('common year birth: ', most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('most recent year: ', most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('earliest year: ', earliest_year)
    else:
        print('Sorry, there is no gender or birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def Display_data(df):
    while True:
        ask_user = input('would you like see the first 5 rows? yes or no:  ').lower()
        if ask_user == 'yes':
            rows = 0
            print('the rows :\n', df.iloc[rows: rows + 5])
            rows += 5
            break
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day,)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        Display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()