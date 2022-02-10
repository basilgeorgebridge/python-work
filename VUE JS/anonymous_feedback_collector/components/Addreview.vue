<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <h2 class="text-center text-dark mt-5">Add your Review</h2>

          <div class="card my-5">
            <form
              class="card-body cardbody-color p-lg-5"
              @submit.prevent="addreview"
            >
              <div class="mb-3">
                <textarea
                  class="form-control"
                  id="review"
                  placeholder="Write your review"
                  required
                  v-model="review"
                ></textarea>
              </div>
              <div class="text-center">
                <button
                  :disabled="loading"
                  type="submit"
                  class="btn btn-primary px-5 mb-5 w-100"
                >
                  Add Review
                </button>
                <div class="error" v-if="error">
                  {{ error }}
                </div>
                <div class="success" v-if="success">
                  {{ success }}
                </div>
              </div>
            </form>
            <div class="loader">
              <img v-if="loading" src="../static/loader.gif" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.loader {
  float: inline-start;
  margin-left: 150px;
}
textarea {
  height: 100px;
}
.gradient-custom {
  background: #6a11cb;
  background: -webkit-linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );

  background: linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );
}
</style>
<script>
export default {
  name: "AddReview",
  data() {
    return {
      loading: false,
      review: null,
      url_id: null,
    };
  },
  methods: {
    async addreview() {
      this.loading = true;
      const data = {
        url_id: this.$route.params.id,
        review: this.review,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/review/create", data);
        console.log(res);
        this.success = "your review is posted successfully";
        this.loading = false;
        this.review = "";
      } catch (e) {
        this.error = e.response.data.error;
        this.loading = false;
      }
    },
  },
};
</script>







