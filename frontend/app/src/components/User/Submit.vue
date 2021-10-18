<template>
    <div id="sumbitPage">
        <Navbar />
        <div class="container mt-5">
            <div class="logo md-5 mb-5 text-left">
                <h1>⭐️ 나의 서류 제출하기</h1>
            </div>
            <div>
                <h2 class="text-left">개인정보처리 동의서</h2>
                <hr>
                <div class="mt-1 ml-1 mr-2 mb-1 pt-4 pl-4 pr-4 pb-4 text-left" style="background-color:#f8f8d9">
                    <a class="text-left text-dark pl-3 pt-2 pb-2 pr-3 ">싸피 은행은 개인정보보허법 제 30조에 따라 고객의 개인정보 보호 및 권익을 보호하고 개인정보와 관련한 고객의 고층을 원활하게 처리할 수 있도록 다음과 같은 처리 방침을 두고 있습니다.</a>
                </div>
            </div>
            <br>
            <div>
                <h4 class="text-left">제 1조(개인정보의 처리 목적)</h4>
                <hr>
                <div class="mt-1 ml-1 mr-2 mb-1 pt-4 pl-4 pr-4 pb-4 text-left" style="background-color:#f8f8d9">
                    <a class="text-left text-dark pl-3 pt-2 pb-2 pr-3 ">귀하의 개인(신용)정보는 귀하가 신청한 [당 행]과의 (금융)거래와 관련하여 신용조회회사 또는 신용정보집중기관에 귀하의 개인(신용)정보를 조회하기 위한 목적으로 수집ㆍ이용 됩니다.</a>
                </div>
            </div>
            <br>
            <div>
                <h4 class="text-left">제 2조(개인정보의 처리 및 보유기간)</h4>
                <hr>
                <div class="mt-1 ml-1 mr-2 mb-1 pt-4 pl-4 pr-4 pb-4 text-left" style="background-color:#f8f8d9">
                    <a class="text-left text-dark pl-3 pt-2 pb-2 pr-3 ">귀하의 개인(신용 정보는 수집ㆍ이용에 관한 동의일로부터 개인(신용)정보 제공ㆍ조회 동의의 효력 기간까지 보유ㆍ이용됩니다.
                        <br>단, 개인(신용)정보 제공ㆍ조회 동의의 효력 기간 종료 후에는 금융사고 조사, 분쟁 해결, 민원처리 및 법령상 의무이행만을 위하여 보유ㆍ이용됩니다.
                    </a>
                </div>
            </div>
            <br>
            <div>
                <h4 class="text-left">제 3조(개인정보 수집 출처 등 고지)</h4>
                <hr>
                <div class="mt-1 ml-1 mr-2 mb-1 pt-4 pl-4 pr-4 pb-4 text-left" style="background-color:#f8f8d9">
                    <a class="text-left text-dark pl-3 pt-2 pb-2 pr-3 ">1. 당행은 정보주체 이외로부터 수집한 개인정보를 처리하는 때에는 정당한 사유가 없는 한 정보 주체의 요구가 있는 날로부터 3일 이내에 수집 출처, 처리 목적, 개인정보 처리 정지를 요구할 권리가 있다는 사실을 정보주체에게 알립니다.
                    <br><br><a class="text-left text-dark pl-3 pt-2 pb-2 pr-3 ">2. 개인정보보호법 제 20조 제 2항 각호에 근거하여 제 1항에 따른 정보주체의 요구를 거부하는 경우에는 정당한 사유가 없는 한 정보주체의 요구가 있는 날로부터 3일 이내에 그 거부의 근거와 사유를 정보주체에게 알립니다.</a>
                    </a>
                </div>
            </div>
            <br>
            <div>
                <h4 class="text-left">제 11조(개인정보 처리방침의 변경)</h4>
                <hr>
                <div class="mt-1 ml-1 mr-2 mb-1 pt-4 pl-4 pr-4 pb-4 text-left" style="background-color:#f8f8d9">
                    <a class="text-left text-dark pl-3 pt-2 pb-2 pr-3 ">당행이 개인정보 처리방침을 변경하는 경우에는 변경 및 시행의 시기, 변경된 내용을 지속적으로 공개하며, 변경된 내용은 고객이 쉽게 확인할 수 있도록 변경 전ㆍ후를 비교하여 공개합니다</a>
                </div>
            </div>

            <br><br><br>
            <div class="text-center">
                <b-button class="btn btn-secondary pa-5 mr-2" onclick="window.open('https://www.shinhan.com/hpe/index.jsp#050404040000')">상세보기</b-button>
                <router-link :to="{ name: 'ApplyDetail' }" class="pa-5 mr-2 btn btn-primary btn-md">
                    동의하기
                </router-link>
                <router-link :to="{ name: 'LoanList' }" class="pa-5 mr-2 btn btn-dark btn-md">
                    돌아가기
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
//import axios from 'axios';
export default {
    name: 'SumbitDoc',
    components: {
        //Product,
        Navbar,
//        axios
    },
}
</script>
