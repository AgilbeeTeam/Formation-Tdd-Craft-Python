import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5172', // ou votre URL d'API
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;