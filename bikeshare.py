import time
import pandas as pd
import numpy as np

CD= { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Menu options and inputs 
def filters():

    print('Hello! Welcome to US bikeshare dataset!')
    while True :
        city=input('Please pick a city ?')
        cities= ['new york city' , 'chicago', 'washington']
        city=city.lower()
        if city in cities :
            break
        else:
           print ('wrong input')
    while True :
        month= input('Please pick a month and use its abbrevition. Only the first six months available for analysis JAN,FEB,MAR,APR,MAY,JUN.\n')
        months=['JAN','FEB','MAR','APR','MAY','JUN','all']
        if month in months:
            break
        else :
            print ('wrong input')
    while True :
        day= input('Please pick a day.\n')
        days= ['monday', 'tuesday','wednesday','thursday','friday','saturday','sunday','all']
        day=day.lower()
        if day in days:
            break
        else :
            print('wrong input')
    print('-'*40)
    return city, month, day

# Used Template From Practice Problem 3

def load_data(city, month, day):
    df=pd.read_csv(CD[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month']= df['Start Time'].dt.month

    df ['day_of_week'] = df['Start Time'].dt.weekday_name

    if month!= 'all' :
        months=['JAN','FEB','MAR','APR','MAY','JUN']
        month=months.index(month) + 1

        df= df[df['month']== month]

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):


    start_time = time.time()

    frequent_m=df ['month'].mode()[0]
    print('The most frequent month is:', frequent_m )



    frequent_w= df ['day_of_week'].mode()[0]
    print('The most frequent day of the week is :', frequent_w )



    df['hour'] = df ['Start Time'].dt.hour
    frequent_hour= df['hour'].mode()[0]
    print ('The most frequent hour is :',frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    start_time = time.time()

    popular_ss =df ['Start Station'].mode()[0]
    print('The most popular start station is :', popular_ss )

    popular_es= df ['End Station'].mode()[0]
    print('The most popular end station is :', popular_es )

    df['combo']= df['Start Station'] + df['End Station']
    popular_combo= df['combo'].mode()[0]
    print ('The most popluar combo of start and end stations :',popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()

    mean=df['Trip Duration'].mean()
    print('mean travel time is :', mean )


    total_travel=df['Trip Duration'].sum()
    print('sum of travel time is:', total_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_rows (df):
    start_time = time.time()

    y=0
    while True :
        user_inputs=input('If you wish to proceed with more data, please answer yes or type anything else to exit or restart program.\n')
        y += 5
        if user_inputs.lower()== 'yes':
           print(df[y:y+5])
        else:
           break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_rows (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break





if __name__ == "__main__":
	main()
