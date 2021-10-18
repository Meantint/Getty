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
      <h5 class="col-5 offset-1">대출신청한 상품</h5>
    </div>
    <div class="row mt-3">
      <h6 class="col-3 offset-2">1. 싹편한 직장인대출</h6>
      <router-link
        :to="{ name: 'FileCheck' }"
        class="pa-5 btn btn-danger btn-sm"
      >
        제출서류 확인
      </router-link>
    </div>
    <div class="row mt-5">
      <router-link
        :to="{ name: 'BankerLoan' }"
        class="pa-3 btn btn-secondary btn-sm col-1 mr-4 offset-5"
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
  name: "UserCheck",
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
      },
    };
  },
  mounted() {
    // console.log(
    //   `cid, lid : ${localStorage.getItem("cid")}, ${localStorage.getItem(
    //     "lid"
    //   )}`
    // );
    axios({
      method: "get",
      url: `http://j5a205.p.ssafy.io:3000/detail/user/${localStorage.getItem(
        "cid"
      )}/loan/${localStorage.getItem("lid")}`,
    })
      .then((res) => {
        // console.log(res.data);
        // console.log(res.data.user_detail);
        // console.log(res.data["user_name"]);
        this.userInfo.user_name = res.data.user_detail.user_name;
        // console.log(this.userInfo.user_name);
        // console.log(res.data.user_name);
        this.userInfo.loan_name = res.data.user_detail.loan_name;
        this.userInfo.cid = localStorage.getItem("cid");
        this.userInfo.lid = localStorage.getItem("lid");
        this.userInfo.is_suitable = res.data.user_detail.is_suitable;
        this.userInfo.phone_number = res.data.user_detail.phone_number;
        this.userInfo.address = res.data.user_detail.address;
        this.userInfo.job = res.data.user_detail.job;
        this.userInfo.salary = res.data.user_detail.salary;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
</style>
