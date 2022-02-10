<template>
  <div>
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
              <li class="active">
                <nuxt-link to="/dashboard">Home</nuxt-link>
              </li>
              <li><nuxt-link to="/grouplist">Group List</nuxt-link></li>
              <li><nuxt-link to="/reviewlist">Review List</nuxt-link></li>
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
        <div class="flex">
          <div class="div1">
            <h3>How to get more customer reviews on Google</h3>
            <li>
              Step 1. Send out review requests. Available tools such as Customer
              Voice can help to simplify this process. Gather reviews from real
              customers quickly and easily.
            </li>

            <li>
              Step 2. Link your Google review page to the business website. Much
              like attaching social pages to a website through their logos, you
              can also create this shortcut to the Google reviews page.
            </li>

            <li>
              Step 3. Create a Google review landing page on the business
              website. This will also be helpful for SEO purposes as the reviews
              will have keywords. Having reviews pulled directly onto the
              business site should encourage other site visitors to leave
              reviews.
            </li>
            <li>
              Step 4. Create a Google review CTA banner or button. This should
              live on the homepage of the business website where most traffic
              will land. Make it as convenient as possible.
            </li>
          </div>
          <br />
          <div class="div2">
            <h3>1. Google reviewsGoogle</h3>
            <p>
              Average monthly US traffic (Alexa): 158.03 million US ranking
              (Alexa): 1 Business reviews for: any business Google My Business
              is a free tool for businesses to manage their online presence
              across Google, including Search and Maps. Google is the go-to
              search engine of choice: as more and more consumers conduct
              multiple searches on it every day, more businesses are vying for
              top SERP results. Very important: Businesses must verify their
              information to complete their Google My Business registration.
              Google My Business puts business data on Search, Maps and Google+.
              Because of this, customers can easily find a location from
              desktop, mobile or anything in between. Google customer reviews
              show up in search and are known to bolster SEO, so they are
              essential to the credibility of all businesses. Google is the king
              of web traffic Did you know that Google’s search engine performs
              over 3.5 billion searches per day (internetlivestats.com)?
              Businesses should aim to be on Google’s snack pack in order to be
              readily found when consumers perform a local search. Users can
              leave reviews for a business easily and simply. The less friction
              involved in the business review process, the easier it is to get
              more reviews. Getting reviews through a business’s Google My
              Business account is a great place to start.
            </p>
          </div>
        </div>
        <div class="flex">
          <br />
          <div class="div3">
            <h3>3. Facebook reviews</h3>
            <p>
              Average monthly US traffic (Alexa): 85.57 million US ranking
              (Alexa): 3 Business reviews for: any business Facebook is a social
              networking platform where users can create profiles, upload photos
              and videos, send messages and keep in touch with friends, family
              and follow their favorite businesses and brands. Companies can
              create business profiles that users can follow and also leave
              business reviews based on their experience with the company.
              Customers now commonly leave reviews on social media Consumers
              increasingly interact with brands through social channels, and
              there is no social platform more prevalent than Facebook. It
              follows, then, that the business reviews on Facebook are seen and
              shared by many potential customers. Businesses should take note of
              the big wins and big mistakes that a business can experience when
              opening themselves up to social media. But again, please note that
              consumers are talking about a business whether that business is
              aware of it or not (and whether businesses have claimed their
              business profile or not). With that being said, it is pertinent
              that businesses are actively monitoring their social media
              mentions at all times. Facebook is becoming a popular review
              resource Due to the sheer size of the user base of Facebook, it is
              gaining momentum towards being one of the most popular business
              review sites. Since most users on the site already have a Facebook
              account, the process to leave a business review is relatively
              friction-less. Consequently, this reduction in friction gives
              Facebook an advantage over other business review websites where
              users must create unique logins or log in to the site each time
              (compared to those consumers that are already living and breathing
              in Facebook).
            </p>
          </div>
          <div class="div4">
            <h3>4. Yelp reviews</h3>
            <p>
              Average monthly US traffic (Alexa): 40.47 million US ranking
              (Alexa): 64 Business reviews for: any business Yelp is a platform
              (review website and app) where users can publish reviews about
              local businesses. Also, Yelp trains small businesses how to
              respond to business reviews, host social events for Yelpers
              (a.k.a. Yelp reviewers) and provides data about businesses
              including health inspection scores (Yelp.com). Reputation
              management is essential on review sites Yelp has become a name
              synonymous with business reviews, as the site has over 102 million
              reviews and counting. As the world’s largest outlet for online
              customer reviews grows, it might be time for all small businesses
              to start caring about what consumers are saying online; and more
              specifically, about their Yelp reviews.
            </p>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");
.div1 {
  background-image: -moz-repeating-radial-gradient();
  background-color: rgb(221, 101, 101);
  color: #fff1f1;
  width: 900px;
  height: 500px;
  padding: 15px;
  border-radius: 15px;
}
.div2 {
  background-image: -moz-repeating-radial-gradient();
  background-color: rgb(85, 42, 42);
  color: #f0d9d9;
  width: 900px;
  height: 500px;
  padding: 15px;
  border-radius: 15px;
  margin-left: 12px;
}
.div3 {
  background-image: -moz-repeating-radial-gradient();
  background-color: rgb(158, 18, 18);
  color: #f0d9d9;
  width: 900px;
  height: 500px;
  padding: 15px;
  border-radius: 15px;
}
.div4 {
  background-image: -moz-repeating-radial-gradient();
  background-color: rgb(32, 83, 224);
  color: #f0d9d9;
  width: 900px;
  height: 500px;
  padding: 15px;
  border-radius: 15px;
  margin-left: 12px;
}
.active {
  pointer-events: none;
}
.flex {
  display: inline-flex;
  padding: 3px;
}
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
  width: 0%;
  height: 8vh;
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
a {
  cursor: pointer;
}
</style>
<script>
export default {
  methods: {
    async logout() {
      await this.$auth.logout();
      this.$router.push("/login");
    },
  },
};
</script>



