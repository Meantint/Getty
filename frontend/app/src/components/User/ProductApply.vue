<template>
    <div id="first">
      <Navbar />
      <div class="container text-left">
        <div class="logo mt-5 md-5 mb-5">
            <h1>⭐️ 대출 신청하기</h1>
        </div>
        <div class="mt-3 mb-5 row">
          <p class="text-secondary mr-3">신청 상품 : </p>
          <!-- 아래는 후에 '신청하기' 버튼 클릭 후 해당하는 이름 전달하기.  -->
          <span class="form-select">
            <select
            id="mm"
            class="selectpicker"
            v-model="apply"
            @focus="checkFlag = false"
            >
              <option
              v-for="(pd, index) in loanlist"
              :key="index"
              :value="pd"
              >
                {{ pd.loan_name }}
              </option>
            </select>
          </span>
        </div>
        <div class="text-center">
            <b-button class="btn btn-primary" @click="applyPd">
              신청하기
            </b-button>
            <b-button @click="$router.go(-1)" class="ml-3" variant="dark">돌아가기</b-button>
        </div>
      </div>
    </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import axios from 'axios'
  export default {
    name: 'ProductApply',
    components: {
      Navbar,
    },
    data: function () {
      return{
        loanlist : [],
        apply : [],
      }
    },
    mounted(){
      axios({
        method: 'get',
        url: `http://j5a205.p.ssafy.io:3000/user/loan`,
        headers:{
          "token" : localStorage.getItem("Token")
        }
      }).then((res) => {
        this.loanlist = res.data
      }).catch((err) => {
        console.log(err.headers)
      })
    },
    methods:{
      applyPd(){
        if(this.apply != null){
          axios({
            method: 'post',
            url: `http://j5a205.p.ssafy.io:3000/user/loan/request/${this.apply.lid}`,
            data: this.apply.lid,
            headers:{
              "token" : localStorage.getItem("Token")
            }
          }).then((res) =>{
            alert("신청완료!!")
            //console.log(res)
            res
          }).catch((err) =>{
            console.log(err)
          })
          this.$router.push({ name: "LoanList" });
        }else{
          alert("신청할 상품을 선택해주세요!")
        }
      }
    }
  }
</script>

<style>
.product  {
  background-color:	#87CEFA;
}
</style>
