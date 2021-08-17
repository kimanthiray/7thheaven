#Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

##Softwares needed:
 - Anaconda.
 - A text editor.
 - Git bash.
 
##Installation link for software:
 - [Git for windows](https://git-scm.com/download/win)
 - [Anaconda](https://www.anaconda.com/products/individual)
 - [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

##Code explained in Detail:
###How the program works:
The code developed takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions will change! There are four questions that will change the answers:

 - Would you like to see data for Chicago, New York, or Washington?
 - Would you like to filter the data by month, day, or not at all?

(If month is selected)
 - Which month?(January, February, March, April, May, or June)
 
(If day is selected)
 - Which day of the week?(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

#Statistics Computed
Your code will provide the following output:

###1 Popular times of travel (i.e., occurs most often in the start time)

 - Most common month
 - Most common day of the week
 - Popular hour of the day
###2 Popular stations and trip

 - Most common start station
 - Most common end station
 - Most common trip combination of start station and end station

###3 Trip duration statistics

 - Total travel time
 - Average travel time
###4 User statistics

 - Counts of user types
 - Counts of gender
 - Earliest, most recent, most common year of birth

###5 Raw data
 - Print raw data in rows of 5

###Duration
Each output computed should have a duration taken by the terminal to compute the code.

