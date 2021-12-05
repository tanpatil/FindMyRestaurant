<template>
<div> 
  <nav class="d-flex justify-content-center">
		<router-link class="nav-item" to="/">Home</router-link>
		<router-link class="nav-item" to="/about">About</router-link>
    <router-link class="nav-item" to="/eat"><strong>Get Recommendations!</strong></router-link>
  </nav> 
</div>
</template>


    

<script>
export default {
  methods: {
    
  }
}
</script>

<style scoped>
nav {
	left: 0%;
	right: 0%;
	background-color: #fbfbfb;
	position: fixed;
	top: 0px;
	display: block;
	box-shadow: 2px 2px 5px #aaaaaa;
	z-index: 1;

}

.nav-item {
	color: #3C3C3C;
	float: right;
	display: block;
	text-align: center;
	padding: 20px;
	text-decoration: none;
	font-size: 17px;
	font-weight: 500;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.nav-item:hover {
	color: #3C3C3C;
	transition: 0.5s;
}


.nav-item:hover:after {
    transform: scaleX(1);
}

.nav-item::after {
    display:block;
    content: '';
    border-bottom: solid 3px #beebe9;  
    transform: scaleX(0);  
    transition: 350ms ease-in-out;
    transform-origin: 0% 50%;
}

</style>