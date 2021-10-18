<template>
  <div>
    <Navbar />
    <div class="container mt-5">
      <div class="text-left ml-10 mr-10" id="first">
          <div class="logo mt-3 mb-5">
              <h1>★ 서류 제출하기</h1>
          </div>
          <div class="row mt-3">
          </div>
          <div class="mt-3 pb-3">
              <h5 class="ml-5">제출할 서류들을 첨부해주세요.</h5>
              <h6 class="text-secondary offset-1" style="font-size: 0.8rem">파일 용량은 최대 200MB입니다.</h6>
              <h6 class="text-secondary offset-1" style="font-size: 0.8rem">업로드할 수 있는 확장자는 이미지 파일(jpg, png), PDF입니다.</h6>
          </div>
          <div class="ml-5 mt-5">
            <b-form>
              <div>
                <div class="mt-4 mb-3">
                    <h4>● 서류 제출하기</h4>
                </div>
                <div class="custom-file form-check form-check-inline">
                  <label class="custom-file-label col-6" for="files"> {{ file_name }}</label>
                  <input
                    type="file"
                    id="files"
                    ref="files"
                    accept="image/*"
                    multiple
                    v-on:change="(e)=>handleFileUpload(e)"
                    enctype="multipart/form-data"
                  />
                </div>
              </div>
            </b-form>
          </div>
          <div class="text-center mt-5">
            <!-- 제출하기 누르면 페이지 만들지 말고 alert으로 제출이 완료 되었습니다. 하기? js code 잘 안되네 -->
              <b-button class="mr-3" variant="primary" @click="submitClick">제출하기</b-button>
              <b-button @click="$router.go(-1)" class="ml-3" variant="dark">돌아가기</b-button>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
// 1. 불러온 파일 data에 저장하고 이 걸 읽어서 textarea에 출력.
import Navbar from '@/components/MainPage/Navbar.vue'
import axios from 'axios';

    export default {
        name: 'ApplyDetail',
        components: {
          Navbar,
        },
        data: function () {
            return {
              credential: {
                incomeCertificate: '',
                insuranceCertificate: '',
                paymentCertificate: ''
              },
              token:{
                token : localStorage.getItem('Token')
              },
              files: "",
              file_name :"Choose File!",
            }
        },

        methods:{
          submitClick : function(){
            // 파일 저장
            if (this.files) {
              var formData = new FormData();
              formData.append("fileobject", this.files);

              for (var i = 0; i < this.files.length; i++) {
                formData.append("fileobject", this.files[i]);
              }

              axios({
                method: "post",
                url: `http://j5a205.p.ssafy.io:3000/user/file`,
                data: formData,
                headers: {
                  "token" : this.token.token,
                  "Content-Type": "multipart/form-data"
                },
              })
              .then(function (res) {
                
                console.log(res.data);
                alert("파일업로드가 완료되었습니다.")
                document.location.href="http://j5a205.p.ssafy.io/loanList"
              })
              .catch(function (err) {
                alert("지원하는 서류 파일이 아닙니다.")
                console.log(err)
              });
            }
          },
          handleFileUpload(e){
            this.files = this.$refs.files.files;
            this.file_name = e.target.files[0].name;
          }
        }
    }

</script>
