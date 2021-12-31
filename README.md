Created by Tanay Patil for Kent Hack Enough 2021

Checkout our [devpost submission](https://devpost.com/software/findmyrestaurant)\
Take a look at our website-[FindMyRestaurant](https://findmyrestaurantwastaken.tech)

## Inspiration
Currently, because of COVID-19, it is becoming increasingly difficult for many restaurants to stay afloat.\
After the pandemic, local restaurants will still be recovering from the financial burdens of COVID-19.\
One of our friends’ parents run a small restaurant and have experienced the negative effect of COVID-19 on their business firsthand, leading us to have a personal connection to how local restaurant owners are being affected.

## What it does
FindMyRestaurant is an immediate response to the pandemic and a foreshadow to the aftermath of this pandemic. Our web app is a restaurant recommender system that filters through user reviews to give you the best dining experience while supporting small businesses in San Diego. We gather the user’s preferences and location information through a simple form, and our algorithm will output a series of relevant recommendations of what local restaurants to try!

## How we built it
We acquired large datasets containing reviews from Google Maps. Since the original datasets had a wide variety of information on businesses all over the United States, we pre-processed the data into a bucket of 2,000 reviews solely for San-Diego businesses.\
We used a _latent factor collaborative filtering_ strategy to narrow down results by the search term input with these relatively smaller datasets. Latent factor collaborative filtering, unlike content-based filtering, seeks to match the search term with the strings of user reviews rather than the restaurant properties directly.\
After that, we used a TF-IDF vectorization to isolate most of the relevant words in the text input, we grouped the vectors by the submitted user and business ID into two matrices that we can multiply together to estimate the rating given by our user. We return the top five recommendations based on this rating and use the Google Places API to get the more detailed information that we display.\
Because we use LFCF, our yielded recommendations are built directly on the text of previous user reviews. For example, if we input the term “date night,” our algorithm compares the string directly to the vector of the most important words for each review. This means that our recommendation engine is not only effective on simple, direct queries like “chinese food” or “tacos,” it can also handle much vaguer terms like “date night” with high accuracy. This is illustrated when we search “date night.” The top two results are Fratelli’s Ristorante and Mai’s Restaurant, which are higher-end locations that are perfect for a date.

![logo](https://user-images.githubusercontent.com/89934290/144749281-2fb1a53d-881a-45b7-b4bc-e3aa9e85c36a.png)

![image](https://user-images.githubusercontent.com/89934290/144749287-2c4913ab-9367-4ea0-b788-fe903f59a81f.png)


## Challenges we ran into
Working with that large 5GB JSON file dataset was something that none of us had experience with. The aggregate review dataset couldn’t be loaded directly by pandas or even displayed in VSCode. We had to use streams to facilitate I/O - reading the dataset one line at a time to get around this. Pre-processing our datasets was much slower than anticipated after this.\
Implementing the recommendation system was also a challenge. Once again, none of us had experience writing even simple ML recommenders, so writing the recommendation engine from scratch was difficult. We also had some trouble with the initial implementation of gradient descent to increase the effectiveness of our model. We knew conceptually that gradient descent was supposed to minimize the estimated and actual rating error, although we struggled with the algorithmic solution.

## Accomplishments that we’re proud of
We were able to create a recommender system and deploy the web app to Heroku with a simple yet effective UI for users in under 24 hours!\
Using a TF-IDF Vectorizer to identify the most important remaining words, processing text in reviews, and accepting ambiguous inputs for our recommender system!\
Learning a ton about data science, especially about latent factor collaborative filtering!

## What we learned
Working with enormous datasets and processing them for our specific use cases\
Use TF-IDF o build a recommender system.

## What’s next for FindMyRestaurant
Implement and use Gradient Descent to calculate and minimize error.\
Expand our data sets past San Diego, and make this accessible nationwide and maybe even internationally.\
We also intend to include local businesses and not just a limit to restaurants!
