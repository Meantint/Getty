<template>
  <div>
    <!-- <b-button pill variant="secondary" class="mr-1">대출 신청 대상자</b-button> -->
    <h2 class="ml-3">대출 신청 대상자</h2>
    <hr class="ml-3" style="width:12%" align="left"/>
    <!-- <b-button-group>
      <b-button pill variant="secondary" class="mr-1">주택자금대출</b-button>
      <b-button pill variant="secondary" class="mr-1">예/적금 담보대출</b-button>
      <b-button pill variant="secondary" class="mr-1">MY CAR</b-button>
    </b-button-group> -->

    <div class="text-center mt-5 ml-5 mr-5 mb-5" style="border-radius:20px">
      <div class="card-header row">
        <ul class="nav nav-tabs card-header-tabs">
          <li v-on:click="changeCase(1)" class="nav-item">
            <a
              v-if="this.cur === '1'"
              class="nav-link active"
              aria-current="true"
              href="#"
              >전체 신청 고객</a
            >
            <a v-else class="nav-link" href="#">전체 신청 고객</a>
          </li>
          <li v-on:click="changeCase(2)" class="nav-item">
            <a
              v-if="this.cur === '2'"
              class="nav-link active"
              aria-current="true"
              href="#"
              >적합 대상</a
            >
            <a v-else class="nav-link" href="#">적합 대상</a>
          </li>
          <li v-on:click="changeCase(3)" class="nav-item">
            <a
              v-if="this.cur === '3'"
              class="nav-link active"
              aria-current="true"
              href="#"
              >확인중 대상</a
            >
            <a v-else class="nav-link" href="#">확인중 대상</a>
          </li>
          <li v-on:click="changeCase(4)" class="nav-item">
            <a
              v-if="this.cur === '4'"
              class="nav-link active"
              aria-current="true"
              href="#"
              >부적합 대상</a
            >
            <a v-else class="nav-link" href="#">부적합 대상</a>
          </li>
        </ul>
      </div>

      <div v-for="(product, index) in loanlist" :key="index">
        <div class="mt-3 pt-1 pb-1" v-if="(product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')) || (product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')) || (product.is_suitable == '확인중' && (cur === '1' || cur === '3'))" style="box-shadow:0 4px 6px 0 hsla(0, 0%, 0%, 0.2); border-radius:20px">
          <div class="row mb-4 ml-5 inner">
            <div
              v-if="product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')"
              class="mt-3 col-3 offset-1 bg-danger content test"
            >
              <h3 style="color:white">{{ product.is_suitable }}</h3>
            </div>
            <div
              v-else-if="product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')"
              class="mt-3 col-3 offset-1 bg-primary content"
            >
              <h3 style="color:white">{{ product.is_suitable }}</h3>
            </div>
            <div
              v-else-if="product.is_suitable == '확인중' && (cur === '1' || cur === '3')"
              class="mt-3 col-3 offset-1 bg-warning content"
            >
              <h3 style="color:white">{{ product.is_suitable }}</h3>
            </div>

            <div class="col-8">
              <div class="card-body">
                <h5
                v-if="(product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')) || (product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')) || (product.is_suitable == '확인중' && (cur === '1' || cur === '3'))"
                class="card-title">{{ product.user_name }} 고객님</h5>
                <p v-if="(product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')) || (product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')) || (product.is_suitable == '확인중' && (cur === '1' || cur === '3'))" class="card-text">{{ product.loan_name }} 상품 신청</p>
                <b-button
                  v-if="(product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')) || (product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')) || (product.is_suitable == '확인중' && (cur === '1' || cur === '3'))"
                  class="pa-5 btn btn-sm mt-2" variant="primary"
                  @click="saveClientID(product.cid, product.lid)"
                >
                  제출서류 확인
                </b-button>
                <!-- <router-link
                  v-if="(product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')) || (product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')) || (product.is_suitable == '확인중' && (cur === '1' || cur === '3'))"
                  :to="{ name: 'FileCheck' }"
                  class="pa-5 btn btn-primary btn-sm"
                  @click.native="saveClientID(product.cid, product.lid)"
                >
                  제출서류 확인
                </router-link> -->
                <!-- <router-link
                  v-if="(product.is_suitable == '부적합 판정' && (cur === '1' || cur === '4')) || (product.is_suitable == '적합 판정' && (cur === '1' || cur === '2')) || (product.is_suitable == '확인중' && (cur === '1' || cur === '3'))"
                  :to="{ name: 'FileCheck' }"
                  class="pa-5 btn btn-danger btn-sm mt-2"
                >
                  제출서류 확인
                </router-link> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- pagination -->
  <!-- footer 겹쳐서 제외 우선순위가 낮아서 일단 제외 -->
  <!-- footer 하단 고정하기  -->
  <!-- <footer class="fixed-bottom d-flex justify-content-center align-items-center text-white-50 py-2">
      <nav nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
          <li class="page-item">
            <a class="page-link" href="#" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item">
            <a class="page-link" href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </footer> -->
</template>

<script>
import axios from "axios";

export default {
  name: "LoanCheck",
  data: function() {
    return {
      cur: '1',
      loanlist: [],
    };
  },
  mounted() {
    axios({
      method: "get",
      url: "http://j5a205.p.ssafy.io:3000/loan/user/list"
    })
      .then(res => {
        //console.log(`this.cur = ${this.cur}`)
        this.loanlist = res.data;
        // console.log(this.loanlist)
      })
      .catch(err => {
        console.log(err);
      });
  },
  methods: {
    saveClientID(cid, lid) {
      localStorage.setItem("cid", cid);
      localStorage.setItem("lid", lid);

      axios({
        method: "get",
        url: "http://j5a205.p.ssafy.io:3000/loan/user/list"
      })
        .then(res => {
          this.loanlist = res.data;
          this.$router.push({ name: 'FileCheck'})
          //console.log(this.loanlist)
        })
        .catch(err => {
          console.log(err);
        });
      // console.log(localStorage.getItem("cid")); // Print cid
      // console.log(localStorage.getItem("lid")); // Print lid
    },
    changeCase(num) {
      this.cur = String(num);
      //console.log(`Case Change -> ${this.cur}`);
    },
  },
};
</script>

<style>
.card-horizontal {
  display: flex;
  flex: 1 1 auto;
}
.content {
  /* background: #f2f2f2; */
  padding: 50px;
  text-align: center;
  display: table-cell;
  vertical-align: middle;
  border-radius: 20px;
}
</style>
