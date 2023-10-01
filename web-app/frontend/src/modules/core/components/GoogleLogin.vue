<template>
    <div>
      <button @click="login">Login Using Google</button>
      <div v-if="userDetails">
        <h2>User Details</h2>
        <p>Name: {{ userDetails.name }}</p>
        <p>Email: {{ userDetails.email }}</p>
        <p>Profile Picture: <img :src="userDetails.picture" alt="Profile Picture"></p>
      </div>
    </div>
  </template>
  
<script lang="ts" setup>
  import { googleSdkLoaded } from "vue3-google-login";
  import axios from "axios";

  let userDetails: {name: string; email:string; picture: string;} = {name: "", email: "", picture: ""};

  const login = () => {
    googleSdkLoaded((google: any) => {
      google.accounts.oauth2
      .initCodeClient({
        client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
        scope: "email profile openid",
        redirect_uri: "http://localhost:3000/login",
        callback: (response: any) => {
          if (response.code) {
            console.log("Response is", response);
            sendCodeToBackend(response.code);
          }
        }
      })
      .requestCode();
    });
  };

  const sendCodeToBackend = async (code: string) => {
    try {
      const headers = {
        Authorization: code
      };
      const response = await axios.post("http://localhost:4000/auth", null, { headers });
      let userDetails = response.data;
      console.log("User Details:", userDetails);
      userDetails = userDetails;

      // Redirect to the homepage ("/")
      //this.$router.push("/rex");
    } catch (error) {
      console.error("Failed to send authorization code:", error);
    }
  };
  
</script>