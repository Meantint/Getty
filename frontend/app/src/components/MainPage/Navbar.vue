<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-success bg-primary" id="navbar">
  <div class="container-fluid">
    <div style="color: white" class="text-left">
      <router-link :to="{ name: 'Home' }">
        <img src="@/assets/logo.png" style="width:70px">
      </router-link>
      <!-- 싸피은행 -->
      SSAFY BANK
    </div>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <span v-if="isLogin">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link :to="{ name: 'LoanList' }" class="text-light nav-link">금융서비스</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'Mypage' }" class="text-light nav-link">마이페이지</router-link>
          </li>
          <li class="nav-item">
            <router-link @click.native="logout" to="#" class="text-light nav-link" text-decoration: none>로그아웃</router-link>
          </li>
        </ul>
      </span>
      <span v-else>
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="http://localhost:8080/loanList" style="color: white">금융서비스</a>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'About' }" class="text-light nav-link">로그인</router-link>
          </li>
          <!-- <li class="nav-item">
            <a class="nav-link" href="https://www.shinhan.com/hpe/index.jsp#050000000000" style="color: white">고객센터</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://www.shinhan.com/hpe/index.jsp#300000000000" style="color: white">회사소개</a>
          </li> -->
        </ul>
      </span>
    </div>
  </div>
  <br>
</nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    msg: String
  },
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('Token')
      localStorage.removeItem('ID')
      this.$router.go()
    },
  },
  created: function () {
    const token = localStorage.getItem('Token')
    if (token != null) {
      this.isLogin = true
    }
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

/* #navbar {
  font-family: 'Noto Sans KR', sans-serif;
} */

</style>
