<!-- 부모 컴포넌트 -->
<!-- HTML 코드가 들어가는 부분 -->
<template>
  <div>
    <h1>This is home.</h1>

    <!-- props1 -->
    <!-- <C1 title="home title" /> -->

    <!-- props3 -->
    <!-- <C1 title="home title" /> -->
    <C1 title="home title" name="user" />
  </div>
</template>

<!-- Vue JS 코드가 들어가는 부분 -->
<script>
import C1 from "@/components/C1.vue"; // @는 해당 파일과 동일 소스를 가리켜요.

export default {
  components: {
    C1,
  },

  data() {
    return {
      name: "data user",
    };
  },
};
</script>

<!-- CSS코드가 들어가는 부분 -->
<!-- scoped : 넣는 게 정석입니다. 안 넣으면 이 어플리케이션 전체에 적용이 됩니다. -->
<style scoped>
h1 {
  color: red;
}
</style>
