<template>
<div class="mb-3 pb-3">
  <router-link :to="{ name: 'LoanList' }" style="text-decoration: none;">
    <div class="row justify-content-center align-items-center" style="height: 720px; text-align: left; pointer-events: none; background-color: #EBF5FB;">
        <div class="ml-5">
          <h1 class="col pt-5">365일 언제 어디서나</h1>
          <h2 class="col" >싸피 싹편한 언택트 대출 S</h2>
          <h3 class="pt-3 col" style="color: black;" >365일 언제 어디서나 내가 필요한 시점에 간편하게 신청!</h3>
          <b-button variant="outline-primary" class="col-6 mt-4 ml-3 btn btn-light p">가능한 대출 상품 보기</b-button>
        </div>
      <img src="@/assets/main.png" style="height:360px">
    </div>
  </router-link>

  <!-- test1 : color: 흰색   -->
  <div class="mb-3 pb-3" style="height: 720px; text-align: center;">
    <h1 class="pt-5" >복잡한 서류 제출을 내가 원하는 시간에 간편하게</h1>
    <h3 class="pb-3 pt-3" style="color: grey">주말이나 공휴일에도 신청할 수 있습니다.</h3>
    <iframe width="900px" height="560px" src="https://www.youtube.com/embed/pQN9rTUBIG8?autoplay=1&mute=1&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

</template>

<script>
export default {
    name: 'MainPageCenter',
}
</script>

<style>

</style>
