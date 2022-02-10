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
              <li>
                <nuxt-link to="/changepassword">Change password</nuxt-link>
              </li>
              <li @click="logout">
                <a>
                  Logout( <span>{{ this.$auth.user.name }}</span> )</a
                >
              </li>
            </ul>
          </div>
        </nav>
        <div class="img"></div>
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-12 col-md-8 col-lg-6 pb-5">
              <form @submit.prevent="addgroup">
                <div class="card border-primary rounded-0">
                  <div class="card-header p-0">
                    <div class="bg-info text-white text-center py-2">
                      <h3>Add Group</h3>
                    </div>
                  </div>
                  <div class="card-body p-3">
                    <div class="form-group">
                      <div class="input-group mb-2">
                        <div class="input-group-prepend">
                          <div class="input-group-text">
                            <i class="fa fa-user text-info"></i>
                          </div>
                        </div>
                        <input
                          type="text"
                          class="form-control"
                          name="groupname"
                          v-model="name"
                          placeholder="Group Name"
                          required
                        />
                      </div>
                    </div>
                    <div class="form-group">
                      <div class="input-group mb-2">
                        <div class="input-group-prepend">
                          <div class="input-group-text">
                            <i class="fa fa-comment text-info"></i>
                          </div>
                        </div>
                        <textarea
                          class="form-control"
                          placeholder="Description"
                          rows="5"
                          v-model="description"
                          required
                        ></textarea>
                      </div>
                    </div>
                    <div class="text-center">
                      <input
                        :disabled="loading"
                        type="submit"
                        value="Add"
                        class="btn btn-primary btn-block rounded-3 py-2"
                      />
                    </div>
                    <div class="success" v-if="success">
                      {{ success }}
                    </div>
                    <div class="error" v-if="error">
                  {{ error }}
                </div>
                    <div class="loader">
                      <img v-if="loading" src="../static/loader.gif" />
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>

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
  position: absolute;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.4);
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
.center .btns {
  margin-top: 20px;
}
.center .btns button {
  height: 55px;
  width: 170px;
  border-radius: 5px;
  border: none;
  margin: 0 10px;
  border: 2px solid white;
  font-size: 20px;
  font-weight: 500;
  padding: 0 10px;
  cursor: pointer;
  outline: none;
  transition: all 0.3s ease;
}
.center .btns button:first-child {
  color: #fff;
  background: none;
}
.btns button:first-child:hover {
  background: white;
  color: black;
}
.center .btns button:last-child {
  background: white;
  color: black;
}
.container {
  margin-top: 280px;
  margin-left: 310px;
}
a {
  cursor: pointer;
}
.active {
  pointer-events: none;
}
.loader {
  float: inline-start;
  margin-left: 100px;
}
</style>
<script>
export default {
  auth: true,
  name: "Addgroup",
  data() {
    return {
      loading: false,
      name: null,
      description: null,
    };
  },
  methods: {
    async logout() {
      await this.$auth.logout();
      this.$router.push("/login");
    },
    async addgroup() {
      this.loading = true;
      const data = {
        name: this.name,
        description: this.description,
      };
      console.log(data);
      try {
        const res = await this.$axios.post("/user/group/create", data);
        this.success = "Group added Successfully";
        this.$router.push("/grouplist");
        this.loading = false;
      } catch (e) {
        this.error = e.response.data.error;
        this.loading = false;
      }
    },
  },
};
</script>
