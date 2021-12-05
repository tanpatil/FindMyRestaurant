<template>
    <div id="AboutUs" class="container">
        <div class="row">
            <div class="col">
                <h1 class="about-title">our algorithm</h1>
                <h2 class="subtitle my-5">Latent Factor Collaborative Filtering</h2>
                <h4 class="intro my-5"> We chose to build a latent factor collaborative filtering (LFCF) 
                    recommendation system trained on user, business, and review datasets from Google Maps
                    (Google Local Reviews) to accurately find the most relevant restaurants to a user's
                    request. LFCF utilizes the behavior of other users to recommend items or services, which
                    in this case was restaurants. </h4>
                <h2 class="subtitle">Methodology</h2>
                <h4 class="intro my-5">From our datasets, we obtained 2000 reviews that included a rating, 
                    submitted user ID, business ID, and textual content. Next, we processed the text content
                    of the review (eliminated punctuation and extraneous characters) and used a TF-IDF Vectorizer 
                    to identify the most important remaining words. </h4>
                    <img src="https://miro.medium.com/max/2400/1*il58xdOYQcy4pHvtiJJpsQ.png" class="img-fluid" />
                <h4 class="intro my-5"> We then inserted these vectors with their
                    corresponding user and business IDs into two matrices and multiplied them together to
                    approximate the most likely rating that the user would give to the restaurant. Finally, 
                    we used gradient descent to calculate and minimize the error in our predictions. </h4> 
                    <img src="~@/assets/error.png" alt="andy" class="img-fluid" />
                <h4 class="intro my-5"> We take the top five recommendations, given by their name, estimated rating, 
                    Google Places ID, and address. Then, we can simply plug the address into the Google Places API to 
                    get detailed information for each location, such as its address and Google Maps listing! </h4>
            </div>
        </div>
        <div class="row mb-5">
            <div class="col">
                <h1 class="about-title">about us</h1>    
                <h4 class='intro my-5'> We are Tanay, Abijit, Gaurab 3 freshman at University of California, San Diego  
                    and Purdue University passionate about food and supporting small businesses, especially through the pandemic. 
                    Our project is focused on bringing visibility to such small businesses and supporting 
                    them as much as possible through these unprecedented times. Not only are local restaurants
                    suffering now, they still will be reeling from the financial burdens of COVID-19 long
                    after the pandemic has ended. We hope that our project can help alleviate financial
                    burdens for small businesses and allow more to survive through the year. </h4>
                <div class="row justify-content-center">
                    <div class="col-md-3 col-sm-6">
                        <img src="~@/assets/tanay.png" alt="tanay" class="propic img-fluid rounded-circle">
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <img src="~@/assets/abijit.png" alt="abijit" class="propic img-fluid rounded-circle">
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <img src="~@/assets/gaurab.png" alt="gaurab" class="propic img-fluid rounded-circle">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script scoped>
export default {
}
</script>

<style scoped>
.propic {
  height: 12rem;
  width: 12rem;
}

body {
  direction: ltr;
  margin: 40px;
  background-color:#ffffff;
  /* make it look decent enough #C8E7F5*/
  color: #000000;
  overflow-x: hidden;
  position: relative;
  height: 100%; 
}

.about-title {
  font-family: 'Kumbh Sans', sans-serif;
  font-size: 80px;
  color: #ffb6b9;
  margin-top: 7%;
  margin-bottom: -10px;
}

.subtitle {
  font-family: 'Kumbh Sans', sans-serif;
  color: #ffb6aF;
}

.intro {
  font-size: 24px;
  margin-left: 20px;
  margin-right: 20px; 

}
</style>