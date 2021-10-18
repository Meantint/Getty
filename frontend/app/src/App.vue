<template>
  <div id="app">
    <section>
      <router-view/>
    </section>
    <!-- <footer id="footer" class="d-flex text-center text-lg-start bg-light text-muted py-4">
      <div class="text-left col-4">
        <h6></h6>
        <h3 style="line-height:20px">고객센터 1599-8000</h3>
        <h6>&copy;SSAFY BANK. All rights reserved</h6>
      </div>
      <div class="text-right col-5">
        <h4 class="text-primary"><a href="https://www.shinhan.com/hpe/index.jsp#300000000000" target="_blank">은행소개 </a> | <a href="https://www.shinhan.com/hpe/index.jsp#050000000000" target="_blank"> 고객센터</a></h4>
        <h6 class="align-self-bottom">평일 09:00 ~ 18:00 (은행휴무일 제외)</h6>
      </div>
    </footer> -->
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap');


#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
  position: relative;
  width: 100%;
  /* height: 100%; */
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#footer {
    min-width: 1190px;
    background-color: #efedf2;
}

footer {
    background-color: #efedf2;
    display: flex;
    justify-content: center;
    padding: 30px 0 30px 0;
    outline: none;
    text-transform: none;
    text-decoration: none;
}
/*
footer {
  width: 100%;
  height: 80px;
  bottom: 0px;
  position: absolute;
  border-top: 1px solid #c4c4c4;
  padding-top: 15px;
  color: #808080;
  font-size: 11px;
} */

section {
  padding-bottom: 80px;
}

.tab { white-space: pre; }

</style>
