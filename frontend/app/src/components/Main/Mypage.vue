<template>
  <div id="myPage">
    <Navbar />

    <div class="row mt-4">
      <h4 class="col-4">마이페이지</h4>
    </div>
    <!-- 고객데이터 table -->
    <div  class="row mt-3">
      <table class="table offset-1 col-10 ">
        <tbody>
          <tr>
            <th scope="row" class="table-active col-3">이름</th>
            <td>{{ userinfo.user_name }}</td>
          </tr>
          <tr>
            <th scope="row" class="table-active">연락처</th>
            <td>{{ userinfo.phone_number }}</td>
          </tr>
          <tr>
            <th scope="row" class="table-active">직장/직무</th>
            <td>{{ userinfo.job }}</td>
          </tr>
          <tr>
            <th scope="row" class="table-active">소득규모</th>
            <td>{{ userinfo.salary }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <hr style="border: solid 2px grey; width: 85%">
    <div class="row mt-5">
      <h4 class="col-4">제출 서류 확인</h4>
    </div>
    <div  class="row mt-3">
      <table class="table offset-1 col-10">
        <thead>
          <tr class="table-active">
            <th scope="col">No.</th>
            <th scope="col">서류이름</th>
            <th scope="col">파일확인</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(name, idx) in uploadFiles" :key="idx">
            <th scope="row" class="table-active">{{ idx + 1 }}</th>
            <td v-if="name.file_name">{{ name.file_name }}</td>
            <td v-else>파일분류 미완</td>
            <td><button type="button" class="btn btn-warning" v-on:click="viewFile(event, name.file_url)">다운로드</button></td>
          </tr>
        </tbody>
      </table>
    </div>
    <hr style="border: solid 2px grey; width: 85%">

    <div class="row mt-5">
      <h4 class="col-4">신청한 대출 상품</h4>
    </div>
    <div  class="row mt-3">
      <table class="table offset-1 col-10">
        <thead>
          <tr class="table-active">
            <th scope="col">No.</th>
            <th scope="col">대출상품</th>
            <th scope="col">적부판정</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(name, index) in loaninfo" :key="index">
            <th scope="row" class="table-active">{{ index + 1 }}</th>
            <td>{{ loaninfo_name[index].loan_name }}</td>
            <td v-if="loaninfo[index].is_suitable == '부적합 판정'">
              <button type="button" class="btn btn-danger">{{ loaninfo[index].is_suitable }}</button>
            <td v-else-if="loaninfo[index].is_suitable == '적합 판정'">
              <button type="button" class="btn btn-primary">{{ loaninfo[index].is_suitable }}</button>
            </td>
            <td v-else>
              <button type="button" class="btn btn-warning">{{ loaninfo[index].is_suitable }}</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- <div class="row mt-5">
      <router-link :to="{ name: 'BankerLoan' }" class="pa-5 btn btn-secondary btn-sm col-2 offset-5">
        목록
      </router-link>
    </div> -->
  </div>

</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import axios from 'axios';

export default {
  name: 'Mypage',
  components: {
    Navbar,
  },
   data: function () {
    return {
      token:{
          token : localStorage.getItem('Token'),
        },
      userinfo:{
        user_name:'',
        job:'',
        salary:'',
        phone_number:'',
        address: "",
      },
      loaninfo:[],
      loaninfo_name:[],
      uploadFiles:[],
    }
  },
  created(){

  },
  mounted(){
    axios({
      method: 'get',
      url: 'http://j5a205.p.ssafy.io:3000/user/info',
      headers : {"token" : `${this.token.token}`}
    })
    .then((res) =>{
      this.userinfo = res.data.user
      this.uploadFiles = res.data.user_files

      //console.log(this.uploadFiles)
    }).catch((err) =>{
      console.log(err)
    }),
    axios({
      method: 'get',
      url: 'http://j5a205.p.ssafy.io:3000/user/loan/list',
      headers : {"token" : `${this.token.token}`}
    })
    .then((res) =>{
      this.loaninfo = res.data[0]
      this.loaninfo_name = res.data[1]
    }).catch((err) =>{
      console.log(err)
    })
  },
  methods:{
    viewFile(event, url){
      window.open(url)
    }
  }
}
</script>

<style>
#myPage{
  text-align: center;
}
</style>

