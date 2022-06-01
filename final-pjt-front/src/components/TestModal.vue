<template>
  <div id="test1" class="w3-modal" style="display: none">
  <div class="w3-modal-content w3-animate-top w3-card-4" style="width=5rem">
        <header class="w3-container w3-dark-grey"> 
          <span @click="modalClose('test1')" id="myBtn"
          class="w3-button w3-display-topright">&times;</span>
        </header>
        <br>
        <div class="w3-container">
          <div class="w3-justify w3-container">
            <div class="w3-center">
            <!-- <home-movie-card 
            :movie="firstActorRecomend" :like="firstActorRecomend.like" :watched="firstActorRecomend.watched"
            ></home-movie-card> -->
            </div>
            <br>
            <p>Testing1</p>
          </div>
        </div>
        <footer class="w3-container w3-dark-grey">
          <p>MOVIE MAGAGIN</p>
        </footer>
      </div>
</div> 
</template>

<script>
export default {
  methods: {
  modalClose(id) {
      var inst = document.getElementById(id);
      inst.style = "display: none;"
    },
  },
}
</script>

<style>

</style>