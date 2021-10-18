<template>
  <nav class="navbar navbar-expand-lg navbar-success bg-primary">
  <div class="container-fluid d-flex justify-content-center">
    <div style="color: white">
      <router-link :to="{ name: 'BankerLoan' }">
        <img src="@/assets/logo.png" style="width:70px">
      </router-link>
        SSAFY BANK
    </div>
  </div>
  <br>
</nav>
</template>

<script>
export default {
  name: 'BankerNavbar',
  props: {
    msg: String
  }
}
</script>

<style scoped>
/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>
