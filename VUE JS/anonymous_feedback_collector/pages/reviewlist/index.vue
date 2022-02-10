<template>
  <div>
    <Reply />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"
    />
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.datatables.net/1.11.4/css/jquery.dataTables.css"
    />

    <script
      type="text/javascript"
      charset="utf8"
      src="https://cdn.datatables.net/1.11.4/js/jquery.dataTables.js"
    ></script>
    <nav>
      <div class="menu">
        <div class="logo">
          <a
            >Anonymous Feedback Collector :
            <span>{{ this.$auth.user.name }}</span></a
          >
        </div>
        <ul>
          <li><nuxt-link to="/dashboard">Home</nuxt-link></li>
          <li>
            <nuxt-link to="/grouplist">Group List</nuxt-link>
          </li>
          <li class="active">
            <nuxt-link to="/reviewlist">Review List</nuxt-link>
          </li>
          <li>
            <nuxt-link to="/changepassword">Change password</nuxt-link>
          </li>
          <li @click="logout">
            <a> Logout</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="img"></div>
    <div>
      <div class="container">
        <br />
        <h2>Review List</h2>
        <div class="flex">
          <div class="per_page-div">
            <label for="per_page">no.of rows:</label>
            <input
              type="number"
              id="per_page"
              aria-describedby="groupHelp"
              name="per_page"
              v-model="per_page"
              @input="changePerPage"
            />
          </div>
        </div>
        <b-table striped hover :items="data" :fields="fields"></b-table>
        <div class="overflow-auto">
          <b-pagination
            v-model="current_page"
            :total-rows="last_page * per_page"
            :per-page="per_page"
            @change="changecurrentpage"
          ></b-pagination>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  auth: true,
  data() {
    return {
      fields: [
        {
          key: "id",
        },
        {
          key: "group_name",
        },
        {
          key: "review",
        },
        {
          key: "created_at",
          sortable: true,
        },
      ],
      reviews: [],
      data: [],
      current_page: 1,
      last_page: null,
      per_page: 6,
    };
  },
  mounted() {
    this.reviewlist();
  },
  methods: {
    async logout() {
      await this.$auth.logout();
      this.$router.push("/login");
    },
    async changePerPage() {
      console.log("per_page is : " + this.per_page);
      this.current_page = 1;
      this.reviewlist();
    },
    async changecurrentpage(clickedPage) {
      this.current_Page = clickedPage;
      this.reviewlist();
    },
    reviewlist() {
      try {
        this.$axios
          .get(
            "user/reviews?page=" +
              this.current_page +
              "&per_page=" +
              this.per_page
          )
          .then((response) => {
            this.reviews = response.data.reviews;
            this.data = response.data.reviews;
            this.current_Page = response.data.current_page;
            this.last_page = response.data.last_page;
          });
      } catch (e) {
        console.log(e.message);
      }
    },
  },
};
</script>
<style scoped>
.filter {
  display: flex;
  justify-content: space-around;
  background: #dfeafd;
  margin-bottom: 20px;
}
h2 {
  margin-top: 30px;
  margin-bottom: 60px;
  text-align: center;
}
.per_page-div > input {
  margin: 10px;
  text-align: center;
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
.menu ul li i a:hover {
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
.container {
  margin-top: 120px;
  margin-left: 310px;
  background: #83a8e7;
  border-radius: 20px;
}
a {
  cursor: pointer;
  color: aliceblue;
}
.pagination {
  display: flex;
  justify-content: end;
  background: #dfeafd;
  margin-bottom: 20px;
}
i {
  cursor: pointer;
  text-align: center;
  color: rgb(233, 86, 60);
}
.active {
  pointer-events: none;
}
button {
  width: 150px;
  height: 45px;
  text-align: center;
  margin-left: 86%;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}
tr:hover {
  background-color: dimgray;
}
tr {
  column-width: 30px;
}
tr:nth-child(even) {
  background-color: #dddddd;
}
.flex {
  display: flex;
}
</style>