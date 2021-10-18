<template>
  <div>
    <BankerNavbar />
    <div class="row mt-5">
      <h3 class="col-5 offset-1">고객정보확인</h3>
    </div>
    <!-- 고객데이터 table -->
    <div class="row mt-3" style="text-align: center;">
      <table class="table offset-1 col-10">
        <tbody>
          <tr>
            <th scope="row" class="table-active col-3">이름</th>
            <td>{{ userInfo.user_name }}</td>
          </tr>
          <tr>
            <th scope="row" class="table-active">연락처</th>
            <td>{{ userInfo.phone_number }}</td>
          </tr>
          <tr>
            <th scope="row" class="table-active">직장/직무</th>
            <td>{{ userInfo.job }}</td>
          </tr>
          <tr>
            <th scope="row" class="table-active">소득규모</th>
            <td>{{ userInfo.salary }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <hr style="border: solid 1px grey; width: 85%" />

    <div class="row mt-5">
      <h5 class="col-2 offset-1">대출신청한 상품</h5>
    </div>
    <div class="row mt-3">
      <h3 class="col-2 offset-1">{{ userInfo.loan_name }}</h3>

      <div class="">
        <select class="form-control ml-3" aria-label="Is_Suitable" v-model="checkSuitable" @change="changeSuit">
          <option value="yes">적합 판정</option>
          <option value="no">부적합 판정</option>
        </select>
      </div>
    </div>

    <div class="row mt-5" style="text-align: center;">
      <table class="table offset-1 col-10">
        <thead>
          <tr class="table-active">
            <th class="w-10" scope="col" style="width:10%">No.</th>
            <th class="w-30" scope="col" style="width:40%" >서류내용</th>
            <th class="w-60" scope="col" style="width:50%">제출서류</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(item, idx) in this.userInfo.user_file"
            :key="idx"
            :value="item.value"
            scope="row"
            class=""
          >
            <th scope="row" class="table-active">{{ idx + 1 }}</th>
            <td class="">{{ item.file_name }}</td>
            <td>
              <b-button variant="light" class="btn mt-1" v-on:click="download(item.file_url)">서류 다운로드 받기</b-button>
              <b-button v-b-modal="'myModal' + idx" variant="dark" class="btn mt-1 ml-3">서류 데이터 받기</b-button>
              <b-modal :id="'myModal' + idx" hide-footer scrollable centered no-fade title="서류 데이터 확인하기">
                <div v-for="(v, k) in user_file_data[idx]" :key="k" :value="v.value">
                  <div v-if='k=="file_name"'>
                    서류명: {{v}}
                  </div>
                  <div v-else>
                    {{k}}: {{v}}
                  </div>
                </div>
                <!-- <b-table hover :items="user_file_data[idx]"></b-table> -->
                <div class="mt-3">
                  <b-img :src='item.file_url' fluid thumbnail></b-img>
                </div>
              </b-modal>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="row mt-5">
      <b-button variant="primary" class="pa-3 btn col-1 mr-4 offset-5" @click="modify">
        수정
      </b-button>
      <router-link
        :to="{ name: 'BankerLoan' }"
        class="pa-3 btn btn-secondary btn-sm col-1"
      >
        목록
      </router-link>
    </div>
  </div>
</template>

<script>
import BankerNavbar from "@/components/Banker/BankerNavbar.vue";
import axios from "axios";

export default {
  name: "FileCheck",
  components: {
    BankerNavbar,
  },
  data: function () {
    return {
      userInfo: {
        user_name: "",
        loan_name: "",
        lid: "",
        cid: "",
        is_suitable: "",
        phone_number: "",
        address: "",
        job: "",
        salary: "",
        user_file: [],
      },
      checkSuitable:'check',
      send_data :{
        cid : localStorage.getItem("cid"),
        lid : localStorage.getItem("lid"),
        is_suitable : ''
      },
      user_file_data:[]
    };
  },
  mounted() {
    // console.log(
    //   `cid, lid : ${localStorage.getItem("cid")}, ${localStorage.getItem("lid")}`
    // );
    axios({
      method: "get",
      url: `http://j5a205.p.ssafy.io:3000/detail/user/${localStorage.getItem(
        "cid"
      )}/loan/${localStorage.getItem("lid")}`,
    })
      .then((res) => {
        //console.log(res.data);
        this.userInfo.user_name = res.data.user_detail.user_name;
        this.userInfo.loan_name = res.data.user_detail.loan_name;
        this.userInfo.cid = localStorage.getItem("cid");
        this.userInfo.lid = localStorage.getItem("lid");
        this.userInfo.is_suitable = res.data.user_detail.is_suitable;
        this.userInfo.phone_number = res.data.user_detail.phone_number;
        this.userInfo.address = res.data.user_detail.address;
        this.userInfo.job = res.data.user_detail.job;
        this.userInfo.salary = res.data.user_detail.salary;

        res.data.user_files.forEach((element) => {
          // console.log(element)
          this.userInfo.user_file.push(element);
          // console.log(11222, element.file_url)
          this.getData(element.file_url);
        });

        //console.log(this.userInfo.user_file);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    download(url) {
      window.open(url);
    },

    changeSuit(){
      if(this.checkSuitable == "yes"){
        this.send_data.is_suitable = "적합 판정"
      }else if(this.checkSuitable == "no"){
        this.send_data.is_suitable = "부적합 판정"
      }else{
        alert("적합 판정을 선택해주세요! " + this.checkSuitable)
      }
    },
    modify(){
      if(this.send_data != null){
        axios({
          method:"PATCH",
          url:`http://j5a205.p.ssafy.io:3000/user/loan/status`,
          data : this.send_data
        }).then(res =>{
          res
          alert("판정이 완료되었습니다!")
          this.$router.push({ name: 'BankerLoan'})
        })
      }else{
        alert("적합 판정을 해주셔야 합니다!")
      }
    },
    getData(urlt){
      axios({
        method: "get",
        url: `http://j5a205.p.ssafy.io:3000/data/file_url/`,
        headers:{
          fileurl : urlt
        }
      }).then((res) =>{
        //console.log(11111,res)
        // res.data.forEach((element) => {
        //   this.user_file_data.push(element);
        // });
        this.user_file_data.push(res.data)
        //console.log("fileurl : " + urlt)

      }).catch((err) =>{
        //console.log("fileUrl : " + urlt)
        console.log(err)
      })
    }
  },
};
</script>

<style>
</style>

