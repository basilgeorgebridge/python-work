<template>
  <div>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <html lang="en" dir="ltr">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="style.css" />
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"
        />
      </head>
      <body>
        <nav>
          <div class="menu">
            <div class="logo">
              <a
                >Anonymous Feedback Collector :
                <span>{{ this.$auth.user.name }}</span>
              </a>
            </div>
            <ul>
              <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
              <li><nuxt-link to="/grouplist">Group List</nuxt-link></li>
              <li><nuxt-link to="/reviewlist">Review List</nuxt-link></li>
              <li class="active">
                <nuxt-link to="/changepassword">Change password</nuxt-link>
              </li>
              <li @click="logout">
                <a> Logout</a>
              </li>
            </ul>
          </div>
        </nav>
        <div class="img"></div>
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
                    <h2 class="text-center">Change Password?</h2>
                    <p>You can reset your password here.</p>
                    <div class="success" v-if="success">
                      {{ success }}
                    </div>
                    <form @submit.prevent="changepassword">
                      <div class="form-group">
                        <label>Current Password</label>
                        <div class="form-group pass_show">
                          <input
                            type="password"
                            v-model="current_password"
                            class="form-control"
                            placeholder="Current Password"
                          />
                        </div>
                        <div class="error" v-if="currenterror">
                          {{ currenterror }}
                        </div>
                        <label>New Password</label>
                        <div class="form-group pass_show">
                          <input
                            type="password"
                            v-model="new_password"
                            class="form-control"
                            placeholder="New Password"
                          />
                        </div>
                        <div class="error" v-if="passworderror">
                          {{ passworderror }}
                        </div>
                        <label>Confirm Password</label>
                        <div class="form-group pass_show">
                          <input
                            type="password"
                            v-model="password_confirmation"
                            class="form-control"
                            placeholder="Confirm Password"
                          />
                        </div>
                        <div class="error" v-if="error">
                          {{ error }}
                        </div>
                        <div class="form-group">
                          <br />
                          <input
                            :disabled="loading"
                            type="submit"
                            name="submit"
                            class="btn btn-info btn-md button"
                            value="Change"
                          />
                        </div>
                        <div class="loader">
                          <img v-if="loading" src="../static/loader.gif" />
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>
<script>
export default {
  auth: true,
  name: "ChangePassword",
  data() {
    return {
      loading: false,
      current_password: null,
      new_password: null,
      password_confirmation: null,
    };
  },
  methods: {
    async logout() {
      await this.$auth.logout();
      this.$router.push("/login");
    },
    async changepassword() {
      this.loading = true;
      const data = {
        current_password: this.current_password,
        password: this.new_password,
        password_confirmation: this.password_confirmation,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/user/change-password", data);
        console.log(res);
        this.success = "Password Changed Successfully";
        this.$router.push("/dashboard");
        this.loading = false;
      } catch (e) {
        if (e.response.data.current_password && e.response.data.password) {
          this.currenterror = e.response.data.current_password[0];
          this.passworderror = e.response.data.password[0];
          this.error = e.response.data.password[0];
        } else if (e.response.data.password) {
          this.currenterror = "";
          this.passworderror = e.response.data.password[0];
          this.error = e.response.data.password[0];
        } else {
           this.currenterror = "";
           this.passworderror = "";
           this.error = "";
           this.error = "request failed";
        }
        this.loading = false;
      }
    },
  },
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
::selection {
  color: #000;
  background: #fff;
}
nav {
  position: absolute;
  background: #1b1b1b;
  width: 100%;
  padding: 10px 0;
  z-index: 12;
}
nav .menu {
  margin: 0px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}
.menu .logo a {
  color: #fff;
  font-size: 35px;
  font-weight: 600;
  text-align: left;
}
.menu ul {
  display: inline-flex;
}
.menu ul li {
  list-style: none;
  margin-left: 5px;
}
.menu ul li:first-child {
  margin-left: 0px;
}
.menu ul li a {
  text-decoration: none;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  padding: 8px 15px;
  border-radius: 5px;
  transition: all 0.3s ease;
}
.menu ul li a:hover {
  background: #fff;
  color: black;
}
.img {
  width: 12%;
  height: 2vh;
  background-size: cover;
  background-position: center;
  position: relative;
}
.img::before {
  content: "";
}
.center {
  position: absolute;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  padding: 0 20px;
  text-align: center;
}
.center .title {
  color: #fff;
  font-size: 55px;
  font-weight: 600;
}
.center .sub_title {
  color: #fff;
  font-size: 52px;
  font-weight: 600;
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
.container {
  margin-top: 80px;
  margin-left: 310px;
}
.button {
  width: 100%;
  height: 40px;
}
.left {
  float: left;
}
a {
  cursor: pointer;
}
.active {
  pointer-events: none;
}
</style>

