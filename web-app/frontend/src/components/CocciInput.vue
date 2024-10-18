<script lang="ts" setup>
const props = defineProps({
  label: String,
  type: String,
});
</script>

<template>
  <div class="relative">
    <input
      :type="props.type"
      :id="uid"
      :placeholder="props.label"
      class="block px-2.5 pb-2.5 pt-4 w-full text-sm bg-transparent text-brand rounded-lg border-2 border-brand appearance-none dark:text-brand dark:border-brand dark:focus:border-brand focus:outline-none focus:ring-0 focus:border-brand peer"
    />
    <label
      :for="uid"
      class="absolute text-sm text-brand dark:text-brand duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-offWhite dark:bg-black px-2 peer-focus:px-2 peer-autofill:px-2 peer-focus:text-brand peer-autofill:text-brand peer-focus:dark:text-brand peer-autofill:dark:text-brand peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-autofill:top-2 peer-focus:scale-75 peer-autofill:scale-75 peer-focus:-translate-y-4 peer-autofill:-translate-y-4 left-1"
      >{{ props.label }}
    </label>
  </div>
</template>

<script lang="ts">
let uid = 0;

export default {
  data() {
    uid += 1;
    return {
      uid: `${uid}`,
    };
  },
};
</script>
