<template>
    <div id="landing">
        <div id="container">
            <el-row :gutter="24">
                <el-col :span="1" align-items="left">
                </el-col>
                <el-col :span="23" z-index="4">
                </el-col>
            </el-row>
            <el-col :span="11">
                <div class="grid-content">
                    <span>
                        <img src="../assets/logo.png" class="img" alt="image">
                        <div class="title">
                            FindMyRestaurant
                        </div>
                    </span>
                </div>
            </el-col>
        </div>
        <div id="row mt-5 h-100">
            <div class="col">
                <p class="slogan">supporting local thru the pandemic</p>
            </div>
        </div>
        <router-link to="eat" class="arrow mt-5"></router-link>
    </div>
</template>

<script scoped>
export default {
  name: 'Landing',
  components: {
  },
}
</script>

<style scoped>
.img {
    margin-top: 18%;
}
.title {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-size: 100px;
  margin-top: 3%;
  color: #ffb6b9;
}
.el-col {
    border-radius: 4px;
    position: relative; /* Declared position allows for location changes */
    top: -5px; /* Moves the image 5px closer to the top of the page */
}

body {
  direction: ltr;
  margin: 0;
  padding: 0;
  /* make it look decent enough #C8E7F5*/
  position: relative;
  height: 100%; 
}

img {
    height: 300px;
    width: 300px;
}

#home {
  font-family: 'Kumbh Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  background-color:azure;
}
@media screen and (max-width: 399px) {
  body {
    overflow: visible;
    overflow-x: hidden;
  }
}
#item {
  margin: 0;
  padding: 0;
}

.button1{
  color: black;
  font-family: 'Kumbh Sans', sans-serif;
  font-size: 20px;
  text-align: left;
}


.button1:hover {
   background-color: azure;
   color: black;
}
.slogan {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-size: 30px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3C3C3C;
  margin-bottom: 1%;
}

.arrow {
	border: solid black;
	border-color: #ffb6b9;
	border-width: 5px 5px 0px 0;
	display: inline-block;
	padding: 10px;
	transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transition: 0.3s;
  animation: bounce 3s infinite;
  margin: 20px;
  
}

.arrow:hover {
	-webkit-animation-play-state: paused;
	opacity: 60%;
	transform: scale(1.25) rotate(45deg);
}


@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateX(15px) rotate(45deg);
  }
  40% {
    transform: translateX(-30px) rotate(45deg);
  }
  60% {
    transform: translateX(-15px) rotate(45deg);
  }
}

</style>