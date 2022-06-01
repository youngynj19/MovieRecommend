<template>
<div class="w3-col l3 m6 w3-margin-bottom">
  <router-link :to="{ name: 'actorProfile', params: {localId: actor.id} }">
    <img :src="actorProfileUrl[idx]" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
    <h3>{{actor.name}}</h3> <span><i class="fa fa-heart" :style="actorColor[idx]"></i>  My Actor Level: {{actorLevel[idx]}}%</span>
  </router-link>
  <!-- <p class="w3-opacity">CEO & Founder</p> -->
  <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
  <p><button 
        @click="modalOpen(actor.id)"
        class="w3-button w3-light-grey w3-block"
        id="myBtn">
    Movie Recommend    
  </button></p>
</div>
</template>

<script>
export default {
  name: 'UserProfileCard',
  props: { key: Number, actor: Object, },
  data() {
    return {
      actorProfileUrl: '',
      actorColor: '',      
    }
  },
  methods: {
    modalOpen(id) {
      var inst = document.getElementById(id);
      inst.style = "display: block;"
    },
  },
  created: {

  }
}
</script>

<style>

</style>