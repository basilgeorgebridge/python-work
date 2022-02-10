<template>
  <div>
    <Grouplist />
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
          <li class="active">
            <nuxt-link to="/grouplist">Group List</nuxt-link>
          </li>
          <li>
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
        <h2>Group List</h2>
        <div class="flex">
          <div class="per_page-div">
            <label for="per_page">no.of rows:</label>
            <input
              type="number"
              id="per_page"
              aria-describedby="groupHelp"
              name="per_page"
              v-model="per_page"
              placeholder="per page show"
              @input="changePerPage"
            />
          </div>
          <div class="per_page-div">
            <label for="filter">Filter using group name :</label>
            <input
              type="text"
              id="filter_by_group_name"
              name="filter_by_group_name"
              v-model="filter_by_group_name"
              placeholder="Enter group name"
              @input="filter_by_group_name_fn"
            />
          </div>
        </div>
        <button class="btn btn-primary btn-block rounded-3 py-2">
          <nuxt-link to="/addgroup"
            ><i class="fa fa-plus"></i> Add group</nuxt-link
          >
        </button>

        <br />
        <table id="datatable1">
          <tr>
            <th>Group Id:</th>
            <th>Group Name:</th>
            <th>Url :</th>
            <th>No.Of Messages :</th>
            <th>Edit</th>
          </tr>
          <tr class="group" v-for="group in groups" :key="group.id">
            <td>{{ group.group_id }}</td>
            <td>{{ group.name }}</td>
            <td @click="copyreview(group)">
              <a>{{ group.url_id }}</a>
            </td>
            <td>{{ group.num_of_reviews }}</td>
            <td>
              <nuxt-link
                :to="`user/groups/${group.group_id}`"
                ><i class="fa fa-edit"></i
              ></nuxt-link>
            </td>
          </tr>
          <br />
          <br />
          <div class="url" v-if="selected">
            {{ selected }}
          </div>
        </table>
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
import Grouplist from "~/components/Grouplist.vue";
export default {
  auth: true,
  components: {
    Grouplist,
  },
  data() {
    return {
      groups: [],
      data: [],
      selected: null,
      filter_by_group_name: "",
      current_page: 1,
      last_page: null,
      per_page: 6,
    };
  },
  mounted() {
    this.grouplist();
  },
  methods: {
    async logout() {
      await this.$auth.logout();
      this.$router.push("/login");
    },
    async changecurrentpage(clickedPage) {
      this.current_Page = clickedPage;
      this.grouplist();
    },
    async changePerPage() {
      this.current_page = 1;
      this.grouplist();
    },
    async filter_by_group_name_fn() {
      console.log("group name is : " + this.filter_by_group_name);
      this.current_page = 1;
      this.grouplist();
    },
    copyreview(group) {
      var select = `http://127.0.0.1:3000/addreview/${group.url_id}`;
      this.selected = "Url for forward = " + select;
    },
    grouplist() {
      try {
        this.$axios
          .get(
            "user/groups?page=" +
              this.current_page +
              "&per_page=" +
              this.per_page +
              "&group_name=" +
              this.filter_by_group_name
          )
          .then((response) => {
            this.groups = response.data[1].groups;
            this.current_page = response.data[0].current_page;
            this.last_page = response.data[0].last_page;
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
.url {
  background-color: rgb(61, 3, 3);
  font-size: larger;
  color: rgb(255, 255, 255);
  text-align: center;
  cursor: copy;
}
.flex {
  display: flex;
}
</style>

