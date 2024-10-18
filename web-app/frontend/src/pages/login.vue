<script lang="ts" setup>
import GoogleLogin from "@/components/GoogleLogin.vue";
import CocciInput from "@/components/CocciInput.vue";
</script>

<template>
  <div class="container sm:max-w-md mx-auto px-4">
    <div class="flex flex-col items-center justify-center px-3 py-4">
      <a
        href="#"
        class="flex items-center mb-6 text-2xl font-semibold text-brand"
      >
        <img class="h-16 w-auto" src="/logo.svg" alt="Cocci" />
        Cocci
      </a>
    </div>
    <form>
      <!-- Email input -->
      <div class="relative mb-6">
        <cocci-input type="email" label="Email Address"></cocci-input>
      </div>

      <!-- Password input -->
      <div class="relative mb-6">
        <cocci-input type="password" label="Password"></cocci-input>
      </div>

      <div class="mb-6 flex items-center justify-between">
        <div class="flex items-start">
          <div class="flex items-center h-5">
            <input
              id="remember"
              aria-describedby="remember"
              type="checkbox"
              class="w-4 h-4 border border-brand rounded bg-gray-50 focus:ring-3 focus:ring-brand dark:bg-gray-700 dark:border-brand dark:focus:ring-brand dark:ring-offset-brand"
              required
            />
          </div>
          <div class="ml-3 text-sm">
            <label for="remember" class="text-brand dark:text-brand"
              >Remember me</label
            >
          </div>
        </div>
        <a
          href="#"
          class="text-sm font-medium text-brand hover:underline dark:text-brand"
          >Forgot password?</a
        >
      </div>
      <button
        type="submit"
        class="w-full mb-6 text-offWhite bg-brand focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
      >
        Sign in
      </button>
      <p class="text-sm font-light text-brand dark:text-brand">
        Don’t have an account yet?
        <a
          href="#"
          class="font-medium text-brand hover:underline dark:text-brand"
          >Sign up</a
        >
      </p>
      <!-- Divider -->
      <div
        class="my-4 flex items-center before:mt-0.5 before:flex-1 before:border-t before:border-brand after:mt-0.5 after:flex-1 after:border-t after:border-brand"
      >
        <p class="mx-4 mb-0 text-center font-semibold text-brand">OR</p>
      </div>
      <!-- Social login buttons -->
      <google-login />
    </form>
  </div>
</template>
