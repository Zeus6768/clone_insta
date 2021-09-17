<template>
  <div style="padding:10px">
    <h4>팔로워</h4>
    <input placeholder="🔍">
    <div class="post-header" v-for="(follower, i) in followers" :key="i">
      <div class="profile" :style="`background-image:url(${follower.image})`"></div>
      <span class="profile-name">{{ follower.name }}</span>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';

export default {
  name : "mypage",

  setup() {
    // 컴포넌트를 만들기 전에 이거부터 실행
    let followers = ref([]);

    onMounted(() => {
      axios.get('/follower.json')
      .then((result) => {
        followers.value = result.data
      })
    })


    return { followers }
  },

  data() {
    return {

    }
  }
}
</script>

<style>

</style>