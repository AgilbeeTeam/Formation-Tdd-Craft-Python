<script setup lang="ts">
import { ref, onMounted } from 'vue';
import apiClient from '@/modules/api';

const items = ref([])
const isLoading = ref(false)
const error = ref(null)


const fetch_message = async () => {
  isLoading.value = true
  try {
    const response = await apiClient.get('/items');
    console.log(response);
    items.value = response.data
  } catch (err) {
    error.value = err.message
    console.error(error);
  } finally {
    isLoading.value = false
  }
};

onMounted(async () => {
 fetch_message();
});

</script>


<template>
  <div class="about">
    <h1 class="green">This is an about page</h1>
    <br/>
    <h3>
      <div v-if="error">Erreur: {{ error }}</div>
      <div v-else>
        <table border="1px">
          <thead>
            <tr>
              <th>Name</th><th>Sell_in</th><th>Quality</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items">
              <td> {{item.name}} </td>
              <td> {{item.sell_in}} </td>
              <td> {{item.quality}} </td>
            </tr>
          </tbody>
        </table>
      </div>
    </h3>
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
