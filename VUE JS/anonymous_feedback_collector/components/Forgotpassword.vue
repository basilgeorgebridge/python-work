<template>
  <div>
    <link
      href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"
      rel="stylesheet"
      id="bootstrap-css"
    />
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <link
      href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"
      rel="stylesheet"
      id="bootstrap-css"
    />
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <div class="container forget-password">
      <div class="row">
        <div class="col-md-12 col-md-offset-4">
          <div class="panel panel-default">
            <div class="panel-body">
              <div class="text-center">
                <img
                  src="https://usa.afsglobal.org/SSO/SelfPasswordRecovery/images/send_reset_password.svg?v=3"
                  alt="car-key"
                  border="0"
                />
                <h2 class="text-center">Forgot Password?</h2>
                <p>You can reset your password here.</p>
                <div class="error" v-if="error">
                  {{ error }}
                </div>
                <div class="success" v-if="success">
                  {{ success }}
                </div>
                <form @submit.prevent="getLink">
                  <div class="form-group">
                    <label for="password" class="text-info">Enter Email:</label
                    ><br />
                    <input
                      type="text"
                      name="email"
                      id="email"
                      class="form-control"
                    />
                  </div>
                  <div class="form-group">
                    <br />
                    <input
                      :disabled="loading"
                      type="submit"
                      name="submit"
                      class="btn btn-info btn-md center"
                      value="Get Otp"
                    />
                  </div>
                  <div class="loader">
                    <img v-if="loading" src="../static/loader.gif" />
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "ForgotPassword",
  data() {
    return {
      loading: false,
      email: null,
    };
  },
  methods: {
    async getLink() {
      this.loading = true;
      const data = {
        email: this.email,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/forgot-password", data);
        this.loading = false;
      } catch (e) {
        this.error = e.response.data.error;
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
body {
  background: #f3c538;
}
.forget-pwd > a {
  color: #dc3545;
  font-weight: 500;
}
.forget-password .panel-default {
  padding: 31%;
  margin-top: -27%;
}
.forget-password .panel-body {
  padding: 15%;
  margin-bottom: -50%;
  background: #fff;
  border-radius: 5px;
  -webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2),
    0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
img {
  width: 40%;
  margin-bottom: 10%;
}
.btnForget {
  background: #c0392b;
  border: none;
}
.forget-password .dropdown {
  width: 100%;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
}
.forget-password .dropdown button {
  width: 100%;
}
.forget-password .dropdown ul {
  width: 100%;
}
</style>