import axios, { AxiosRequestHeaders, RawAxiosRequestHeaders } from 'axios';

const axioss = axios.create({});


// Request interceptor
axioss.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    // Handle request errors here

    return Promise.reject(error);
  }
);
// End of Request interceptor



// Response interceptor
axioss.interceptors.response.use(
  (response) => {
    // Modify the response data here

    return response;
  },
  (error) => {
    // Handle response errors here

    return Promise.reject(error);
  }
);
// End of Response interceptor

export default axioss;