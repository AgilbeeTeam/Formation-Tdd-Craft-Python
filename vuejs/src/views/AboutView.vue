<script setup lang="ts">
import { ref, onMounted } from 'vue';
import apiClient from '@/modules/api';

const message = ref<string | null>(null);
const errorMessage = ref<string | null>(null);

const fetch_message = async () => {
  try {
    const response = await apiClient.get('/message');
    console.log(response);
    message.value = response.data.message;
  } catch (error) {
    errorMessage.value = 'Erreur lors de la récupération des info de l\'api.';
    console.error(error);
  }
};
onMounted(() => {
  fetch_message();
});

</script>

<template>
  <div class="about">
    <h1 class="green">This is an about page</h1>
    <br/>
    Message: <p v-if="errorMessage">{{ errorMessage }}</p>
    <p>{{ message }}</p>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
