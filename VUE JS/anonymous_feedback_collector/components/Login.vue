<template>
  <div>
    <section
      class="vh-100 bg-image"
      style="
        background-image: url('https://mdbcdn.b-cdn.net/img/Photos/new-templates/search-box/img4.webp');
      "
    >
      <div class="mask d-flex align-items-center h-100 gradient-custom-3">
        <div class="container h-100">
          <div
            class="row d-flex justify-content-center align-items-center h-100"
          >
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px">
                <div class="card-body p-5">
                  <h2 class="text-center mb-5">Login Here...!</h2>
                  <form @submit.prevent="login">
                    <div class="form-outline mb-4">
                      <label class="form-label" for="form3Example3cg"
                        >Your Email</label
                      >
                      <input
                        type="email"
                        id="form3Example3cg"
                        v-model="email"
                        class="form-control form-control-lg"
                      />
                    </div>
                    <div class="error" v-if="emailerror">
                      {{ emailerror }}
                    </div>

                    <div class="form-outline mb-4">
                      <label class="form-label" for="form3Example4cg"
                        >Password</label
                      >
                      <input
                        type="password"
                        id="form3Example4cg"
                        v-model="password"
                        class="form-control form-control-lg"
                      />
                    </div>
                    <div class="error" v-if="passworderror">
                      {{ passworderror }}
                    </div>
                    <div class="d-flex justify-content-center">
                      <button
                        :disabled="loading"
                        type="submit"
                        class="
                          btn btn-success btn-block btn-lg
                          gradient-custom-4
                          text-body
                        "
                      >
                        Login
                      </button>
                    </div>
                    <br />
                    <div class="loader">
                      <img v-if="loading" src="../static/loader.gif" />
                    </div>
                    <div class="error" v-if="unauthorized">
                      {{ unauthorized }}
                    </div>

                    <p class="text-center text-muted mt-5 mb-0">
                      Dont Have an account?
                      <nuxt-link to="/signup" class="fw-bold text-body"
                        ><u>Register here</u></nuxt-link
                      >
                    </p>
                    <p class="text-center text-muted mt-5 mb-0">
                      <nuxt-link to="/forgotpassword" class="fw-bold text-body"
                        ><u>Forgot Password?</u></nuxt-link
                      >
                    </p>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  middleware: "guest",
  name: "Login",
  auth: false,
  data() {
    return {
      loading: false,
      email: null,
      password: null,
    };
  },
  methods: {
    async login() {
      this.loading = true;
      const data = {
        email: this.email,
        password: this.password,
      };
      console.log(data);
      try {
        const res = await this.$auth.login({ data: data });
        this.$router.push("/dashboard");
        this.loading = false;
      } catch (e) {
        if (e.response.data.email && e.response.data.password) {
          this.emailerror = e.response.data.email[0];
          this.passworderror = e.response.data.password[0];
          this.unauthorized = "";
        } else if (e.response.data.email) {
          this.passworderror = "";
          this.unauthorized = "";
          this.emailerror = e.response.data.email[0];
        } else if (e.response.data.password) {
          this.emailerror ="";
          this.unauthorized = "";
          this.passworderror = e.response.data.password[0];
        } else {
          this.unauthorized = "Unauthorized";
          this.emailerror = "";
          this.passworderror = "";
        }
        this.loading = false;
      }
    },
  },
};
</script>
<style>
.loader {
  float: inline-start;
  margin-left: 100px;
}
u:hover {
  color: rgb(26, 100, 185);
}
.gradient-custom-3 {
  /* fallback for old browsers */
  background: #84fab0;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(132, 250, 176, 0.5),
    rgba(143, 211, 244, 0.5)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(132, 250, 176, 0.5),
    rgba(143, 211, 244, 0.5)
  );
}
.gradient-custom-4 {
  /* fallback for old browsers */
  background: #84fab0;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(132, 250, 176, 1),
    rgba(143, 211, 244, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(132, 250, 176, 1),
    rgba(143, 211, 244, 1)
  );
}
button:hover {
  background-color: burlywood;
  color: cornsilk;
}
.error {
  color: rgb(236, 57, 44);
}
</style>