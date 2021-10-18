<template>
  <div id="first">
    <Navbar />
    <div class="container">
      <div  v-if="isLogin" class="text-center mt-3 pb-2">
        <div class="custom-file form-check form-check-inline mb-5">
          <div class="float-left text-right col-md-5" >
            <div v-if="hasFile">
              <b-button class="btn btn-warning btn-lg mr-3">
                <router-link :to="{ name: 'Mypage' }" class="text-light"
                  >서류 확인하기
                </router-link>
              </b-button>
              <b-button class="btn btn-warning btn-lg"
                ><router-link :to="{ name: 'SubmitDoc' }" class="text-light">
                  서류 추가하기
                </router-link>
              </b-button>
            </div>
            <div v-else>
              <b-button class="btn btn-warning btn-lg"
                ><router-link :to="{ name: 'SubmitDoc' }" class="text-light"
                  >서류 제출하기</router-link
                ></b-button
              >
            </div>
          </div>
          <div v-if="isLogin" class="float-right text-left col-md-7">
            <div class="text-left">
              <h6>서류를 무작위로 제출하여</h6>
            </div>
            <div class="text-left">
              <h5 class="ml-5">"나의 조건"에 맞는 대출상품을 확인해보세요!</h5>
            </div>
          </div>
        </div>
      </div>
      <div class="logo mt-3 md-3 mb-5 text-left">
        <h1>{{ this.title }}</h1>
      </div>
      <div class="pl-3 pt-3 pb-2 pr-3 mb-3" style="box-shadow:0 4px 6px 0 hsla(0, 0%, 0%, 0.2); border-radius:20px" v-for="(item, idx) in this.loanlist" :key="idx" :value="item.value">
        <div class="text-left">
          <div class="text-secondary">
          </div>
          <div class="mt-3">
            <h2>{{ item.loan_name }}</h2>
          </div>
          <br />
          <div>
            <h5>
              {{item.loan_about}}
            </h5>
          </div>
          <div class="row mt-3">
            <b-button v-if="isLogin && item.is_exist===false" variant="primary" class="pa-5 mr-4 btn-md offset-4" v-on:click="applyPd(event, item.lid)">
              신청하기
            </b-button>
            <b-button v-else-if="isLogin && item.is_exist===true" variant="info" class="pa-5 mr-4 btn-md offset-4" v-on:click="createAlert()">
              신청완료
            </b-button>

            <b-button v-if="isLogin" v-b-modal="'myModal' + item.lid" class="mr-4 ml-1">
              상세보기
            </b-button>

            <b-button v-else v-b-modal="'myModal' + item.lid" class="pa-5 mr-4 btn-md offset-5">
              상세보기
            </b-button>

            <b-modal :id="'myModal' + item.lid" hide-footer scrollable centered no-fade size="lg" :title="item.loan_name">
              <form ref="form" style="text-align: center;">
                <img :src="item.loan_img">
              </form>
            </b-modal>

            <b-button  variant="dark" class="pa-5 mr-4 btn-md" v-on:click="linkDetail(event, item.loan_address)">
              이동하기
            </b-button>
            <!-- <b-button variant="secondary" class="ml-1"> ♡ </b-button> -->
          </div>
        </div>
      </div>
    </div>


  </div>

</template>

<script>
//  1. mounted에서 해당 페이지가 열릴 때 데이터에서 상품 목록들을 가져옴.
//  2. 가져온 상품 목록 데이터를 for문으로 Product.vue에 넘겨줌
//      => 이전 프로젝트 프로필카드 참고하기.
//  3. 넘긴 데이터를 형식에 맞게 가져와서 for문으로 출력 및 페이지네이션?   => 배운 페이지네이션은 SPring에서 하는거엿는데 찾아보기.
//import Product from '@/components/User/Product.vue'
import Navbar from "@/components/MainPage/Navbar.vue";
import axios from "axios";

export default {
  name: "LoanList",
  components: {
    //Product,
    Navbar,
    //        axios
  },
  data: function () {
    return {
      loanlist: [],
      hasFile: false,
      isLogin: false,
      token: {
        token: localStorage.getItem("Token"),
      },
      title: '',
      apply: '',
      img_url:'',
    };
  },
  mounted() {
    //console.log("this.token : ", this.token["token"]);
    if (this.token["token"] == null) {
      axios({
        method: "get",
        url: `http://j5a205.p.ssafy.io:3000/loan`,
      })
        .then((res) => {
          this.loanlist = res.data;
          //console.log(this.loanlist)
        })
        .catch((err) => {
          console.log(err.headers);
        });
        this.title = "⭐️ 대출 상품"
    } else {
      axios({
        method: "get",
        url: `http://j5a205.p.ssafy.io:3000/user/loan`,
        headers: { token: `${this.token.token}` },
      })
        .then((res) => {
          this.loanlist = res.data;
        })
        .catch((err) => {
          console.log(err.headers);
        }),
        axios({
          method: "get",
          url: "http://j5a205.p.ssafy.io:3000/user/info",
          headers: { token: `${this.token.token}` },
        })
          .then((res) => {
            //console.log(res.data);
            if (res.data.user_files[0] != null) {
              this.hasFile = true;
            }
            this.title = "⭐️ 신청 가능한 대출 상품"
            this.isLogin = true
          })
          .catch((err) => {
            console.log(err);
          });
    }
  },
  methods: {
    applyPd(event, id){
      if(this.token.token != null){
        axios({
          method: 'post',
          url: `http://j5a205.p.ssafy.io:3000/user/loan/request/${id}`,
          data: id,
          headers:{
            "token" : localStorage.getItem("Token")
          }
        }).then((res) =>{
          alert("신청완료!!")
          //console.log(res)
          res
          this.$router.go()
        }).catch((err) =>{
          console.log(err)
        })
      }else{
        alert("대출 상품을 신청하려면 로그인 해 주세요!")
      }
    },
    linkDetail(event, addr){

      window.open(addr)
    },
    createAlert(){
      if (window.confirm("이미 신청이 완료된 상태입니다. 마이페이지로 이동하시겠습니까?")) {
        window.open("http://j5a205.p.ssafy.io/mypage","_self");
      }
    },
    openModal(event, url){
      this.img_url = url
      //console.log(this.img_url)
    }
  },
};
</script>
