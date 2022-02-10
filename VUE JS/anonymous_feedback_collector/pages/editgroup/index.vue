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
        <!------<title> Website Layout | CodingLab</title>------>
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
              <a>Anonymous Feedback Collector : <span>{{ this.$auth.user.name }}</span> </a>
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
               Logout</a>
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
                      <h3>Edit Group</h3>
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
                          rows="5"
                          placeholder="Description"
                          v-model="group"
                        ></textarea>
                      </div>
                    </div>
                    <br>
                    <div class="text-center flex">
                      <input
                        type="submit"
                        value="Save Changes"
                        class=" button btn btn-primary py-2"
                      /><nuxt-link to="/grouplist">
                      <input
                        type="button"
                        value="Cancel"
                        class="button btn btn-primary  py-2"
                      />
                      </nuxt-link>
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
.center {
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
.container {
  margin-top: 280px;
  margin-left: 310px;
}
a{
 cursor: pointer; 
}
.active {
  pointer-events: none ;
}
.flex{
    display: flex;
}
.button{
height:50px;
width:150px;
margin-left: 70px;

}
</style>
<script>
import Editgroup from "~/components/Editgroup.vue";
export default {
  auth: true,
  components: {
    Editgroup,
  },
  data() {
    return {
      groups: [],
      data: [],
      editing : null,
    };
  },
  mounted() {
    this.editgroup();
  },
  methods: {
    async logout() {
      await this.$auth.logout();
      this.$router.push("/login");
    },
    editgroup() {
      try {
        this.$axios.get("user/groups/"+this.$route.query.id)
        .then((response) => {
          this.groups = response.data[1].groups;
        });
      } catch (e) {
        console.log(e.message);
      }
    },
  },
};