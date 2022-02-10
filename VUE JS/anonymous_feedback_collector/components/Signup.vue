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
                  <h2 class="text-center mb-5">Register Here...!</h2>
                  <form @submit.prevent="register">
                    <div class="form-outline mb-4">
                      <label class="form-label" for="form3Example1cg"
                        >Your Name</label
                      >
                      <input
                        type="text"
                        id="form3Example1cg"
                        v-model="name"
                        class="form-control form-control-lg"
                      />
                    </div>
                    <div class="error" v-if="nameerror">
                      {{ nameerror }}
                    </div>

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
                    <div class="form-outline mb-4">
                      <label class="form-label" for="form3Example4cdg"
                        >Repeat your password</label
                      >
                      <input
                        type="password"
                        id="form3Example4cdg"
                        v-model="password_confirmation"
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
                        Register
                      </button>
                    </div>
                    <br />
                    <div class="loader">
                      <img v-if="loading" src="../static/loader.gif" />
                    </div>
                    <p class="text-center text-muted mt-5 mb-0">
                      Already Have an account?
                      <nuxt-link to="/login" class="fw-bold text-body"
                        ><u>Login here</u></nuxt-link
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
  name: "Register",
  auth: false,
  data() {
    return {
      loading: false,
      email: null,
      password: null,
      password_confirmation: null,
    };
  },
  methods: {
    async register() {
      this.loading = true;
      const data = {
        name: this.name,
        email: this.email,
        password: this.password,
        password_confirmation: this.password_confirmation,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/register", data);
        console.log(res);
        this.$router.push("/login");
        this.loading = false;
      } catch (e) {
        if (
          e.response.data.email &&
          e.response.data.password &&
          e.response.data.name
        ) {
          this.emailerror = e.response.data.email[0];
          this.passworderror = e.response.data.password[0];
          this.nameerror = e.response.data.name[0];
        } else if (e.response.data.email && e.response.data.password) {
          this.nameerror = "";
          this.emailerror = e.response.data.email[0];
          this.passworderror = e.response.data.password[0];
        } else if (e.response.data.name && e.response.data.password) {
          this.emailerror = "";
          this.passworderror = e.response.data.password[0];
          this.nameerror = e.response.data.name[0];
        } else if (e.response.data.email) {
          this.nameerror = "";
          this.passworderror = "";
          this.emailerror = e.response.data.email[0];
        } else if (e.response.data.password) {
          this.passworderror = e.response.data.password[0];
          this.nameerror = "";
          this.emailerror = "";
        } else {
          this.nameerror = e.response.data.name[0];
          this.passworderror = "";
          this.emailerror = "";
        }
        this.loading = false;
      }
    },
  },
};
</script>
<style scoped>
.loader {
  float: inline-start;
  margin-left: 100px;
}
u:hover {
  color: rgb(26, 100, 185);
}
.gradient-custom-3 {
  background: #84fab0;

  background: -webkit-linear-gradient(
    to right,
    rgba(132, 250, 176, 0.5),
    rgba(143, 211, 244, 0.5)
  );

  background: linear-gradient(
    to right,
    rgba(132, 250, 176, 0.5),
    rgba(143, 211, 244, 0.5)
  );
}
.gradient-custom-4 {
  background: #84fab0;

  background: -webkit-linear-gradient(
    to right,
    rgba(132, 250, 176, 1),
    rgba(143, 211, 244, 1)
  );

  background: linear-gradient(
    to right,
    rgba(132, 250, 176, 1),
    rgba(143, 211, 244, 1)
  );
}
.error {
  color: rgb(236, 57, 44);
}
</style>


