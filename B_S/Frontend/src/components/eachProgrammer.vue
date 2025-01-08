<template>
  <section id="introduction">
    <h2>{{ name }}</h2>
    <div class="mainContent">
      王玺之，在项目中主要负责B/S系统的搭建。
    </div>
    <div class="otherInform">
      <p>
        <span>
          分工占比：
          {{ percentage }}%
        </span>
      </p>
      <p>
        <span>
          邮 &nbsp&nbsp&nbsp&nbsp&nbsp 箱：
          <a href="#">{{ email }}</a>
        </span>
      </p>
    </div>
  </section>
</template>

<script>
export default {
  name: 'eachProgrammer',
  props: {
    name: {
      type: String,
      required: true
    },
    percentage: {
      type: Number,
      required: true
    },
    email: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
/* 清除默认样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
li {
  list-style: none;
}
a {
  color: #333;
  text-decoration: none;
}

#introduction {
  margin: 80px 40px;
  background-color: #19211e;
  width: 400px;
  height: 600px;
  /* border: 1px solid #000; */
  border-radius: 40px;
  padding-top: 25px;
  padding-left: 30px;
  padding-right: 30px;
}
h2 {
    color: #ffa200;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
div {
    font-size: 20px;
    line-height: 1.6;
    margin-bottom: 10px;
    color: #fff;
}
div .mainContent {
  margin: 20px 0;
  font-weight: lighter;
}
div .otherInform {
  margin: 20px 0;
}
a {
    color: #fff;
}
a:hover {
    text-decoration: underline;
}
span {
  font-size: 20px;
  line-height: 40px;
  color: #fff;
}
</style>