<template>
  <div>
    <h1>Browse Recipes</h1>
    <RecipeList />
  </div>
</template>

<script>
import RecipeList from "@/components/RecipeList.vue";
export default {
  components: { RecipeList }
};
</script>