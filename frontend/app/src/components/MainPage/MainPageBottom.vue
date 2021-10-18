<template>
  <div class="mt-5 justify-content-center align-items-center" style="text-align: center; width: 100%">
    <!-- test1 : color: #559CDE  -->
    <div class="row justify-content-center align-items-center" style="height: 720px; text-align: left; pointer-events: none; background-color: #019bbc;">
      <iframe src="https://giphy.com/embed/1KllEBZdsLBwt3sDMG" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <div class="ml-5">
        <h1 class="col">클릭한번으로 더욱 간편해진</h1>
        <h1 class="col" >대출신청, 싹편한 언택트 대출</h1>
        <h4 class="pt-3 col" >서류제출 한번으로 신청가능한 대출상품 리스트 확인 가능합니다.</h4>
        <h4 class="col" >365일 언제 어디서나 내가 필요한 시점에 신청해보세요.</h4>
      </div>
    </div>
    <div class="row justify-content-center align-items-center" style="height: 720px; text-align: left; pointer-events: none; background-color: #fff6e5;">
      <iframe src="https://giphy.com/embed/l0IylQoMkcbZUbtKw" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <div class="ml-5">
        <h1 class="col">기대 그 이상의 손쉬운 대출,</h1>
        <h1 class="col" >싹편한 전세 대출</h1>
        <h4 class="pt-3 col" >온라인으로 신청하고 온라인으로 바로 확인 가능합니다.</h4>
        <h4 class="col" >실제 대출 여부를 확인하여 손쉬운 대출을 경험해보세요.</h4>
      </div>
    </div>
    <!-- 7FB3D5 -->
    <div class="row justify-content-center align-items-center" style="height: 720px; text-align: left; pointer-events: none; background-color: #7db2cc;">
      <iframe src="https://giphy.com/embed/W2i6o8uAXOx0QIoL2a" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <div class="ml-5">
        <h1 class="col">복잡한 과정없는, 조건없는</h1>
        <h1 class="col" >서류 제출하나로 가능, MY CAR 대출</h1>
        <h4 class="pt-3 col" >높은 금리의 자동차 대출을 좀더 낮은 금리의 대출로 전환</h4>
        <h4 class="col" >신차 구입 예정 고객에게 차량구입 대금을 지원해 드립니다.</h4>
      </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'MainPageBottom',
    data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
  },
  created: function () {
    const token = localStorage.getItem('Token')
    if (token != null) {
      this.isLogin = true
    }
  }
}
</script>

<style>
.content {
    /* background: #f2f2f2; */
    padding: 50px;
    text-align: center;
    display: table-cell;
    vertical-align: middle;
}
</style>
