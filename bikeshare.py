import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city_input ='NA'
    
    while city_input not in CITY_DATA:
        city_input = input("Please enter one of the following cities\nChicago , New York City, Washington:\n")
        city_input = city_input.lower()
        
        if city_input in CITY_DATA:
            #print(city_input)
            city = CITY_DATA[city_input]
        else:
            print("Warning! your city input name is not available \nor there is a spelling mistake\n")
    


    # TO DO: get user input for month (all, january, february, ... , june)
    month_input ='NA'  
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while month_input not in months:
        month_input = input("Please enter a month you want to filter\nMonths to enter are 'January','February','March','April','May','June'\nor 'all' for the whole month: ")
        month_input = month_input.lower()
        if month_input in months:
            month = month_input
        else:
            print("There is an error;  \n ")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input ='NA'
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    while day_input not in days:
        day_input = input("Please enter the day you want to filter\ntype the day name as the following\n 'Sunday' , 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'\n or 'all' for the whole week: ")
        day_input = day_input.lower()
        if day_input in days:
            day = day_input
        else:
            print("There is an error; \n")

    
    print('-'*40)
    

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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name ## dt.weekday_name ##dayofweek
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month: {}".format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week: {}".format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour: {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station: " + most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("The most commonly used end station: " + most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    z = df.loc[df['Start Station'] == most_common_start] 
    x = z['End Station'].mode()[0]
    if x == most_common_start:
        y = z.pop('End Station')
        y = y.replace(x, np.nan)
        s = y.mode()[0]
        print("The most frequent combination of start station: {} and end station: {}".format(most_common_start,s))
    else:
        print("The most frequent combination of start station: {} and end station: {}".format(most_common_start,x))
        
    
    #print("The most frequent combination of start station and end station trips: " + y['End Station'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time']  - df['Start Time']
    total_travel_time = df['Travel Time'].sum()
    print("Total travel time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print("The mean travel time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    x = df['User Type'].value_counts()
    print("Counts of user types: ")
    print(x)
    print(' '*40)
    # TO DO: Display counts of gender
    try: 
        y = df['Gender'].value_counts()
        print("Counts of gender: ")
        print(y)
        
    except:
        print("There is no gender information available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print("The earliest year of birth: {}".format(earliest))
        ##
        most_recent = int(df['Birth Year'].max())
        print("The most recent year of birth: {}".format(most_recent))
        ##
        most_common_year = int(df['Birth Year'].mode()[0])
        print("The most common year of birth: {}".format(most_common_year))
        
    except:
        print("There is no year of birth information available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        raw_data = 'n'
        while raw_data == 'n':
            raw_data = input("Do you want to see raw data? type 'y' or 'n' ").lower()
            if raw_data == 'y':
                city, month, day = get_filters()
                df = load_data(city, month, day)
                print(df.head())
                time_stats(df)
                print(df.head())
                station_stats(df)
                print(df.head())
                trip_duration_stats(df)
                print(df.head())
                user_stats(df)
                print(df.head())
                break
            elif raw_data == 'n':
                city, month, day = get_filters()
                df = load_data(city, month, day)
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
